# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T06:22:26.835494+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11164`

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

- `news_risk_high->unknown_4h` score `399.749` n `78` status `ready` deltaP `-21.9981` edge `33.5484` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `22.5622` n `78` status `ready` deltaP `18.4028` edge `1.7575` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.1431` n `78` status `ready` deltaP `43.7767` edge `1.5092` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.7233` n `78` status `ready` deltaP `32.9594` edge `1.2376` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.571` n `78` status `ready` deltaP `46.5545` edge `1.0819` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5623` n `78` status `ready` deltaP `60.7238` edge `0.3263` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4157` n `78` status `ready` deltaP `37.7938` edge `0.3281` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.1583` n `52` status `ready` deltaP `39.5833` edge `0.2493` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1583` n `52` status `ready` deltaP `39.5833` edge `0.2493` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.8613` n `137` status `ready` deltaP `32.284` edge `0.2424` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.0288` n `52` status `ready` deltaP `45.82` edge `0.0345` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.0288` n `52` status `ready` deltaP `45.82` edge `0.0345` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.6318` n `137` status `ready` deltaP `42.6336` edge `0.04` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9737` n `52` status `ready` deltaP `25.2228` edge `0.0313` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9737` n `52` status `ready` deltaP `25.2228` edge `0.0313` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8735` n `149` status `ready` deltaP `21.7251` edge `0.0531` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8234` n `149` status `ready` deltaP `13.3666` edge `0.0172` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.63` n `78` status `ready` deltaP `16.2015` edge `0.0356` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2222` n `52` status `ready` deltaP `7.7614` edge `0.0073` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2222` n `52` status `ready` deltaP `7.7614` edge `0.0073` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
