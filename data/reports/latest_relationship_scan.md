# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T11:22:32.309827+00:00`
- Price records: `672`
- Market context records: `7134`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11670`

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

- `market_context_high->fx_4h` score `0.502` n `139` status `ready` deltaP `17.8584` edge `0.0153` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1326` n `151` status `ready` deltaP `4.6903` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.3882` n `151` status `ready` deltaP `-2.6986` edge `0.0415` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.5868` n `151` status `ready` deltaP `0.3311` edge `0.0256` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.6362` n `151` status `ready` deltaP `3.6424` edge `0.0352` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.694` n `151` status `ready` deltaP `-1.5743` edge `-0.0164` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7128` n `151` status `ready` deltaP `1.8103` edge `-0.005` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.3418` n `151` status `ready` deltaP `-4.5128` edge `-0.0053` maxDD `-2.1142`
- `market_context_high->unknown_4h` score `-2.1806` n `139` status `ready` deltaP `-5.2115` edge `0.02` maxDD `-5.0245`
- `market_context_high->commodity_4h` score `-2.2571` n `139` status `ready` deltaP `-6.3235` edge `-0.0424` maxDD `-2.9494`
- `market_context_high->crypto_major_4h` score `-3.2958` n `139` status `ready` deltaP `1.1405` edge `-0.0011` maxDD `-24.6569`
- `market_context_high->equity_1h` score `-3.504` n `151` status `ready` deltaP `-0.0674` edge `-0.0458` maxDD `-14.9936`
- `market_context_high->index_4h` score `-4.0933` n `139` status `ready` deltaP `-2.8952` edge `-0.0519` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.3111` n `139` status `ready` deltaP `-7.7229` edge `-0.0127` maxDD `-5.2725`
- `market_context_high->commodity_24h` score `-4.3646` n `135` status `ready` deltaP `-12.8009` edge `-0.1475` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9051` n `135` status `ready` deltaP `-15.1273` edge `-0.0252` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-5.3248` n `139` status `ready` deltaP `-2.8524` edge `-0.0375` maxDD `-22.9772`
- `market_context_high->unknown_24h` score `-9.9794` n `135` status `ready` deltaP `-31.5509` edge `-0.1066` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.8988` n `139` status `ready` deltaP `-1.5902` edge `-0.2572` maxDD `-64.2346`
- `market_context_high->metal_24h` score `-14.4782` n `135` status `ready` deltaP `-29.1319` edge `-0.1829` maxDD `-41.0187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
