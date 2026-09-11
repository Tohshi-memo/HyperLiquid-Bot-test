# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T09:07:30.805492+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12372`

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

- `news_risk_high->unknown_1h` score `750.8501` n `59` status `ready` deltaP `-6.5082` edge `62.6564` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `22.0106` n `91` status `ready` deltaP `39.6444` edge `1.5929` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `22.0106` n `91` status `ready` deltaP `39.6444` edge `1.5929` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `19.2601` n `171` status `ready` deltaP `35.7822` edge `1.4492` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.1333` n `171` status `ready` deltaP `34.2014` edge `0.5331` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.8801` n `91` status `ready` deltaP `41.3361` edge `0.5016` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.8801` n `91` status `ready` deltaP `41.3361` edge `0.5016` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `8.7457` n `91` status `ready` deltaP `34.2014` edge `0.5008` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.7457` n `91` status `ready` deltaP `34.2014` edge `0.5008` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.5041` n `91` status `ready` deltaP `31.5918` edge `0.5006` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.5041` n `91` status `ready` deltaP `31.5918` edge `0.5006` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.3212` n `91` status `ready` deltaP `25.021` edge `1.1786` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.3212` n `91` status `ready` deltaP `25.021` edge `1.1786` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.4014` n `91` status `ready` deltaP `50.0019` edge `0.121` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.4014` n `91` status `ready` deltaP `50.0019` edge `0.121` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.3187` n `171` status `ready` deltaP `42.7723` edge `0.1141` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.542` n `91` status `ready` deltaP `34.1078` edge `0.0771` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.542` n `91` status `ready` deltaP `34.1078` edge `0.0771` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.4456` n `171` status `ready` deltaP `27.8357` edge `0.1009` maxDD `-2.6138`
- `risk_on_high->equity_1h` score `1.6082` n `91` status `ready` deltaP `21.1835` edge `0.0206` maxDD `-0.2246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
