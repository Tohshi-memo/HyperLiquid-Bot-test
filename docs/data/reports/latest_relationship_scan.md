# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T00:52:30.963527+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8098`

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

- `news_risk_high->crypto_major_24h` score `62.6578` n `42` status `ready` deltaP `33.0109` edge `5.0906` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `57.4021` n `42` status `ready` deltaP `34.623` edge `4.6906` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.4171` n `149` status `ready` deltaP `-1.3781` edge `3.1506` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `15.2322` n `42` status `ready` deltaP `51.5625` edge `0.9256` maxDD `0.0`
- `risk_on_high->unknown_4h` score `11.2957` n `52` status `ready` deltaP `-8.6187` edge `1.0213` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.2957` n `52` status `ready` deltaP `-8.6187` edge `1.0213` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.8984` n `72` status `ready` deltaP `28.3706` edge `0.665` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.4744` n `52` status `ready` deltaP `46.875` edge `0.3937` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.4744` n `52` status `ready` deltaP `46.875` edge `0.3937` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.1753` n `149` status `ready` deltaP `40.1636` edge `0.3827` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.1321` n `72` status `ready` deltaP `25.254` edge `0.4601` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.8733` n `42` status `ready` deltaP `35.1438` edge `0.1876` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.1732` n `72` status `ready` deltaP `17.4734` edge `0.1945` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.8714` n `72` status `ready` deltaP `21.9395` edge `0.1453` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.7141` n `52` status `ready` deltaP `31.7777` edge `0.0493` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7141` n `52` status `ready` deltaP `31.7777` edge `0.0493` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6138` n `149` status `ready` deltaP `28.28` edge `0.0711` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.8481` n `42` status `ready` deltaP `9.0773` edge `0.0977` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5403` n `72` status `ready` deltaP `12.3984` edge `0.1357` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.4739` n `72` status `ready` deltaP `16.0061` edge `0.038` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
