# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T11:07:24.707781+00:00`
- Price records: `672`
- Market context records: `6491`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5859`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `news_risk_high->crypto_alt_24h` score `12.7831` n `32` status `ready` deltaP `34.6512` edge `0.849` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4816` n `32` status `ready` deltaP `53.8995` edge `0.1808` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.1962` n `159` status `ready` deltaP `15.4311` edge `0.7435` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.558` n `32` status `ready` deltaP `18.138` edge `0.5414` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9347` n `38` status `ready` deltaP `41.8329` edge `0.0536` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.8781` n `32` status `ready` deltaP `27.7026` edge `0.0757` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `2.7955` n `181` status `ready` deltaP `-4.4909` edge `0.353` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.8365` n `38` status `ready` deltaP `22.9801` edge `0.0179` maxDD `-0.1113`
- `market_context_high->index_4h` score `0.7041` n `169` status `ready` deltaP `14.5371` edge `0.0294` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `0.689` n `159` status `ready` deltaP `8.7364` edge `0.186` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `0.6268` n `169` status `ready` deltaP `-14.8946` edge `0.3921` maxDD `-10.5788`
- `news_risk_high->crypto_major_1h` score `0.6036` n `38` status `ready` deltaP `5.4283` edge `0.0949` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.5338` n `169` status `ready` deltaP `10.4635` edge `0.1301` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.107` n `38` status `ready` deltaP `1.959` edge `0.0516` maxDD `-2.0756`
- `market_context_high->metal_4h` score `-0.1653` n `169` status `ready` deltaP `10.2465` edge `0.0434` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.4416` n `32` status `ready` deltaP `4.7769` edge `-0.0013` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4421` n `169` status `ready` deltaP `8.656` edge `0.0555` maxDD `-8.2573`
- `market_context_high->metal_1h` score `-0.5866` n `181` status `ready` deltaP `0.2337` edge `0.001` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.6009` n `181` status `ready` deltaP `-0.8903` edge `-0.0028` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.6054` n `181` status `ready` deltaP `5.681` edge `0.0158` maxDD `-5.8368`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
