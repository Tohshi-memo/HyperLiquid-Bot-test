# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T13:06:59.280051+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->index_1h` score `0.4795` n `121` status `ready` deltaP `12.2891` edge `0.0068` maxDD `-0.5685`
- `market_context_high->equity_1h` score `0.3923` n `121` status `ready` deltaP `9.2233` edge `0.0527` maxDD `-3.1861`
- `market_context_high->fx_4h` score `0.2416` n `109` status `ready` deltaP `10.7001` edge `0.0099` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0405` n `121` status `ready` deltaP `3.8687` edge `0.0049` maxDD `-0.2043`
- `market_context_high->equity_4h` score `-0.0804` n `109` status `ready` deltaP `4.4613` edge `0.1265` maxDD `-8.3685`
- `market_context_high->index_4h` score `-0.2793` n `109` status `ready` deltaP `5.9689` edge `0.0168` maxDD `-1.7252`
- `market_context_high->metal_4h` score `-0.3668` n `109` status `ready` deltaP `4.7633` edge `-0.0212` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.4619` n `105` status `ready` deltaP `4.4147` edge `0.1154` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.4815` n `121` status `ready` deltaP `0.7188` edge `-0.0053` maxDD `-0.503`
- `market_context_high->unknown_1h` score `-0.5966` n `121` status `ready` deltaP `9.8407` edge `-0.0926` maxDD `-0.4843`
- `market_context_high->commodity_1h` score `-0.6435` n `121` status `ready` deltaP `-4.006` edge `0.0008` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.6776` n `109` status `ready` deltaP `-1.6419` edge `0.0091` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.9202` n `121` status `ready` deltaP `-0.6037` edge `0.0075` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.4808` n `121` status `ready` deltaP `-3.6225` edge `-0.0632` maxDD `-4.1996`
- `market_context_high->fx_24h` score `-3.05` n `105` status `ready` deltaP `-12.8224` edge `-0.0077` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-3.1347` n `109` status `ready` deltaP `-0.7104` edge `-0.1295` maxDD `-5.4926`
- `market_context_high->index_24h` score `-4.1606` n `105` status `ready` deltaP `-5.248` edge `-0.0482` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.3197` n `109` status `ready` deltaP `-1.3313` edge `-0.249` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.4606` n `105` status `ready` deltaP `-16.7212` edge `-0.1296` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-4.8759` n `105` status `ready` deltaP `8.6409` edge `-0.4133` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
