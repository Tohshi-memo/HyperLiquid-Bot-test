# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T00:37:25.730136+00:00`
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

- `market_context_high->unknown_4h` score `39.8236` n `91` status `ready` deltaP `-3.5965` edge `3.3965` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.082` n `49` status `ready` deltaP `43.1402` edge `0.8859` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.6318` n `49` status `ready` deltaP `44.2416` edge `0.8478` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.7676` n `49` status `ready` deltaP `28.0585` edge `0.7202` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.2812` n `90` status `ready` deltaP `21.9122` edge `1.3412` maxDD `-16.7906`
- `market_context_high->equity_24h` score `8.0992` n `90` status `ready` deltaP `27.3329` edge `0.5356` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.7548` n `49` status `ready` deltaP `48.1802` edge `0.2417` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.8579` n `49` status `ready` deltaP `32.233` edge `0.2938` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5417` n `49` status `ready` deltaP `45.3677` edge `0.0805` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.097` n `90` status `ready` deltaP `13.6145` edge `0.9001` maxDD `-34.5048`
- `news_risk_high->crypto_major_1h` score `3.0546` n `49` status `ready` deltaP `11.863` edge `0.211` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `2.5603` n `49` status `ready` deltaP `5.8903` edge `0.2058` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4266` n `49` status `ready` deltaP `29.986` edge `0.0163` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.1657` n `49` status `ready` deltaP `29.194` edge `-0.0057` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.6613` n `91` status `ready` deltaP `17.554` edge `0.229` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.2599` n `90` status `ready` deltaP `21.7388` edge `0.1651` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1676` n `49` status `ready` deltaP `18.2958` edge `0.0693` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5417` n `91` status `ready` deltaP `16.1435` edge `0.0122` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.414` n `91` status `ready` deltaP `8.4935` edge `0.0021` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.274` n `91` status `ready` deltaP `10.2932` edge `0.0554` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
