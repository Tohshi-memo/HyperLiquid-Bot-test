# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T22:37:32.469224+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8896`

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

- `market_context_high->unknown_4h` score `39.8382` n `91` status `ready` deltaP `-3.4441` edge `3.3967` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.1602` n `49` status `ready` deltaP `43.2927` edge `0.8914` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.7224` n `49` status `ready` deltaP `44.6989` edge `0.8523` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.0723` n `49` status `ready` deltaP `26.6721` edge `0.6715` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.0012` n `90` status `ready` deltaP `21.9122` edge `1.3053` maxDD `-16.7906`
- `market_context_high->equity_24h` score `7.4039` n `90` status `ready` deltaP `25.9465` edge `0.4869` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.5371` n `49` status `ready` deltaP `46.7938` edge `0.2328` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.9025` n `49` status `ready` deltaP `32.3855` edge `0.2965` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5587` n `49` status `ready` deltaP `45.5202` edge `0.0809` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.0666` n `49` status `ready` deltaP `12.0127` edge `0.211` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `2.9168` n `90` status `ready` deltaP `13.6145` edge `0.877` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.6071` n `49` status `ready` deltaP `6.1897` edge `0.2077` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4397` n `49` status `ready` deltaP `30.1357` edge `0.0164` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.2822` n `49` status `ready` deltaP `29.5406` edge `0.0017` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.7202` n `91` status `ready` deltaP `18.0113` edge `0.2335` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.3679` n `90` status `ready` deltaP `23.1253` edge `0.1697` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2568` n `49` status `ready` deltaP `19.5153` edge `0.0726` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5795` n `91` status `ready` deltaP `16.6008` edge `0.0123` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4512` n `91` status `ready` deltaP `8.9426` edge `0.0022` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2818` n `91` status `ready` deltaP `10.4429` edge `0.0554` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
