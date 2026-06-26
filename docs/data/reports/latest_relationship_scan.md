# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T08:07:30.363350+00:00`
- Price records: `672`
- Market context records: `4808`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7578`

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

- `market_context_high->unknown_1h` score `11.4435` n `118` status `ready` deltaP `11.4128` edge `0.9193` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.8558` n `117` status `ready` deltaP `18.1038` edge `0.655` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.2173` n `111` status `ready` deltaP `12.6314` edge `0.1929` maxDD `-4.7201`
- `market_context_high->equity_4h` score `0.268` n `117` status `ready` deltaP `9.6441` edge `0.1154` maxDD `-6.9604`
- `market_context_high->commodity_4h` score `0.1213` n `117` status `ready` deltaP `12.4753` edge `0.0496` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.1126` n `118` status `ready` deltaP `5.7368` edge `0.0299` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.3077` n `117` status `ready` deltaP `5.1582` edge `0.0038` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.3109` n `117` status `ready` deltaP `7.5972` edge `0.0148` maxDD `-5.4242`
- `market_context_high->equity_1h` score `-0.6894` n `118` status `ready` deltaP `2.144` edge `0.005` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.9587` n `118` status `ready` deltaP `-1.7913` edge `-0.003` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.4123` n `118` status `ready` deltaP `-1.497` edge `-0.0073` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1236` n `111` status `ready` deltaP `19.909` edge `0.1059` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3117` n `118` status `ready` deltaP `-1.2915` edge `-0.0702` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-2.7413` n `111` status `ready` deltaP `-11.8572` edge `-0.0184` maxDD `-3.1464`
- `market_context_high->crypto_major_1h` score `-3.0519` n `118` status `ready` deltaP `-0.0964` edge `-0.0816` maxDD `-22.0555`
- `market_context_high->crypto_alt_1h` score `-3.1865` n `118` status `ready` deltaP `0.8982` edge `-0.0511` maxDD `-14.9676`
- `market_context_high->index_24h` score `-4.3775` n `111` status `ready` deltaP `-7.0899` edge `-0.1231` maxDD `-23.2678`
- `market_context_high->crypto_alt_4h` score `-4.4922` n `117` status `ready` deltaP `6.6826` edge `-0.0126` maxDD `-43.2966`
- `market_context_high->crypto_major_4h` score `-8.291` n `117` status `ready` deltaP `3.7811` edge `-0.1726` maxDD `-67.9107`
- `market_context_high->metal_4h` score `-8.6018` n `117` status `ready` deltaP `4.9028` edge `-0.3114` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
