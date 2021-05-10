"""
Complete solution
"""


def query_01(connection, column_names, X=150):
    # Bouw je query
    query = """
    SELECT
        M.W, 
        M.L, 
        M.yearID, 
        P.nameGiven, 
        P.nameLast, 
        M.teamID 
    FROM 
        Managers as M, 
        Master as P
    WHERE 
        M.G > {X} AND 
        M.playerID = P.playerID
    ORDER BY 
        M.W DESC, 
        M.L, 
        M.yearID, 
        M.teamID, 
        P.nameLast, 
        P.nameGiven;
    """.format(
        X=X
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_02(connection, column_names):
    # Bouw je query
    query = """
    SELECT 
        nameFirst, 
        nameLast
    FROM 
        Master
    WHERE 
        1959 < birthYear AND
        birthYear < 1970
    ORDER BY 
        nameLast, 
        nameFirst;
    """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_03(connection, column_names, X="Blue"):
    # Bouw je query
    query = """
    SELECT DISTINCT 
        name, 
        teamID
    FROM 
        Teams
    WHERE 
        name LIKE '%{X}%'
    ORDER BY 
        teamID, 
        name;
    """.format(
        X=X
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 04
def query_04(connection, column_names, X=3):
    # Bouw je query
    query = """
    SELECT 
        P.nameLast, 
        P.nameFirst, 
        M.teamID, 
        COUNT(M.yearID) as NumYears, 
        AVG(W) as AvgW, 
        AVG(rank) as AvgR
    FROM 
        Managers as M, 
        Master as P
    WHERE 
        M.playerID=P.playerID
    GROUP BY 
        M.playerID, 
        M.teamID
    HAVING 
        COUNT(M.yearID) >= {X}
    ORDER BY 
        AvgR, 
        NumYears DESC, 
        AvgW DESC, 
        M.teamID, 
        P.nameLast, 
        P.nameFirst;
    """.format(
        X=X
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_04_v_02(connection, column_names, X=3):
    # Bouw je query
    query = """
    SELECT 
        P.nameLast, 
        P.nameFirst, 
        M.teamID, 
        COUNT(DISTINCT M.yearID) as NumYears, 
        AVG(W) as AvgW, 
        AVG(rank) as AvgR
    FROM 
        Managers as M, 
        Master as P
    WHERE 
        M.playerID=P.playerID
    GROUP BY 
        M.playerID, 
        M.teamID
    HAVING 
        COUNT(DISTINCT M.yearID) >= {X}
    ORDER BY 
        AvgR, 
        NumYears DESC, 
        AvgW DESC, 
        M.teamID, 
        P.nameLast, 
        P.nameFirst;
    """.format(
        X=X
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 05
def query_05(connection, column_names, X=1975):
    # Bouw je query
    query = """
    SELECT 
        T.name, 
        P.nameFirst, 
        P.nameLast, 
        SUM(B.HR) as HRs
    FROM 
        Teams as T, 
        Batting as B, 
        Master as P
    WHERE 
        T.teamID=B.teamID AND 
        T.yearID={X} AND 
        B.yearID={X} AND 
        B.playerID=P.playerID
    GROUP BY 
        T.teamID,  
        B.playerID
    HAVING 
        SUM(B.HR) >= ALL (
                        SELECT 
                            SUM(A.HR) 
                        FROM 
                            Batting as A 
                        WHERE 
                            A.teamID=T.teamID AND 
                            A.yearID={X}
                        GROUP BY 
                            A.playerID)
    ORDER BY 
        T.name, 
        P.nameLast, 
        P.nameFirst;
    """.format(
        X=X
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 06
def query_06(connection, column_names):
    # Bouw je query
    query = """
    SELECT DISTINCT 
        A.birthYear, 
        A.birthMonth, 
        A.birthDay, 
        A.nameLast, 
        A.NameFirst
    FROM 
        Master as A, 
        Master as B
    WHERE 
        A.birthYear=B.birthYear AND 
        A.birthMonth=B.birthMonth AND 
        A.birthDay=B.birthDay AND 
        NOT (A.playerID = B.playerID) AND 
        A.birthYear > 0 AND 
        A.birthMonth > 0 AND 
        A.birthDay > 0 
    ORDER BY 
        A.birthYear, 
        A.birthMonth, 
        A.birthDay, 
        A.nameLast, 
        A.nameFirst;
    """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 07
def query_07(connection, column_names, X=1950):
    # Bouw je query
    query = """
    SELECT 
        Master.nameFirst, 
        Master.nameLast, 
        AwardsPlayers.awardID, 
        AwardsPlayers.yearID
    FROM 
        Master LEFT OUTER JOIN AwardsPlayers
        ON 
            Master.playerID = AwardsPlayers.playerID
    WHERE 
        Master.birthYear = {X}
    ORDER BY 
        Master.nameLast, 
        Master.nameFirst, 
        AwardsPlayers.awardID, 
        AwardsPlayers.yearID;
    """.format(
        X=X
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 08
def query_08(connection, column_names, N=5, R=1):
    # Bouw je query
    query = """
    SELECT 
        P1.nameFirst, 
        P1.nameLast, 
        M1.yearID-P1.birthYear as Age, 
        T.name, 
        COUNT(*) as NrRankR
    FROM 
        Managers as M1, 
        Master as P1, 
        Teams as T
    WHERE 
        M1.playerID=P1.playerID AND 
        M1.rank={R} AND 
        T.teamID=M1.teamID AND 
        T.yearID=M1.yearID
    GROUP BY 
        M1.playerID
    HAVING 
        MIN(M1.yearID-P1.birthYear)-{N} <= ALL(
            SELECT  
                M.yearID-P.birthYear
            FROM
                Managers as M, 
                Master as P
            WHERE 
                M.playerID=P.playerID AND 
                M.rank={R}
            )
    ORDER BY 
        Age, 
        P1.nameLast, 
        P1.nameFirst;
    """.format(
        N=N, R=R
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df
