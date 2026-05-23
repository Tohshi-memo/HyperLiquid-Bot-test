# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T21:22:17.477748+00:00`
- Price records: `672`
- Market context records: `1669`
- Flow alert records: `6712`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `9.6579` n `164` status `ready` deltaP `28.4285` edge `0.8579` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.9054` n `195` status `ready` deltaP `22.8901` edge `0.5226` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8268` n `164` status `ready` deltaP `20.0249` edge `0.3232` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.0246` n `195` status `ready` deltaP `18.9955` edge `0.3963` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.2004` n `195` status `ready` deltaP `13.2028` edge `0.2048` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8207` n `164` status `ready` deltaP `19.3159` edge `0.5128` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7623` n `207` status `ready` deltaP `6.644` edge `0.1216` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.6131` n `164` status `ready` deltaP `26.0402` edge `1.0584` maxDD `-88.8062`
- `market_context_high->crypto_major_24h` score `0.446` n `164` status `ready` deltaP `25.2237` edge `0.7476` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.1402` n `207` status `ready` deltaP `3.2349` edge `0.0476` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.2468` n `195` status `ready` deltaP `3.5147` edge `0.0649` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.2686` n `207` status `ready` deltaP `4.2762` edge `0.0765` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.4103` n `164` status `ready` deltaP `6.9922` edge `0.0241` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.5988` n `207` status `ready` deltaP `-0.0788` edge `0.0138` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8073` n `207` status `ready` deltaP `-0.1873` edge `-0.0028` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-1.0435` n `207` status `ready` deltaP `5.3581` edge `0.0109` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.0439` n `195` status `ready` deltaP `10.4847` edge `0.1123` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.2595` n `195` status `ready` deltaP `-8.3224` edge `-0.0131` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.2675` n `207` status `ready` deltaP `-1.6228` edge `-0.0352` maxDD `-14.9083`
- `market_context_high->unknown_24h` score `-3.0452` n `164` status `ready` deltaP `10.0958` edge `0.2318` maxDD `-35.8966`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
