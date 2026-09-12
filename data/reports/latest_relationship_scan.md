# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T03:53:09.108987+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11337`

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

- `market_context_high->unknown_24h` score `671.0795` n `140` status `ready` deltaP `14.0228` edge `55.835` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.1829` n `82` status `ready` deltaP `-3.4541` edge `31.9971` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.6986` n `88` status `ready` deltaP `42.9293` edge `1.795` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.6986` n `88` status `ready` deltaP `42.9293` edge `1.795` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `23.6964` n `56` status `ready` deltaP `54.1418` edge `1.7038` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `20.565` n `140` status `ready` deltaP `37.1825` edge `1.5486` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `16.9791` n `56` status `ready` deltaP `28.9682` edge `1.2706` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `11.9288` n `56` status `ready` deltaP `33.4078` edge `0.7812` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.1323` n `88` status `ready` deltaP `36.9792` edge `0.5145` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1323` n `88` status `ready` deltaP `36.9792` edge `0.5145` maxDD `0.0`
- `market_context_high->equity_24h` score `8.8155` n `140` status `ready` deltaP `36.9792` edge `0.4881` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.7106` n `88` status `ready` deltaP `43.7777` edge `0.4712` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.7106` n `88` status `ready` deltaP `43.7777` edge `0.4712` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.1885` n `56` status `ready` deltaP `51.0417` edge `0.3421` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9428` n `56` status `ready` deltaP `51.2897` edge `0.3293` maxDD `-0.0797`
- `risk_on_high->crypto_major_24h` score `7.3966` n `88` status `ready` deltaP `23.7847` edge `1.1965` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.3966` n `88` status `ready` deltaP `23.7847` edge `1.1965` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `6.6984` n `88` status `ready` deltaP `31.3748` edge `0.4349` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.6984` n `88` status `ready` deltaP `31.3748` edge `0.4349` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.2462` n `88` status `ready` deltaP `51.452` edge `0.0984` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
