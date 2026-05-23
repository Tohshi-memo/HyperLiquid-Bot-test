# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T11:07:21.811523+00:00`
- Price records: `672`
- Market context records: `1625`
- Flow alert records: `6583`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8824`

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

- `market_context_high->metal_24h` score `10.4988` n `190` status `ready` deltaP `26.2354` edge `0.9426` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.0913` n `190` status `ready` deltaP `18.4064` edge `0.2727` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.4638` n `190` status `ready` deltaP `11.9897` edge `0.1515` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.6859` n `190` status `ready` deltaP `14.5988` edge `0.3119` maxDD `-19.3696`
- `market_context_high->crypto_major_4h` score `0.3926` n `190` status `ready` deltaP `10.4573` edge `0.2515` maxDD `-13.3376`
- `market_context_high->equity_24h` score `0.2431` n `190` status `ready` deltaP `16.9956` edge `0.3968` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `-0.2108` n `196` status `ready` deltaP `1.775` edge `0.0635` maxDD `-4.1892`
- `market_context_high->fx_24h` score `-0.2525` n `190` status `ready` deltaP `7.8545` edge `0.0315` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.389` n `196` status `ready` deltaP `2.4197` edge `0.0323` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.7071` n `196` status `ready` deltaP `0.2017` edge `0.0029` maxDD `-1.7205`
- `market_context_high->index_4h` score `-0.7921` n `190` status `ready` deltaP `0.8681` edge `0.0371` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.8025` n `196` status `ready` deltaP `-0.0825` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.8794` n `196` status `ready` deltaP `-0.9593` edge `0.029` maxDD `-6.1613`
- `market_context_high->commodity_1h` score `-1.0454` n `196` status `ready` deltaP `0.6324` edge `0.0008` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2774` n `196` status `ready` deltaP `3.4553` edge `0.0041` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.3556` n `190` status `ready` deltaP `9.1977` edge `0.0949` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3698` n `190` status `ready` deltaP `-10.2937` edge `-0.0141` maxDD `-1.4313`
- `market_context_high->crypto_major_24h` score `-1.3762` n `190` status `ready` deltaP `22.4104` edge `0.5945` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `-3.2193` n `190` status `ready` deltaP `22.4598` edge `0.7629` maxDD `-88.8062`
- `market_context_high->unknown_4h` score `-5.1209` n `190` status `ready` deltaP `6.9111` edge `-0.2457` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
