# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T06:06:29.066314+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10712`

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

- `market_context_high->commodity_4h` score `1.2822` n `168` status `ready` deltaP `14.7067` edge `0.0761` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.004` n `136` status `ready` deltaP `20.4044` edge `0.0284` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.8566` n `169` status `ready` deltaP `11.2178` edge `0.0309` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.144` n `168` status `ready` deltaP `9.1609` edge `0.0109` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.0899` n `169` status `ready` deltaP `4.8657` edge `0.0012` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6165` n `136` status `ready` deltaP `1.7054` edge `0.0904` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7823` n `169` status `ready` deltaP `-2.2774` edge `-0.0023` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8381` n `169` status `ready` deltaP `-5.1075` edge `-0.0098` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.071` n `168` status `ready` deltaP `-0.4646` edge `-0.0079` maxDD `-1.26`
- `market_context_high->equity_1h` score `-1.2052` n `169` status `ready` deltaP `-1.6068` edge `-0.0027` maxDD `-4.6286`
- `market_context_high->metal_24h` score `-1.2083` n `136` status `ready` deltaP `-2.3897` edge `0.0434` maxDD `-2.9193`
- `market_context_high->crypto_alt_1h` score `-1.5045` n `169` status `ready` deltaP `-8.23` edge `-0.0359` maxDD `-5.5029`
- `market_context_high->equity_24h` score `-1.6626` n `136` status `ready` deltaP `-1.9097` edge `0.1885` maxDD `-21.1456`
- `market_context_high->metal_4h` score `-1.9051` n `168` status `ready` deltaP `-5.6475` edge `-0.0302` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.0399` n `168` status `ready` deltaP `-10.032` edge `-0.1103` maxDD `-8.0039`
- `market_context_high->crypto_major_1h` score `-3.5144` n `169` status `ready` deltaP `-9.4922` edge `-0.0562` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.8292` n `168` status `ready` deltaP `-10.7796` edge `-0.1433` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.3906` n `136` status `ready` deltaP `-11.8771` edge `-0.1424` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.8172` n `136` status `ready` deltaP `-2.4918` edge `-0.1354` maxDD `-14.2873`
- `market_context_high->unknown_1h` score `-7.5299` n `169` status `ready` deltaP `-4.5876` edge `-0.5512` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
