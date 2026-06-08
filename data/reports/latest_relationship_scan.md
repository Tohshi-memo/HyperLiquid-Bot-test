# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T23:52:28.073136+00:00`
- Price records: `672`
- Market context records: `3328`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_24h` score `62.621` n `31` status `ready` deltaP `67.1875` edge `4.7705` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `62.621` n `31` status `ready` deltaP `67.1875` edge `4.7705` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `57.7275` n `31` status `ready` deltaP `61.4583` edge `4.4009` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `57.7275` n `31` status `ready` deltaP `61.4583` edge `4.4009` maxDD `0.0`
- `risk_on_high->equity_24h` score `46.7937` n `31` status `ready` deltaP `56.7708` edge `3.521` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.7937` n `31` status `ready` deltaP `56.7708` edge `3.521` maxDD `0.0`
- `risk_on_high->index_24h` score `22.9508` n `31` status `ready` deltaP `50.6944` edge `1.5746` maxDD `0.0`
- `risk_on_and_context->index_24h` score `22.9508` n `31` status `ready` deltaP `50.6944` edge `1.5746` maxDD `0.0`
- `risk_on_high->metal_24h` score `15.9675` n `31` status `ready` deltaP `34.9294` edge `1.1239` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.9675` n `31` status `ready` deltaP `34.9294` edge `1.1239` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.8423` n `32` status `ready` deltaP `30.1829` edge `1.2312` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8423` n `32` status `ready` deltaP `30.1829` edge `1.2312` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `15.0795` n `143` status `ready` deltaP `22.9968` edge `2.7641` maxDD `-70.3986`
- `market_context_high->index_24h` score `11.4227` n `143` status `ready` deltaP `34.6105` edge `0.9766` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.1065` n `143` status `ready` deltaP `28.0995` edge `1.95` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.3125` n `32` status `ready` deltaP `9.375` edge `0.7313` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3125` n `32` status `ready` deltaP `9.375` edge `0.7313` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.4872` n `32` status `ready` deltaP `13.3384` edge `0.4716` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.4872` n `32` status `ready` deltaP `13.3384` edge `0.4716` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `3.33` n `143` status `ready` deltaP `24.5302` edge `2.3333` maxDD `-152.2601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
