# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T13:37:28.061455+00:00`
- Price records: `672`
- Market context records: `2566`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->crypto_alt_4h` score `5.8065` n `146` status `ready` deltaP `25.1963` edge `0.5838` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `5.4067` n `115` status `ready` deltaP `13.8285` edge `0.6237` maxDD `-15.2264`
- `market_context_high->unknown_24h` score `5.0127` n `115` status `ready` deltaP `20.3019` edge `0.3152` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.9682` n `146` status `ready` deltaP `17.2026` edge `0.397` maxDD `-10.1468`
- `market_context_high->equity_24h` score `1.7714` n `115` status `ready` deltaP `21.3406` edge `0.0637` maxDD `-2.0014`
- `market_context_high->unknown_4h` score `1.5542` n `146` status `ready` deltaP `10.1236` edge `0.167` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.4792` n `146` status `ready` deltaP `11.5803` edge `0.1648` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.8683` n `146` status `ready` deltaP `9.6116` edge `0.1277` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6446` n `115` status `ready` deltaP `5.8635` edge `0.1127` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.2711` n `115` status `ready` deltaP `-0.9616` edge `0.679` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.1119` n `146` status `ready` deltaP `7.4508` edge `0.0438` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1443` n `146` status `ready` deltaP `3.7917` edge `0.0121` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.4098` n `146` status `ready` deltaP `5.3523` edge `0.018` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4116` n `146` status `ready` deltaP `1.8005` edge `0.02` maxDD `-2.6375`
- `market_context_high->fx_24h` score `-0.5626` n `115` status `ready` deltaP `1.9958` edge `0.0056` maxDD `-1.6157`
- `market_context_high->fx_1h` score `-0.5874` n `146` status `ready` deltaP `0.0636` edge `0.0041` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.6332` n `146` status `ready` deltaP `1.2612` edge `0.0136` maxDD `-2.9823`
- `market_context_high->equity_1h` score `-0.7162` n `146` status `ready` deltaP `0.2215` edge `0.0227` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8316` n `146` status `ready` deltaP `0.5367` edge `0.0129` maxDD `-0.8621`
- `market_context_high->metal_4h` score `-0.9311` n `146` status `ready` deltaP `2.9777` edge `0.0413` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
