# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T00:52:31.778744+00:00`
- Price records: `672`
- Market context records: `7618`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->equity_24h` score `0.8199` n `145` status `ready` deltaP `16.9771` edge `0.4825` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.4889` n `146` status `ready` deltaP `11.1849` edge `0.0842` maxDD `-4.775`
- `market_context_high->commodity_24h` score `0.1294` n `145` status `ready` deltaP `14.2845` edge `0.0739` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.0828` n `146` status `ready` deltaP `7.1126` edge `0.0111` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1939` n `146` status `ready` deltaP `7.5568` edge `0.0208` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2287` n `146` status `ready` deltaP `2.0548` edge `0.0202` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.282` n `146` status `ready` deltaP `3.33` edge `-0.0013` maxDD `-1.5641`
- `market_context_high->commodity_4h` score `-0.3235` n `146` status `ready` deltaP `5.1234` edge `0.0134` maxDD `-2.2943`
- `market_context_high->fx_24h` score `-0.3491` n `145` status `ready` deltaP `9.2803` edge `0.0178` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4682` n `146` status `ready` deltaP `5.9773` edge `0.0515` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.6018` n `146` status `ready` deltaP `9.522` edge `0.0295` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.6216` n `146` status `ready` deltaP `1.538` edge `0.0146` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6774` n `146` status `ready` deltaP `-0.722` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.9542` n `146` status `ready` deltaP `3.0446` edge `0.0563` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.172` n `146` status `ready` deltaP `8.3695` edge `0.0617` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4115` n `146` status `ready` deltaP `-0.0861` edge `-0.0547` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.4725` n `146` status `ready` deltaP `2.3669` edge `0.2098` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.6101` n `146` status `ready` deltaP `-0.9084` edge `0.0453` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.9551` n `146` status `ready` deltaP `-3.1036` edge `0.0957` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5776` n `146` status `ready` deltaP `-6.3529` edge `-0.004` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
