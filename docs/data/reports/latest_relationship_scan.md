# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T04:37:39.074954+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `57.7571` n `50` status `ready` deltaP `20.6239` edge `4.6756` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.0739` n `50` status `ready` deltaP `46.6066` edge `2.5729` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `10.0389` n `50` status `ready` deltaP `28.0208` edge `0.6991` maxDD `-2.6128`
- `news_risk_high->unknown_4h` score `7.3895` n `76` status `ready` deltaP `13.5511` edge `0.5648` maxDD `-1.4812`
- `news_risk_high->equity_24h` score `7.3183` n `50` status `ready` deltaP `30.1005` edge `0.502` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `7.0658` n `120` status `ready` deltaP `13.9572` edge `0.569` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.5342` n `50` status `ready` deltaP `43.4073` edge `0.0927` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.3514` n `120` status `ready` deltaP `28.7406` edge `0.1896` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4946` n `50` status `ready` deltaP `26.9948` edge `0.043` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.4316` n `120` status `ready` deltaP `18.7704` edge `0.1182` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.3968` n `80` status `ready` deltaP `5.2246` edge `0.2006` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `2.3001` n `76` status `ready` deltaP `33.6329` edge `0.0224` maxDD `-0.3953`
- `market_context_high->unknown_1h` score `0.9707` n `120` status `ready` deltaP `9.3913` edge `0.0633` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6393` n `80` status `ready` deltaP `12.994` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4556` n `80` status `ready` deltaP `12.7994` edge `0.0051` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.109` n `120` status `ready` deltaP `10.1016` edge `0.0104` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.332` n `120` status `ready` deltaP `4.6607` edge `-0.0004` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.3731` n `80` status `ready` deltaP `0.6063` edge `-0.0082` maxDD `-0.8275`
- `market_context_high->crypto_major_4h` score `-0.5119` n `120` status `ready` deltaP `13.6382` edge `0.2115` maxDD `-20.9394`
- `news_risk_high->equity_1h` score `-0.5508` n `80` status `ready` deltaP `8.9072` edge `-0.0366` maxDD `-5.1385`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
