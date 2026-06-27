# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T04:52:28.348224+00:00`
- Price records: `672`
- Market context records: `4899`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8590`

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

- `market_context_high->unknown_1h` score `14.7415` n `110` status `ready` deltaP `9.423` edge `1.2074` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5434` n `110` status `ready` deltaP `23.1624` edge `0.694` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.5134` n `110` status `ready` deltaP `21.3609` edge `0.5356` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.4466` n `110` status `ready` deltaP `18.9495` edge `0.5333` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.4762` n `91` status `ready` deltaP `24.6013` edge `0.3266` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1101` n `110` status `ready` deltaP `7.9102` edge `0.106` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8976` n `110` status `ready` deltaP `12.439` edge `0.1703` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5312` n `110` status `ready` deltaP `11.0781` edge `0.0405` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.5038` n `110` status `ready` deltaP `6.7692` edge `0.1233` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4425` n `110` status `ready` deltaP `8.3206` edge `0.1035` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2301` n `110` status `ready` deltaP `4.3849` edge `0.06` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.2172` n `110` status `ready` deltaP `-0.0545` edge `0.0305` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2215` n `110` status `ready` deltaP `3.2825` edge `0.0157` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5156` n `110` status `ready` deltaP `-0.2885` edge `0.0113` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.7273` n `110` status `ready` deltaP `0.0` edge `0.0038` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.7905` n `110` status `ready` deltaP `7.0343` edge `0.0059` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3538` n `110` status `ready` deltaP `-7.0169` edge `-0.0047` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.5616` n `91` status `ready` deltaP `-3.2109` edge `-0.0077` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.5753` n `91` status `ready` deltaP `-5.5823` edge `-0.1408` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.5855` n `91` status `ready` deltaP `16.5827` edge `0.0182` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
