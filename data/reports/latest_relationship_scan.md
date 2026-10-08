# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T23:22:28.957131+00:00`
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

- `market_context_high->unknown_4h` score `39.7982` n `91` status `ready` deltaP `-3.749` edge `3.3954` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.076` n `49` status `ready` deltaP `43.1402` edge `0.8854` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.644` n `49` status `ready` deltaP `44.394` edge `0.8478` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.3275` n `49` status `ready` deltaP `27.192` edge `0.6893` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.0886` n `90` status `ready` deltaP `21.9122` edge `1.3165` maxDD `-16.7906`
- `market_context_high->equity_24h` score `7.6591` n `90` status `ready` deltaP `26.4664` edge `0.5047` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.6195` n `49` status `ready` deltaP `47.3137` edge `0.2362` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.8833` n `49` status `ready` deltaP `32.3855` edge `0.2949` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5563` n `49` status `ready` deltaP `45.5202` edge `0.0807` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.0042` n `49` status `ready` deltaP `11.5636` edge `0.2088` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `2.9558` n `90` status `ready` deltaP `13.6145` edge `0.882` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.5303` n `49` status `ready` deltaP `5.7406` edge `0.2043` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4146` n `49` status `ready` deltaP `29.8363` edge `0.0163` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.2534` n `49` status `ready` deltaP `29.5406` edge `-0.0007` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.6693` n `91` status `ready` deltaP `17.7064` edge `0.229` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.3299` n `90` status `ready` deltaP `22.6054` edge `0.1683` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2275` n `49` status `ready` deltaP `19.058` edge `0.0719` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5807` n `91` status `ready` deltaP `16.6008` edge `0.0124` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4643` n `91` status `ready` deltaP `9.0923` edge `0.0023` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2413` n `91` status `ready` deltaP `9.9938` edge `0.0532` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
