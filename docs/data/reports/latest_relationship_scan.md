# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T18:22:31.184333+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9046`

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

- `news_risk_high->unknown_4h` score `420.9207` n `77` status `ready` deltaP `-20.8821` edge `35.3054` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.34` n `52` status `ready` deltaP `50.0` edge `0.445` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.34` n `52` status `ready` deltaP `50.0` edge `0.445` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.6449` n `73` status `ready` deltaP `28.7577` edge `0.6666` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `8.0409` n `149` status `ready` deltaP `43.2886` edge `0.434` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.7039` n `73` status `ready` deltaP `28.2154` edge `0.6313` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.4287` n `73` status `ready` deltaP `36.494` edge `0.2267` maxDD `-0.075`
- `news_risk_high->crypto_major_24h` score `5.4111` n `73` status `ready` deltaP `19.9985` edge `0.7599` maxDD `-13.2931`
- `news_risk_high->metal_24h` score `3.592` n `73` status `ready` deltaP `26.9621` edge `0.165` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9383` n `52` status `ready` deltaP `32.5399` edge `0.0629` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9383` n `52` status `ready` deltaP `32.5399` edge `0.0629` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.838` n `149` status `ready` deltaP `29.0422` edge `0.0847` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.9933` n `52` status `ready` deltaP `27.5908` edge `-0.0136` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.9933` n `52` status `ready` deltaP `27.5908` edge `-0.0136` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.8584` n `149` status `ready` deltaP `24.8159` edge `0.011` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1517` n `149` status `ready` deltaP `16.3606` edge `0.0246` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.9955` n `77` status `ready` deltaP `15.5627` edge `0.0258` maxDD `-0.3938`
- `risk_on_high->commodity_1h` score `0.5284` n `52` status `ready` deltaP `9.4427` edge `0.0163` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5284` n `52` status `ready` deltaP `9.4427` edge `0.0163` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2127` n `149` status `ready` deltaP `10.4957` edge `0.0049` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
