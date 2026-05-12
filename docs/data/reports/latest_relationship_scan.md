# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-12T01:52:17.715017+00:00`
- Price records: `672`
- Market context records: `987`
- Flow alert records: `3196`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `13.1082` n `210` status `ready` deltaP `31.2513` edge `0.9174` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.4798` n `210` status `ready` deltaP `10.6129` edge `0.3859` maxDD `0.0`
- `market_context_high->fx_1h` score `-0.3732` n `211` status `ready` deltaP `1.6231` edge `-0.0006` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.418` n `211` status `ready` deltaP `3.2921` edge `0.024` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.7046` n `211` status `ready` deltaP `0.9528` edge `0.0118` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.7235` n `210` status `ready` deltaP `2.7482` edge `0.1209` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.7276` n `210` status `ready` deltaP `0.8499` edge `0.0007` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.8048` n `211` status `ready` deltaP `2.4431` edge `0.002` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.207` n `211` status `ready` deltaP `-1.2325` edge `-0.0152` maxDD `-3.5069`
- `market_context_high->crypto_major_1h` score `-1.2505` n `211` status `ready` deltaP `4.738` edge `-0.0196` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.2583` n `210` status `ready` deltaP `4.2323` edge `0.1274` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-1.5711` n `210` status `ready` deltaP `1.4521` edge `0.0746` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7985` n `210` status `ready` deltaP `-2.0862` edge `0.0163` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.9848` n `211` status `ready` deltaP `-1.6556` edge `-0.0475` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.2181` n `211` status `ready` deltaP `-0.7762` edge `-0.0357` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.9495` n `210` status `ready` deltaP `7.1407` edge `0.0772` maxDD `-22.648`
- `market_context_high->unknown_4h` score `-3.2096` n `210` status `ready` deltaP `7.6276` edge `-0.1305` maxDD `-8.3588`
- `market_context_high->commodity_4h` score `-3.2852` n `210` status `ready` deltaP `-2.1909` edge `0.0576` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.4742` n `210` status `ready` deltaP `-2.3254` edge `0.0038` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.5718` n `210` status `ready` deltaP `-1.215` edge `-0.0219` maxDD `-20.2343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
