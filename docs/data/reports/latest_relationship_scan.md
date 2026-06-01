# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T07:07:20.863855+00:00`
- Price records: `672`
- Market context records: `2539`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->crypto_alt_4h` score `5.1326` n `156` status `ready` deltaP `23.6867` edge `0.5377` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.8954` n `116` status `ready` deltaP `19.3307` edge `0.3119` maxDD `-1.626`
- `market_context_high->crypto_major_24h` score `4.8831` n `116` status `ready` deltaP `13.2663` edge `0.6303` maxDD `-19.9453`
- `market_context_high->crypto_major_4h` score `3.5742` n `156` status `ready` deltaP `17.0028` edge `0.3655` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.9365` n `156` status `ready` deltaP `11.0772` edge `0.1925` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1042` n `156` status `ready` deltaP `9.5924` edge `0.1468` maxDD `-6.1656`
- `market_context_high->equity_24h` score `0.8509` n `116` status `ready` deltaP `19.8575` edge `0.0403` maxDD `-4.809`
- `market_context_high->crypto_major_1h` score `0.6095` n `156` status `ready` deltaP `8.0109` edge `0.1168` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.2016` n `116` status `ready` deltaP `4.5259` edge `0.0847` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.0429` n `116` status `ready` deltaP `-0.1556` edge `0.6793` maxDD `-42.7009`
- `market_context_high->index_4h` score `-0.1` n `156` status `ready` deltaP `6.5119` edge `0.0324` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1309` n `156` status `ready` deltaP `3.7809` edge `0.0329` maxDD `-2.8543`
- `market_context_high->index_1h` score `-0.303` n `156` status `ready` deltaP `2.4528` edge `0.0078` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3182` n `156` status `ready` deltaP `4.6561` edge `0.016` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4257` n `156` status `ready` deltaP `1.9653` edge `0.0049` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.4601` n `156` status `ready` deltaP `1.0479` edge `0.0088` maxDD `-2.9823`
- `market_context_high->fx_4h` score `-0.8401` n `156` status `ready` deltaP `0.4886` edge `0.0127` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.8441` n `156` status `ready` deltaP `-0.3723` edge `0.016` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8565` n `116` status `ready` deltaP `3.125` edge `0.0034` maxDD `-2.3904`
- `market_context_high->metal_4h` score `-0.8726` n `156` status `ready` deltaP `3.2598` edge `0.0443` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
