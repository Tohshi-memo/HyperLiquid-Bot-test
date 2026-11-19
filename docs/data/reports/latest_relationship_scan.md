# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T10:37:39.881079+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2572`

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

- `market_context_high->unknown_1h` score `11471.907` n `112` status `ready` deltaP `1.1175` edge `956.0046` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7105.5775` n `112` status `ready` deltaP `0.3266` edge `592.1577` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `12.1642` n `98` status `ready` deltaP `39.594` edge `1.6226` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.3622` n `98` status `ready` deltaP `21.1416` edge `1.3999` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2583` n `112` status `ready` deltaP `3.1437` edge `0.0124` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.2795` n `112` status `ready` deltaP `13.6978` edge `0.0164` maxDD `-6.1475`
- `market_context_high->metal_24h` score `-0.3349` n `98` status `ready` deltaP `15.3557` edge `0.1922` maxDD `-15.7982`
- `market_context_high->crypto_major_4h` score `-0.3826` n `112` status `ready` deltaP `1.1542` edge `0.3015` maxDD `-22.3259`
- `market_context_high->crypto_alt_4h` score `-0.6066` n `112` status `ready` deltaP `1.6115` edge `0.1925` maxDD `-17.1476`
- `market_context_high->crypto_major_1h` score `-0.8093` n `112` status `ready` deltaP `2.8443` edge `0.064` maxDD `-10.2705`
- `market_context_high->index_1h` score `-0.8245` n `112` status `ready` deltaP `-1.4703` edge `0.0028` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.0556` n `112` status `ready` deltaP `-1.775` edge `0.0268` maxDD `-7.6911`
- `market_context_high->index_4h` score `-1.262` n `112` status `ready` deltaP `-3.8327` edge `-0.0019` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.4428` n `112` status `ready` deltaP `-9.6504` edge `-0.001` maxDD `-0.392`
- `market_context_high->fx_4h` score `-2.4358` n `112` status `ready` deltaP `-15.6577` edge `-0.0036` maxDD `-2.0104`
- `market_context_high->commodity_1h` score `-2.5738` n `112` status `ready` deltaP `-11.7408` edge `-0.0284` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.7432` n `112` status `ready` deltaP `1.358` edge `-0.0199` maxDD `-11.0868`
- `market_context_high->fx_24h` score `-6.7705` n `98` status `ready` deltaP `-19.3346` edge `-0.0044` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4172` n `112` status `ready` deltaP `-23.6716` edge `-0.0984` maxDD `-14.9509`
- `market_context_high->index_24h` score `-9.1929` n `98` status `ready` deltaP `-16.943` edge `-0.1109` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
