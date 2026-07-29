# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T01:07:30.718913+00:00`
- Price records: `672`
- Market context records: `8253`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5924`

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

- `news_risk_high->unknown_24h` score `7957.6373` n `43` status `ready` deltaP `38.5417` edge `662.8795` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.1819` n `54` status `ready` deltaP `26.3832` edge `0.4823` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1073` n `54` status `ready` deltaP `22.4274` edge `0.1403` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6995` n `54` status `ready` deltaP `22.8771` edge `0.0915` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3235` n `54` status `ready` deltaP `11.3934` edge `0.2913` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7955` n `54` status `ready` deltaP `14.5542` edge `0.096` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7073` n `54` status `ready` deltaP `11.3551` edge `0.1063` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3403` n `54` status `ready` deltaP `16.6215` edge `0.2002` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.1642` n `54` status `ready` deltaP `10.5013` edge `0.0738` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4734` n `54` status `ready` deltaP `7.2023` edge `0.0203` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1666` n `54` status `ready` deltaP `6.9971` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0868` n `54` status `ready` deltaP `3.2546` edge `0.0114` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4658` n `54` status `ready` deltaP `4.4602` edge `0.0063` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.148` n `54` status `ready` deltaP `-8.6605` edge `-0.0427` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.078` n `43` status `ready` deltaP `-18.6491` edge `-0.0439` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-5.6114` n `43` status `ready` deltaP `-19.7311` edge `-0.0846` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-9.0103` n `54` status `ready` deltaP `-32.7913` edge `-0.2015` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.6936` n `43` status `ready` deltaP `-24.3096` edge `-0.3546` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-14.0307` n `43` status `ready` deltaP `-18.4391` edge `-0.4632` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.1188` n `43` status `ready` deltaP `-23.4415` edge `-1.208` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
