# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T19:51:05.865080+00:00`
- Price records: `672`
- Market context records: `8228`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5930`

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

- `news_risk_high->unknown_24h` score `7957.2389` n `43` status `ready` deltaP `38.5417` edge `662.8463` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.4458` n `54` status `ready` deltaP `27.2979` edge `0.4982` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1325` n `54` status `ready` deltaP `22.4274` edge `0.1424` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6373` n `54` status `ready` deltaP `22.1149` edge `0.0914` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3171` n `54` status `ready` deltaP `11.241` edge `0.2915` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7907` n `54` status `ready` deltaP `14.5542` edge `0.0956` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7815` n `54` status `ready` deltaP `12.2533` edge `0.1065` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.316` n `54` status `ready` deltaP `16.4691` edge `0.1981` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8689` n `54` status `ready` deltaP `8.5196` edge `0.0624` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4794` n `54` status `ready` deltaP `7.2023` edge `0.0208` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.144` n `54` status `ready` deltaP `6.548` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1503` n `54` status `ready` deltaP `2.6558` edge `0.0101` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5078` n `54` status `ready` deltaP `3.698` edge `0.006` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0952` n `54` status `ready` deltaP `-8.5108` edge `-0.0393` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.0984` n `43` status `ready` deltaP `-18.6491` edge `-0.0456` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-6.1707` n `43` status `ready` deltaP `-23.3769` edge `-0.1069` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-8.8601` n `54` status `ready` deltaP `-32.6389` edge `-0.19` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.7295` n `43` status `ready` deltaP `-23.9624` edge `-0.3599` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-14.7928` n `43` status `ready` deltaP `-22.0849` edge `-0.5024` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.7536` n `43` status `ready` deltaP `-23.4415` edge `-1.2609` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
