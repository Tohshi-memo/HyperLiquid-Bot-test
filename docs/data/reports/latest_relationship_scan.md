# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T05:52:25.627176+00:00`
- Price records: `672`
- Market context records: `6575`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9904`

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

- `market_context_high->unknown_24h` score `6.2078` n `144` status `ready` deltaP `11.032` edge `0.7738` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.7484` n `210` status `ready` deltaP `-5.4291` edge `0.272` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.4193` n `144` status `ready` deltaP `13.3492` edge `0.2161` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.337` n `210` status `ready` deltaP `1.1577` edge `-0.0002` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.376` n `210` status `ready` deltaP `7.3467` edge `0.0294` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.4869` n `210` status `ready` deltaP `6.3402` edge `0.0266` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5724` n `210` status `ready` deltaP `-0.6801` edge `0.0031` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.6149` n `210` status `ready` deltaP `-0.8583` edge `-0.0048` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9849` n `210` status `ready` deltaP `8.0851` edge `0.0078` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.228` n `210` status `ready` deltaP `1.6325` edge `-0.0022` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2871` n `210` status `ready` deltaP `-3.7268` edge `-0.0017` maxDD `-2.1239`
- `market_context_high->commodity_4h` score `-1.351` n `210` status `ready` deltaP `-1.8642` edge `-0.0113` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.5513` n `210` status `ready` deltaP `-15.8561` edge `0.217` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.7152` n `210` status `ready` deltaP `7.8825` edge `0.059` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.7633` n `210` status `ready` deltaP `-0.2331` edge `-0.0033` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.9068` n `210` status `ready` deltaP `5.2381` edge `0.0608` maxDD `-19.2145`
- `market_context_high->metal_24h` score `-1.9345` n `144` status `ready` deltaP `6.0917` edge `0.0912` maxDD `-5.7746`
- `market_context_high->metal_4h` score `-2.1429` n `210` status `ready` deltaP `-1.3779` edge `0.0205` maxDD `-5.2172`
- `market_context_high->index_24h` score `-3.7041` n `144` status `ready` deltaP `1.4429` edge `0.0038` maxDD `-10.7676`
- `market_context_high->fx_24h` score `-3.8289` n `144` status `ready` deltaP `-4.8143` edge `-0.0053` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
