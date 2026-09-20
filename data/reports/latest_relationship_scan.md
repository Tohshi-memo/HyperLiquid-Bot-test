# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T16:18:02.234783+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9242`

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

- `news_risk_high->crypto_major_24h` score `22.8688` n `98` status `ready` deltaP `9.1447` edge `2.5306` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3072` n `98` status `ready` deltaP `14.9199` edge `2.0809` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `14.2977` n `49` status `ready` deltaP `0.28` edge `1.2046` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.9357` n `101` status `ready` deltaP `23.1873` edge `0.461` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.4972` n `101` status `ready` deltaP `21.9678` edge `0.3541` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.3952` n `49` status `ready` deltaP `36.688` edge `0.135` maxDD `-0.0659`
- `market_context_high->commodity_24h` score `3.8406` n `38` status `ready` deltaP `22.9898` edge `0.2193` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `3.0197` n `101` status `ready` deltaP `16.6805` edge `0.187` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.3096` n `49` status `ready` deltaP `29.9216` edge `0.0145` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2355` n `101` status `ready` deltaP `18.4769` edge `0.1154` maxDD `-2.8494`
- `market_context_high->fx_24h` score `1.9228` n `38` status `ready` deltaP `20.2851` edge `0.0292` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.599` n `50` status `ready` deltaP `17.9042` edge `0.0414` maxDD `-0.2012`
- `market_context_high->fx_1h` score `1.2489` n `50` status `ready` deltaP `17.0599` edge `0.0078` maxDD `-0.063`
- `news_risk_high->commodity_24h` score `1.0721` n `98` status `ready` deltaP `22.775` edge `0.1162` maxDD `-3.4467`
- `news_risk_high->metal_4h` score `0.7152` n `101` status `ready` deltaP `18.1659` edge `0.0439` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6425` n `101` status `ready` deltaP `14.7477` edge `0.0154` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.6005` n `98` status `ready` deltaP `16.571` edge `0.0805` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.2626` n `50` status `ready` deltaP `7.4012` edge `0.0067` maxDD `-0.4568`
- `news_risk_high->equity_1h` score `0.2245` n `101` status `ready` deltaP `5.2143` edge `0.0245` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.2156` n `98` status `ready` deltaP `15.5046` edge `0.0087` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
