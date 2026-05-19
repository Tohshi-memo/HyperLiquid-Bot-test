# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T00:52:16.407584+00:00`
- Price records: `672`
- Market context records: `1171`
- Flow alert records: `5274`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `20.7887` n `140` status `ready` deltaP `45.9276` edge `1.5394` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.1366` n `140` status `ready` deltaP `22.1627` edge `0.8986` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.6019` n `140` status `ready` deltaP `21.989` edge `0.5799` maxDD `-6.4404`
- `market_context_high->index_24h` score `5.697` n `140` status `ready` deltaP `20.6002` edge `0.3932` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.59` n `140` status `ready` deltaP `-3.4127` edge `0.6553` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.5049` n `153` status `ready` deltaP `12.8657` edge `0.1893` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1734` n `153` status `ready` deltaP `9.3575` edge `0.1037` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5499` n `153` status `ready` deltaP `8.1777` edge `0.023` maxDD `-0.5353`
- `market_context_high->unknown_24h` score `0.3823` n `140` status `ready` deltaP `3.2292` edge `0.2833` maxDD `-10.1706`
- `market_context_high->equity_1h` score `0.2955` n `153` status `ready` deltaP `2.9089` edge `0.043` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1498` n `153` status `ready` deltaP `8.6484` edge `0.0004` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.0807` n `153` status `ready` deltaP `8.1699` edge `0.148` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.0669` n `153` status `ready` deltaP `6.2238` edge `0.0265` maxDD `-4.1256`
- `market_context_high->unknown_4h` score `-0.148` n `153` status `ready` deltaP `5.8833` edge `0.0701` maxDD `-6.7322`
- `market_context_high->metal_1h` score `-0.4609` n `153` status `ready` deltaP `5.6143` edge `-0.0148` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.5219` n `153` status `ready` deltaP `1.678` edge `0.0296` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8412` n `153` status `ready` deltaP `-3.4451` edge `-0.0041` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.0165` n `153` status `ready` deltaP `-3.8976` edge `-0.0047` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.354` n `153` status `ready` deltaP `3.795` edge `0.0976` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.9318` n `153` status `ready` deltaP `4.5802` edge `-0.0828` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
