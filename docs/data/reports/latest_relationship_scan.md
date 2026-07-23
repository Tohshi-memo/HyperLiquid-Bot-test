# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T09:07:32.018569+00:00`
- Price records: `672`
- Market context records: `7654`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14697`

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

- `market_context_high->index_1h` score `0.05` n `146` status `ready` deltaP `6.512` edge `0.0109` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.19` n `146` status `ready` deltaP `7.8562` edge `0.0193` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2903` n `146` status `ready` deltaP `1.456` edge `0.0163` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3563` n `145` status `ready` deltaP `9.2803` edge `0.0172` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.3967` n `146` status `ready` deltaP `1.5282` edge `-0.004` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5423` n `146` status `ready` deltaP `5.0764` edge `0.048` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6489` n `146` status `ready` deltaP `0.9392` edge `0.0151` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.7116` n `146` status `ready` deltaP `1.6066` edge `0.0045` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.7222` n `146` status `ready` deltaP `7.6871` edge `0.0263` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.7555` n `146` status `ready` deltaP `-1.6229` edge `-0.0022` maxDD `-0.6615`
- `market_context_high->commodity_24h` score `-0.8909` n `145` status `ready` deltaP `8.5354` edge `0.0272` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `-1.1158` n `146` status `ready` deltaP `1.9775` edge `0.0427` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1892` n `146` status `ready` deltaP `9.2841` edge `0.0534` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.5158` n `146` status `ready` deltaP `-1.134` edge `-0.0564` maxDD `-1.3217`
- `market_context_high->equity_24h` score `-1.5582` n `145` status `ready` deltaP `14.1896` edge `0.1962` maxDD `-34.5784`
- `market_context_high->equity_4h` score `-1.7065` n `146` status `ready` deltaP `0.8378` edge `0.19` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.7084` n `146` status `ready` deltaP `-2.7376` edge `0.0449` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.2379` n `146` status `ready` deltaP `-3.2772` edge `0.0606` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.7534` n `146` status `ready` deltaP `-8.3407` edge `-0.0054` maxDD `-2.1425`
- `market_context_high->unknown_24h` score `-2.7534` n `146` status `ready` deltaP `5.4557` edge `-0.1478` maxDD `-4.775`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
