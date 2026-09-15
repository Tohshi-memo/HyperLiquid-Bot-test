# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T09:22:26.343308+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11176`

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

- `news_risk_high->unknown_4h` score `397.4446` n `78` status `ready` deltaP `-22.303` edge `33.3584` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.7973` n `78` status `ready` deltaP `45.3392` edge `1.5533` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `21.6363` n `78` status `ready` deltaP `18.2292` edge `1.6815` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `16.4899` n `78` status `ready` deltaP `35.0428` edge `1.2876` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.0754` n `78` status `ready` deltaP `48.4642` edge `1.1112` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7149` n `78` status `ready` deltaP `62.2863` edge `0.3286` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.5734` n `78` status `ready` deltaP `38.8354` edge `0.3343` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9968` n `52` status `ready` deltaP `38.1944` edge `0.2451` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9968` n `52` status `ready` deltaP `38.1944` edge `0.2451` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6998` n `137` status `ready` deltaP `30.8951` edge `0.2382` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.7841` n `52` status `ready` deltaP `43.7366` edge `0.028` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.7841` n `52` status `ready` deltaP `43.7366` edge `0.028` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.3871` n `137` status `ready` deltaP `40.5502` edge `0.0335` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9337` n `52` status `ready` deltaP `24.9179` edge `0.03` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9337` n `52` status `ready` deltaP `24.9179` edge `0.03` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8335` n `149` status `ready` deltaP `21.4202` edge `0.0518` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8282` n `149` status `ready` deltaP `13.3666` edge `0.0176` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7122` n `78` status `ready` deltaP `17.421` edge `0.038` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2494` n `52` status `ready` deltaP `8.2105` edge `0.0078` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2494` n `52` status `ready` deltaP `8.2105` edge `0.0078` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
