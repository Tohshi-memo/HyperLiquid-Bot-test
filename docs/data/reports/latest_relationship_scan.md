# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T23:22:27.350790+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10650`

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

- `risk_on_high->unknown_4h` score `19.9423` n `133` status `ready` deltaP `8.9985` edge `1.6637` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.9423` n `133` status `ready` deltaP `8.9985` edge `1.6637` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.4448` n `217` status `ready` deltaP `9.4351` edge `0.7937` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `4.6712` n `46` status `ready` deltaP `21.7542` edge `0.2712` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.3569` n `46` status `ready` deltaP `10.3394` edge `0.1758` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `1.9661` n `46` status `ready` deltaP `11.3451` edge `0.1054` maxDD `-0.042`
- `news_risk_high->metal_4h` score `1.6827` n `46` status `ready` deltaP `17.7757` edge `0.048` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6219` n `46` status `ready` deltaP `15.6795` edge `0.0697` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.4851` n `46` status `ready` deltaP `10.2664` edge `0.0754` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.1337` n `46` status `ready` deltaP `14.547` edge `0.0109` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.7783` n `46` status `ready` deltaP `9.9714` edge `0.0177` maxDD `-0.2118`
- `news_risk_high->crypto_alt_1h` score `0.2934` n `46` status `ready` deltaP `4.6538` edge `0.0237` maxDD `-1.0885`
- `news_risk_high->fx_4h` score `0.2665` n `46` status `ready` deltaP `10.1007` edge `0.0001` maxDD `-0.9514`
- `news_risk_high->commodity_1h` score `0.2364` n `46` status `ready` deltaP `9.0797` edge `0.0038` maxDD `-0.9036`
- `news_risk_high->crypto_major_1h` score `0.1442` n `46` status `ready` deltaP `0.5272` edge `0.0442` maxDD `-1.0047`
- `risk_on_high->metal_1h` score `0.1303` n `133` status `ready` deltaP `13.0116` edge `0.0012` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1303` n `133` status `ready` deltaP `13.0116` edge `0.0012` maxDD `-1.699`
- `risk_on_high->index_1h` score `-0.2299` n `133` status `ready` deltaP `2.7948` edge `-0.0036` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.2299` n `133` status `ready` deltaP `2.7948` edge `-0.0036` maxDD `-0.5605`
- `news_risk_high->crypto_major_24h` score `-0.27` n `46` status `ready` deltaP `15.4816` edge `0.1398` maxDD `-18.2098`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
