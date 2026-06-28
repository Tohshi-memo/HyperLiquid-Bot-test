# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T19:07:26.638340+00:00`
- Price records: `672`
- Market context records: `5070`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10324`

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

- `market_context_high->unknown_1h` score `11.938` n `101` status `ready` deltaP `4.6392` edge `1.014` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.218` n `97` status `ready` deltaP `21.178` edge `0.7292` maxDD `-5.5109`
- `market_context_high->unknown_24h` score `7.5095` n `80` status `ready` deltaP `27.8472` edge `0.4744` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `6.1896` n `97` status `ready` deltaP `18.4546` edge `0.5147` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.5442` n `97` status `ready` deltaP `17.0025` edge `0.5071` maxDD `-8.3416`
- `market_context_high->metal_4h` score `0.9666` n `97` status `ready` deltaP `10.4319` edge `0.1189` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.9465` n `101` status `ready` deltaP `7.1737` edge `0.1159` maxDD `-4.121`
- `market_context_high->equity_1h` score `0.7601` n `101` status `ready` deltaP `7.6332` edge `0.0698` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.6965` n `97` status `ready` deltaP `6.0112` edge `0.1707` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.5495` n `101` status `ready` deltaP `8.7967` edge `0.0368` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.3434` n `101` status `ready` deltaP `6.0102` edge `0.0963` maxDD `-4.7207`
- `market_context_high->index_4h` score `0.0174` n `97` status `ready` deltaP `5.8147` edge `0.0388` maxDD `-1.0893`
- `market_context_high->index_1h` score `-0.2635` n `101` status `ready` deltaP `2.2336` edge `0.0124` maxDD `-0.552`
- `market_context_high->fx_24h` score `-0.295` n `80` status `ready` deltaP `4.8264` edge `0.0062` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.5389` n `101` status `ready` deltaP `1.0598` edge `0.014` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.8601` n `97` status `ready` deltaP `7.1426` edge `0.0056` maxDD `-4.9914`
- `market_context_high->fx_4h` score `-0.944` n `97` status `ready` deltaP `-3.2232` edge `-0.0006` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.5292` n `101` status `ready` deltaP `-9.2903` edge `-0.0045` maxDD `-0.5464`
- `market_context_high->commodity_24h` score `-3.5966` n `80` status `ready` deltaP `5.0694` edge `-0.0408` maxDD `-24.3277`
- `market_context_high->metal_24h` score `-3.6741` n `80` status `ready` deltaP `2.3611` edge `0.0587` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
