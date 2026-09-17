# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T20:37:29.678602+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9004`

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

- `news_risk_high->unknown_4h` score `444.1872` n `74` status `ready` deltaP `-13.806` edge `37.1846` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.28` n `52` status `ready` deltaP `50.0` edge `0.44` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.28` n `52` status `ready` deltaP `50.0` edge `0.44` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.3503` n `64` status `ready` deltaP `28.6458` edge `0.6428` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.9809` n `149` status `ready` deltaP `43.2886` edge `0.429` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.8574` n `64` status `ready` deltaP `23.7847` edge `0.5903` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.0263` n `64` status `ready` deltaP `34.375` edge `0.2073` maxDD `-0.075`
- `news_risk_high->crypto_major_24h` score `4.5454` n `64` status `ready` deltaP `16.1458` edge `0.6746` maxDD `-13.2931`
- `news_risk_high->metal_24h` score `3.1267` n `64` status `ready` deltaP `22.9167` edge `0.1532` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `3.0571` n `52` status `ready` deltaP `33.4545` edge `0.0667` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0571` n `52` status `ready` deltaP `33.4545` edge `0.0667` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9568` n `149` status `ready` deltaP `29.9568` edge `0.0885` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.8787` n `52` status `ready` deltaP `26.5491` edge `-0.0162` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8787` n `52` status `ready` deltaP `26.5491` edge `-0.0162` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.7438` n `149` status `ready` deltaP `23.7742` edge `0.0084` maxDD `-0.0593`
- `news_risk_high->index_4h` score `1.6605` n `74` status `ready` deltaP `23.1543` edge `0.0306` maxDD `-0.3938`
- `market_context_high->commodity_1h` score `1.2356` n `149` status `ready` deltaP `17.1091` edge `0.0266` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6123` n `52` status `ready` deltaP `10.1912` edge `0.0183` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6123` n `52` status `ready` deltaP `10.1912` edge `0.0183` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2143` n `149` status `ready` deltaP `10.4957` edge `0.0051` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
