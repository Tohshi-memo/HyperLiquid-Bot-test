# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T02:37:27.044117+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `4.91` n `73` status `ready` deltaP `18.0836` edge `0.4094` maxDD `-4.9964`
- `market_context_high->equity_24h` score `1.1779` n `73` status `ready` deltaP `14.5913` edge `0.0221` maxDD `-1.0305`
- `market_context_high->commodity_4h` score `0.5815` n `109` status `ready` deltaP `12.0888` edge `0.0529` maxDD `-2.4692`
- `market_context_high->commodity_24h` score `0.4295` n `73` status `ready` deltaP `12.6469` edge `0.1348` maxDD `-4.666`
- `market_context_high->metal_24h` score `0.406` n `73` status `ready` deltaP `4.8384` edge `0.0756` maxDD `-1.5883`
- `market_context_high->index_24h` score `0.3225` n `73` status `ready` deltaP `12.9081` edge `-0.0364` maxDD `-0.4888`
- `market_context_high->unknown_1h` score `0.2699` n `109` status `ready` deltaP `8.4739` edge `-0.0081` maxDD `-0.7386`
- `market_context_high->index_1h` score `0.2079` n `109` status `ready` deltaP `8.4011` edge `0.0033` maxDD `-0.3584`
- `market_context_high->equity_1h` score `-0.0753` n `109` status `ready` deltaP `4.2287` edge `0.0224` maxDD `-1.8201`
- `market_context_high->fx_4h` score `-0.2096` n `109` status `ready` deltaP `4.7466` edge `0.0016` maxDD `-0.3904`
- `market_context_high->crypto_major_4h` score `-0.41` n `109` status `ready` deltaP `2.6069` edge `0.0495` maxDD `-4.5553`
- `market_context_high->metal_4h` score `-0.4943` n `109` status `ready` deltaP `6.2709` edge `-0.0094` maxDD `-3.3284`
- `market_context_high->metal_1h` score `-0.6703` n `109` status `ready` deltaP `-1.9942` edge `-0.0044` maxDD `-1.4598`
- `market_context_high->commodity_1h` score `-0.7528` n `109` status `ready` deltaP `-5.3453` edge `0.0004` maxDD `-1.5684`
- `market_context_high->fx_1h` score `-0.801` n `109` status `ready` deltaP `-4.616` edge `0.0002` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.8709` n `109` status `ready` deltaP `-5.7689` edge `-0.0048` maxDD `-0.8045`
- `market_context_high->crypto_major_1h` score `-0.8895` n `109` status `ready` deltaP `-2.424` edge `-0.0023` maxDD `-3.6463`
- `market_context_high->unknown_24h` score `-1.2219` n `73` status `ready` deltaP `0.2256` edge `-0.089` maxDD `-1.5327`
- `market_context_high->crypto_alt_1h` score `-1.4369` n `109` status `ready` deltaP `-3.829` edge `-0.0013` maxDD `-3.4335`
- `market_context_high->equity_4h` score `-1.8493` n `109` status `ready` deltaP `-9.2722` edge `-0.0411` maxDD `-5.4002`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
