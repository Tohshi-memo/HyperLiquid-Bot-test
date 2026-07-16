# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T23:22:27.086673+00:00`
- Price records: `672`
- Market context records: `6969`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11735`

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

- `market_context_high->fx_1h` score `-0.2515` n `237` status `ready` deltaP `2.1842` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3637` n `237` status `ready` deltaP `2.2803` edge `0.0246` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.7014` n `237` status `ready` deltaP `-1.641` edge `-0.0022` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7169` n `237` status `ready` deltaP `-0.0891` edge `-0.0002` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.9069` n `237` status `ready` deltaP `12.2401` edge `0.0085` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.1933` n `237` status `ready` deltaP `2.7294` edge `0.0176` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.3101` n `237` status `ready` deltaP `-3.1235` edge `-0.0162` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.6297` n `237` status `ready` deltaP `-2.2803` edge `-0.0305` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `-1.6564` n `224` status `ready` deltaP `-9.2014` edge `0.304` maxDD `-18.7342`
- `market_context_high->commodity_4h` score `-1.6695` n `237` status `ready` deltaP `-4.4329` edge `-0.0355` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.8576` n `237` status `ready` deltaP `7.0572` edge `-0.0153` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.9882` n `237` status `ready` deltaP `2.3882` edge `-0.0154` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.0362` n `237` status `ready` deltaP `4.871` edge `0.0048` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-3.1152` n `237` status `ready` deltaP `-0.2463` edge `-0.0192` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-3.3063` n `237` status `ready` deltaP `-8.4105` edge `0.0171` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.7729` n `224` status `ready` deltaP `-6.4485` edge `-0.0846` maxDD `-5.2791`
- `market_context_high->crypto_major_4h` score `-3.7858` n `237` status `ready` deltaP `-1.5012` edge `-0.0469` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-4.4281` n `224` status `ready` deltaP `-7.3661` edge `-0.0152` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.6968` n `237` status `ready` deltaP `4.011` edge `-0.0918` maxDD `-66.7371`
- `market_context_high->index_24h` score `-12.24` n `224` status `ready` deltaP `-5.7043` edge `-0.1242` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
