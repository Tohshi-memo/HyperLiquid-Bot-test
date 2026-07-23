# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T01:07:27.151052+00:00`
- Price records: `672`
- Market context records: `7619`
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

- `market_context_high->equity_24h` score `0.823` n `145` status `ready` deltaP `16.9771` edge `0.4829` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.4246` n `146` status `ready` deltaP `11.0112` edge `0.08` maxDD `-4.775`
- `market_context_high->commodity_24h` score `0.1022` n `145` status `ready` deltaP `14.1103` edge `0.0728` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.0742` n `146` status `ready` deltaP `6.9625` edge `0.011` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1962` n `146` status `ready` deltaP `7.5568` edge `0.0205` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2388` n `146` status `ready` deltaP `1.9051` edge `0.0199` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.2898` n `146` status `ready` deltaP `3.1798` edge `-0.0013` maxDD `-1.5641`
- `market_context_high->commodity_4h` score `-0.3405` n `146` status `ready` deltaP `4.9705` edge `0.013` maxDD `-2.2943`
- `market_context_high->fx_24h` score `-0.3467` n `145` status `ready` deltaP `9.2803` edge `0.018` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4791` n `146` status `ready` deltaP `5.8271` edge `0.0511` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.6026` n `146` status `ready` deltaP `9.522` edge `0.0294` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.6302` n `146` status `ready` deltaP `1.3883` edge `0.0145` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6762` n `146` status `ready` deltaP `-0.722` edge `-0.0016` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.9542` n `146` status `ready` deltaP `3.0446` edge `0.0563` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.187` n `146` status `ready` deltaP `8.217` edge `0.0608` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4127` n `146` status `ready` deltaP `-0.0861` edge `-0.0548` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.4725` n `146` status `ready` deltaP `2.3669` edge `0.2098` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.6188` n `146` status `ready` deltaP `-1.0608` edge `0.0452` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.9559` n `146` status `ready` deltaP `-3.1036` edge `0.0956` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5764` n `146` status `ready` deltaP `-6.3529` edge `-0.0039` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
