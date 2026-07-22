# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T23:07:30.901023+00:00`
- Price records: `672`
- Market context records: `7610`
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

- `market_context_high->equity_24h` score `1.1054` n `145` status `ready` deltaP `16.9771` edge `0.5191` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.9066` n `146` status `ready` deltaP `12.4001` edge `0.1109` maxDD `-4.775`
- `market_context_high->commodity_24h` score `0.3577` n `145` status `ready` deltaP `15.504` edge `0.0848` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.1163` n `146` status `ready` deltaP `7.5631` edge `0.0124` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1277` n `146` status `ready` deltaP `8.3053` edge `0.0243` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1929` n `146` status `ready` deltaP `2.5039` edge `0.0218` maxDD `-2.7243`
- `market_context_high->commodity_4h` score `-0.1934` n `146` status `ready` deltaP `6.1938` edge `0.0171` maxDD `-2.2943`
- `market_context_high->commodity_1h` score `-0.2468` n `146` status `ready` deltaP `3.9306` edge `-0.0008` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3335` n `145` status `ready` deltaP `9.2803` edge `0.0191` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4034` n `146` status `ready` deltaP `6.5779` edge `0.0558` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.5503` n `146` status `ready` deltaP `10.2865` edge `0.031` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.585` n `146` status `ready` deltaP `2.1368` edge `0.0153` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6534` n `146` status `ready` deltaP `-0.4217` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.9281` n `146` status `ready` deltaP `3.5019` edge `0.0566` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.08` n `146` status `ready` deltaP `9.2841` edge `0.0674` maxDD `-14.4206`
- `market_context_high->equity_4h` score `-1.3835` n `146` status `ready` deltaP `3.2843` edge `0.2151` maxDD `-20.4824`
- `market_context_high->unknown_1h` score `-1.4631` n `146` status `ready` deltaP `-0.2358` edge `-0.058` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.5984` n `146` status `ready` deltaP `-0.9084` edge `0.0468` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.796` n `146` status `ready` deltaP `-1.8883` edge `0.108` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5642` n `146` status `ready` deltaP `-6.2` edge `-0.0039` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
