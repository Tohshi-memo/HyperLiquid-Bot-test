# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T11:22:22.388333+00:00`
- Price records: `672`
- Market context records: `2556`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9238`

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

- `market_context_high->crypto_alt_4h` score `5.7101` n `149` status `ready` deltaP `24.8609` edge `0.578` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.2988` n `118` status `ready` deltaP `19.3032` edge `0.3457` maxDD `-1.626`
- `market_context_high->crypto_major_24h` score `4.8949` n `118` status `ready` deltaP `12.1704` edge `0.5921` maxDD `-15.2264`
- `market_context_high->crypto_major_4h` score `3.9823` n `149` status `ready` deltaP `17.7535` edge `0.3945` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.7561` n `149` status `ready` deltaP `10.1571` edge `0.1836` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1977` n `149` status `ready` deltaP `9.7265` edge `0.1537` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.1964` n `118` status `ready` deltaP `18.9972` edge `0.0314` maxDD `-2.0014`
- `market_context_high->index_24h` score `0.7334` n `118` status `ready` deltaP `6.9592` edge `0.1128` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.6814` n `149` status `ready` deltaP `8.2345` edge `0.1213` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.1612` n `118` status `ready` deltaP `-0.9592` edge `0.6675` maxDD `-39.2351`
- `market_context_high->index_4h` score `0.0028` n `149` status `ready` deltaP `6.8372` edge `0.0388` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1909` n `149` status `ready` deltaP `3.4492` edge `0.0105` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2605` n `149` status `ready` deltaP `2.566` edge `0.0302` maxDD `-2.8543`
- `market_context_high->metal_1h` score `-0.4581` n `149` status `ready` deltaP `1.0117` edge `0.0093` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.5417` n `149` status `ready` deltaP `0.635` edge `0.0041` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.5434` n `149` status `ready` deltaP `4.2077` edge `0.0145` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.7448` n `118` status `ready` deltaP `1.2565` edge `0.0038` maxDD `-1.946`
- `market_context_high->equity_1h` score `-0.8045` n `149` status `ready` deltaP `-0.2984` edge `0.0188` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.8588` n `149` status `ready` deltaP `3.6872` edge `0.0426` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-0.8817` n `149` status `ready` deltaP `-0.0011` edge `0.0125` maxDD `-0.8774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
