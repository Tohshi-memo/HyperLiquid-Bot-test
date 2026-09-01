# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T14:52:26.399032+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11475`

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

- `risk_on_high->unknown_4h` score `7.3449` n `107` status `ready` deltaP `20.83` edge `0.535` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3449` n `107` status `ready` deltaP `20.83` edge `0.535` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8915` n `151` status `ready` deltaP `17.1226` edge `0.4463` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.0711` n `107` status `ready` deltaP `4.1203` edge `0.2028` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.0711` n `107` status `ready` deltaP `4.1203` edge `0.2028` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.9403` n `151` status `ready` deltaP `3.4828` edge `0.2015` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.3608` n `59` status `ready` deltaP `1.5858` edge `0.1375` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `0.2194` n `107` status `ready` deltaP `6.5226` edge `0.0736` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.2194` n `107` status `ready` deltaP `6.5226` edge `0.0736` maxDD `-0.5706`
- `news_risk_high->fx_4h` score `0.1355` n `59` status `ready` deltaP `10.4873` edge `0.0007` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.059` n `107` status `ready` deltaP `7.4948` edge `0.0021` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.059` n `107` status `ready` deltaP `7.4948` edge `0.0021` maxDD `-0.5605`
- `market_context_high->commodity_1h` score `0.013` n `151` status `ready` deltaP `8.1235` edge `0.0119` maxDD `-1.5315`
- `news_risk_high->commodity_4h` score `-0.0174` n `59` status `ready` deltaP `3.072` edge `0.0132` maxDD `-0.8733`
- `news_risk_high->commodity_24h` score `-0.0288` n `59` status `ready` deltaP `3.3545` edge `-0.0055` maxDD `-0.2074`
- `risk_on_high->metal_1h` score `-0.0302` n `107` status `ready` deltaP `10.1489` edge `-0.0003` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0302` n `107` status `ready` deltaP `10.1489` edge `-0.0003` maxDD `-1.699`
- `risk_on_high->commodity_1h` score `-0.0649` n `107` status `ready` deltaP `5.0227` edge `0.0104` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0649` n `107` status `ready` deltaP `5.0227` edge `0.0104` maxDD `-0.8428`
- `risk_on_high->index_4h` score `-0.1145` n `107` status `ready` deltaP `17.2769` edge `0.0032` maxDD `-3.6448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
