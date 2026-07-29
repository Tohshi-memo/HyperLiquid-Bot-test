# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T08:22:28.537173+00:00`
- Price records: `672`
- Market context records: `8284`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `6411.2488` n `51` status `ready` deltaP `38.4906` edge `534.0224` maxDD `-0.3284`
- `news_risk_high->equity_4h` score `7.1157` n `54` status `ready` deltaP `26.2308` edge `0.4778` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9539` n `54` status `ready` deltaP `21.0801` edge `0.1365` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6833` n `54` status `ready` deltaP `22.4198` edge `0.0932` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.036` n `54` status `ready` deltaP `9.8691` edge `0.2646` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7848` n `54` status `ready` deltaP `13.9554` edge `0.0991` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.542` n `54` status `ready` deltaP `17.2313` edge `0.222` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.5023` n `54` status `ready` deltaP `10.1575` edge `0.0972` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `0.9981` n `54` status `ready` deltaP `9.1294` edge `0.0691` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3992` n `54` status `ready` deltaP `6.3041` edge `0.0201` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1689` n `54` status `ready` deltaP `6.9971` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1527` n `54` status `ready` deltaP `2.5061` edge `0.0109` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4073` n `54` status `ready` deltaP `5.3748` edge `0.0077` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0952` n `54` status `ready` deltaP `-8.3611` edge `-0.0403` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.8153` n `51` status `ready` deltaP `-20.1083` edge `-0.049` maxDD `-5.1242`
- `news_risk_high->metal_24h` score `-5.5153` n `51` status `ready` deltaP `-18.7296` edge `-0.0601` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-8.7506` n `54` status `ready` deltaP `-30.5048` edge `-0.1951` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9202` n `51` status `ready` deltaP `-11.0805` edge `-0.3255` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0674` n `51` status `ready` deltaP `-24.2239` edge `-0.3133` maxDD `-27.4656`
- `news_risk_high->crypto_major_24h` score `-33.9548` n `51` status `ready` deltaP `-15.6556` edge `-1.2727` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
