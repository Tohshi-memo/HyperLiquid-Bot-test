# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T03:52:25.208419+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10952`

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

- `market_context_high->commodity_4h` score `1.4373` n `163` status `ready` deltaP `16.1501` edge `0.0794` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7342` n `173` status `ready` deltaP `9.8828` edge `0.0296` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.5726` n `138` status `ready` deltaP `19.452` edge `0.0245` maxDD `-1.4613`
- `market_context_high->fx_4h` score `-0.1204` n `163` status `ready` deltaP `6.9102` edge `0.0067` maxDD `-1.1228`
- `market_context_high->fx_1h` score `-0.1677` n `173` status `ready` deltaP `4.1648` edge `-0.0006` maxDD `-0.8933`
- `market_context_high->index_24h` score `-0.6211` n `138` status `ready` deltaP `1.9474` edge `0.0884` maxDD `-5.9181`
- `market_context_high->index_4h` score `-0.7853` n `163` status `ready` deltaP `-1.9537` edge `-0.0094` maxDD `-1.26`
- `market_context_high->metal_1h` score `-0.8163` n `173` status `ready` deltaP `-4.6718` edge `-0.0099` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-0.8357` n `173` status `ready` deltaP `-2.1183` edge `-0.006` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.8714` n `173` status `ready` deltaP `-3.0459` edge `-0.0046` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-1.2447` n `138` status `ready` deltaP `-3.3137` edge `0.035` maxDD `-2.6638`
- `market_context_high->equity_24h` score `-1.4479` n `138` status `ready` deltaP `-1.6606` edge `0.1964` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.5285` n `173` status `ready` deltaP `-8.6307` edge `-0.0363` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-2.0117` n `163` status `ready` deltaP `-7.7538` edge `-0.0352` maxDD `-6.0144`
- `market_context_high->equity_4h` score `-2.6904` n `163` status `ready` deltaP `-7.9138` edge `-0.1001` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.5537` n `173` status `ready` deltaP `-9.8785` edge `-0.0569` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.9928` n `163` status `ready` deltaP `-12.067` edge `-0.1557` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.3595` n `138` status `ready` deltaP `-11.2772` edge `-0.1438` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.8044` n `138` status `ready` deltaP `-2.1966` edge `-0.1363` maxDD `-14.2873`
- `market_context_high->unknown_1h` score `-7.5307` n `173` status `ready` deltaP `-4.7636` edge `-0.5501` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
