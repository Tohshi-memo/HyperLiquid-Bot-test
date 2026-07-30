# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T15:37:33.650733+00:00`
- Price records: `672`
- Market context records: `8423`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5742`

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

- `news_risk_high->unknown_24h` score `6253.3085` n `52` status `ready` deltaP `41.6133` edge `520.8737` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.7386` n `52` status `ready` deltaP `23.628` edge `0.3804` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.2935` n `52` status `ready` deltaP `19.1847` edge `0.0941` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1618` n `52` status `ready` deltaP `18.75` edge `0.0742` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5572` n `52` status `ready` deltaP `12.31` edge `0.0911` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.358` n `52` status `ready` deltaP `9.9148` edge `0.0868` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.3413` n `52` status `ready` deltaP `5.4057` edge `0.2053` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `1.0752` n `52` status `ready` deltaP `14.4348` edge `0.1808` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.1851` n `52` status `ready` deltaP `3.213` edge `0.0408` maxDD `-0.7433`
- `news_risk_high->fx_1h` score `0.125` n `52` status `ready` deltaP `5.942` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0347` n `52` status `ready` deltaP `2.7983` edge `0.0131` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.4002` n `52` status `ready` deltaP `0.7025` edge `0.0023` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4181` n `52` status `ready` deltaP `4.8077` edge `0.0101` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9477` n `52` status `ready` deltaP `-6.4717` edge `-0.0406` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7385` n `52` status `ready` deltaP `-27.7244` edge `-0.0612` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.3269` n `52` status `ready` deltaP `-25.598` edge `-0.1925` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.6097` n `52` status `ready` deltaP `-34.5352` edge `-0.2102` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.5077` n `52` status `ready` deltaP `-12.2596` edge `-0.3666` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.5958` n `52` status `ready` deltaP `-26.6827` edge `-0.3215` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.7457` n `52` status `ready` deltaP `-24.773` edge `-1.0261` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
