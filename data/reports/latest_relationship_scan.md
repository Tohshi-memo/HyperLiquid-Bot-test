# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T17:07:25.333741+00:00`
- Price records: `672`
- Market context records: `2580`
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

- `market_context_high->crypto_alt_4h` score `6.2191` n `146` status `ready` deltaP `26.8731` edge `0.607` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `6.2079` n `123` status `ready` deltaP `18.7881` edge `0.4249` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.398` n `146` status `ready` deltaP `18.2697` edge `0.4257` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `1.6517` n `123` status `ready` deltaP `9.7603` edge `0.5121` maxDD `-26.4952`
- `market_context_high->crypto_alt_1h` score `1.5127` n `146` status `ready` deltaP `12.0294` edge `0.1646` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.2282` n `146` status `ready` deltaP `9.5139` edge `0.1439` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `1.0326` n `146` status `ready` deltaP `10.6595` edge `0.1344` maxDD `-4.2199`
- `market_context_high->equity_24h` score `0.7372` n `123` status `ready` deltaP `17.9031` edge `0.0091` maxDD `-2.3615`
- `market_context_high->index_24h` score `0.6782` n `123` status `ready` deltaP `7.334` edge `0.1057` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.6739` n `123` status `ready` deltaP `1.6684` edge `0.7131` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.3556` n `146` status `ready` deltaP `9.4325` edge `0.0509` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1623` n `146` status `ready` deltaP `3.642` edge `0.0116` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4284` n `146` status `ready` deltaP `1.8005` edge `0.0186` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4626` n `146` status `ready` deltaP `5.2026` edge `0.0146` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.4844` n `146` status `ready` deltaP `5.1119` edge `0.0643` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.6212` n `146` status `ready` deltaP `1.1115` edge `0.0156` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6377` n `146` status `ready` deltaP `-0.5352` edge `0.0039` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.8181` n `146` status `ready` deltaP `-0.3773` edge `0.0182` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.85` n `146` status `ready` deltaP `0.2318` edge `0.0134` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-1.0668` n `123` status `ready` deltaP `1.3296` edge `0.0016` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
