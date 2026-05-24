# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T07:22:16.487399+00:00`
- Price records: `672`
- Market context records: `1712`
- Flow alert records: `6837`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `6.7218` n `138` status `ready` deltaP `25.4175` edge `0.6333` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.234` n `196` status `ready` deltaP `22.0384` edge `0.5492` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.5836` n `196` status `ready` deltaP `23.3294` edge `0.467` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.8555` n `138` status `ready` deltaP `16.6692` edge `0.333` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.0515` n `196` status `ready` deltaP `16.4167` edge `0.2543` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.3931` n `138` status `ready` deltaP `15.5007` edge `0.5026` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.9504` n `196` status `ready` deltaP `8.0197` edge `0.1281` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.5406` n `196` status `ready` deltaP `8.5117` edge `0.0972` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `0.3809` n `138` status `ready` deltaP `23.9482` edge `1.053` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.2856` n `196` status `ready` deltaP `5.1968` edge `0.0965` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0683` n `196` status `ready` deltaP `4.6713` edge `0.0554` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.1939` n `196` status `ready` deltaP `13.0538` edge `0.1573` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.4419` n `196` status `ready` deltaP `6.2447` edge `0.0353` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.4443` n `196` status `ready` deltaP `0.9227` edge `0.02` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6622` n `196` status `ready` deltaP `-3.1162` edge `-0.0009` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.8112` n `138` status `ready` deltaP `4.4406` edge `0.0077` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.995` n `138` status `ready` deltaP `22.0976` edge `0.5837` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.7876` n `196` status `ready` deltaP `-6.9717` edge `-0.0096` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.0134` n `196` status `ready` deltaP `0.333` edge `-0.0149` maxDD `-14.9691`
- `market_context_high->unknown_24h` score `-4.8943` n `138` status `ready` deltaP `17.622` edge `0.0067` maxDD `-35.8966`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
