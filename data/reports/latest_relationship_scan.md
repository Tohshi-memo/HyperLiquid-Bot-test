# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T15:53:05.604256+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8576`

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

- `market_context_high->unknown_4h` score `80.9938` n `135` status `ready` deltaP `4.5472` edge `6.7344` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `14.5561` n `135` status `ready` deltaP `0.6199` edge `1.2578` maxDD `-1.5807`
- `market_context_high->index_24h` score `2.0023` n `135` status `ready` deltaP `27.1875` edge `0.0544` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.5194` n `135` status `ready` deltaP `11.3551` edge `0.0034` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3568` n `135` status `ready` deltaP `11.9817` edge `0.0097` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0623` n `135` status `ready` deltaP `8.849` edge `0.0077` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.2231` n `135` status `ready` deltaP `2.8765` edge `0.0123` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.4666` n `135` status `ready` deltaP `5.7746` edge `0.0445` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.5604` n `135` status `ready` deltaP `5.1375` edge `0.0222` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.6146` n `135` status `ready` deltaP `-0.9614` edge `-0.0041` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.6206` n `135` status `ready` deltaP `8.7847` edge `0.0191` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.821` n `135` status `ready` deltaP `8.0137` edge `-0.0046` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9501` n `135` status `ready` deltaP `16.0995` edge `0.0913` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.5314` n `135` status `ready` deltaP `1.2918` edge `-0.0137` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.905` n `135` status `ready` deltaP `8.0671` edge `0.0839` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-2.0208` n `135` status `ready` deltaP `-1.6401` edge `-0.0118` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.8067` n `135` status `ready` deltaP `-6.1654` edge `-0.0306` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.7845` n `135` status `ready` deltaP `3.2024` edge `-0.0746` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.9623` n `135` status `ready` deltaP `0.544` edge `-0.0259` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.2687` n `135` status `ready` deltaP `0.8706` edge `-0.1579` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
