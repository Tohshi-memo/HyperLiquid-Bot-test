# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T05:37:17.838861+00:00`
- Price records: `522`
- Market context records: `617`
- Flow alert records: `1746`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `5.1853` n `146` status `ready` deltaP `7.5311` edge `0.3867` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `4.885` n `146` status `ready` deltaP `14.0813` edge `0.3466` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0742` n `146` status `ready` deltaP `9.2152` edge `0.0162` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3211` n `146` status `ready` deltaP `1.9855` edge `0.0034` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.63` n `146` status `ready` deltaP `1.2526` edge `0.0366` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6944` n `146` status `ready` deltaP `-0.1306` edge `-0.0028` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.0849` n `146` status `ready` deltaP `-3.5807` edge `-0.0062` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1509` n `146` status `ready` deltaP `5.8894` edge `-0.0037` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2812` n `146` status `ready` deltaP `-2.2707` edge `-0.0106` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.5642` n `146` status `ready` deltaP `5.1194` edge `0.0925` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.6826` n `146` status `ready` deltaP `5.728` edge `-0.0061` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-2.2228` n `146` status `ready` deltaP `14.6055` edge `0.088` maxDD `-22.648`
- `market_context_high->index_4h` score `-2.2995` n `146` status `ready` deltaP `-0.6686` edge `-0.0349` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.7548` n `146` status `ready` deltaP `-7.7031` edge `0.0213` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.2331` n `146` status `ready` deltaP `-3.2582` edge `-0.0325` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2818` n `146` status `ready` deltaP `-4.4032` edge `-0.0482` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6777` n `146` status `ready` deltaP `-6.1916` edge `0.0849` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2653` n `146` status `ready` deltaP `-2.5125` edge `-0.0129` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.6485` n `146` status `ready` deltaP `2.6314` edge `-0.2171` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.7401` n `146` status `ready` deltaP `-11.1504` edge `-0.0602` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
