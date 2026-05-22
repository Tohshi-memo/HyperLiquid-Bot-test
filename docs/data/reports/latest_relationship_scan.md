# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T18:52:17.121921+00:00`
- Price records: `672`
- Market context records: `1554`
- Flow alert records: `6385`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `12.4353` n `182` status `ready` deltaP `23.6435` edge `0.9787` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.8414` n `182` status `ready` deltaP `26.9974` edge `0.9251` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.2973` n `182` status `ready` deltaP `26.7399` edge `0.7097` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.08` n `182` status `ready` deltaP `20.7799` edge `0.3101` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7463` n `182` status `ready` deltaP `14.2418` edge `0.3666` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.5789` n `182` status `ready` deltaP `15.4876` edge `0.0499` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.3425` n `199` status `ready` deltaP `5.5483` edge `0.101` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.131` n `199` status `ready` deltaP `13.2545` edge `0.2268` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.2327` n `199` status `ready` deltaP `9.1272` edge `0.1802` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.401` n `199` status `ready` deltaP `0.8177` edge `0.0455` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6335` n `199` status `ready` deltaP `-2.1439` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.704` n `199` status `ready` deltaP `-0.1978` edge `0.0032` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7431` n `199` status `ready` deltaP `5.1478` edge `0.004` maxDD `-6.3532`
- `market_context_high->equity_1h` score `-0.8032` n `199` status `ready` deltaP `-1.0328` edge `0.0208` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.8063` n `199` status `ready` deltaP `-0.5732` edge `-0.0002` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.9543` n `199` status `ready` deltaP `-0.8929` edge `0.0193` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3736` n `199` status `ready` deltaP `-10.3973` edge `-0.0139` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.3921` n `199` status `ready` deltaP `10.2111` edge `0.0851` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4668` n `199` status `ready` deltaP `-4.7448` edge `0.0183` maxDD `-3.7119`
- `market_context_high->commodity_4h` score `-5.0921` n `199` status `ready` deltaP `-14.0903` edge `-0.0962` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
