# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T22:07:31.887244+00:00`
- Price records: `672`
- Market context records: `7606`
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

- `market_context_high->equity_24h` score `1.2466` n `145` status `ready` deltaP `16.9771` edge `0.5372` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `1.1361` n `146` status `ready` deltaP `13.0946` edge `0.1254` maxDD `-4.775`
- `market_context_high->commodity_24h` score `0.4903` n `145` status `ready` deltaP `16.2009` edge `0.0912` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.1062` n `146` status `ready` deltaP `7.4129` edge `0.0121` maxDD `-0.8324`
- `market_context_high->commodity_4h` score `-0.1265` n `146` status `ready` deltaP `6.8054` edge `0.0186` maxDD `-2.2943`
- `market_context_high->crypto_major_1h` score `-0.1401` n `146` status `ready` deltaP `8.1556` edge `0.0237` maxDD `-4.0162`
- `market_context_high->commodity_1h` score `-0.2258` n `146` status `ready` deltaP `4.2309` edge `-0.0001` maxDD `-1.5641`
- `market_context_high->crypto_alt_1h` score `-0.2365` n `146` status `ready` deltaP `1.9051` edge `0.0202` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3239` n `145` status `ready` deltaP `9.2803` edge `0.0199` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.419` n `146` status `ready` deltaP `6.4277` edge `0.0548` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.5449` n `146` status `ready` deltaP `10.2865` edge `0.0317` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.6131` n `146` status `ready` deltaP `1.6877` edge `0.0147` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6546` n `146` status `ready` deltaP `-0.4217` edge `-0.0018` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.9116` n `146` status `ready` deltaP `3.6543` edge `0.0577` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.0367` n `146` status `ready` deltaP `9.7414` edge `0.0699` maxDD `-14.4206`
- `market_context_high->equity_4h` score `-1.3315` n `146` status `ready` deltaP `3.743` edge `0.2187` maxDD `-20.4824`
- `market_context_high->unknown_1h` score `-1.535` n `146` status `ready` deltaP `-0.8346` edge `-0.06` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.5953` n `146` status `ready` deltaP `-0.9084` edge `0.0472` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.7076` n `146` status `ready` deltaP `-1.1939` edge `0.1147` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5788` n `146` status `ready` deltaP `-6.3529` edge `-0.0041` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
