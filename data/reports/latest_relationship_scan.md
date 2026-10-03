# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T23:37:27.448957+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4256`

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

- `market_context_high->unknown_1h` score `381.3331` n `50` status `ready` deltaP `12.8204` edge `31.6972` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.6968` n `50` status `ready` deltaP `12.8049` edge `26.7227` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.326` n `50` status `ready` deltaP `29.286` edge `1.0856` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.2591` n `50` status `ready` deltaP `36.0728` edge `0.8394` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.6538` n `62` status `ready` deltaP `29.2643` edge `0.7412` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.498` n `68` status `ready` deltaP `38.3339` edge `0.6396` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.2786` n `68` status `ready` deltaP `26.0044` edge `0.5676` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0981` n `50` status `ready` deltaP `16.628` edge `0.551` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.562` n `50` status `ready` deltaP `15.122` edge `0.4916` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.4854` n `62` status `ready` deltaP `32.423` edge `0.1735` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8279` n `68` status `ready` deltaP `26.9637` edge `0.2005` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.0468` n `50` status `ready` deltaP `13.006` edge `0.2335` maxDD `-3.6376`
- `market_context_high->fx_4h` score `2.9968` n `50` status `ready` deltaP `33.6037` edge `0.0392` maxDD `-0.0791`
- `news_risk_high->index_4h` score `2.9595` n `68` status `ready` deltaP `32.3888` edge `0.0569` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9103` n `68` status `ready` deltaP `13.0592` edge `0.191` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8455` n `50` status `ready` deltaP `12.3533` edge `0.1998` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.399` n `68` status `ready` deltaP `20.4448` edge `0.1052` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9839` n `68` status `ready` deltaP `24.4981` edge `0.017` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.5334` n `50` status `ready` deltaP `21.3892` edge `0.0116` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.4971` n `50` status `ready` deltaP `8.5546` edge `0.3211` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
