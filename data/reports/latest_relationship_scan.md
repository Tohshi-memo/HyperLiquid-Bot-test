# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T11:37:25.635779+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_4h` score `39.6159` n `113` status `ready` deltaP `-0.2914` edge `3.3368` maxDD `-1.016`
- `market_context_high->unknown_1h` score `3.6037` n `113` status `ready` deltaP `4.0207` edge `0.3224` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `0.8702` n `52` status `ready` deltaP `18.5496` edge `0.0788` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0487` n `113` status `ready` deltaP `8.221` edge `0.0091` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0498` n `113` status `ready` deltaP `3.8591` edge `0.0028` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5601` n `113` status `ready` deltaP `-0.7816` edge `0.0086` maxDD `-1.0053`
- `market_context_high->crypto_major_24h` score `-0.5697` n `52` status `ready` deltaP `-0.4941` edge `0.0328` maxDD `-4.5369`
- `market_context_high->metal_1h` score `-0.6203` n `113` status `ready` deltaP `4.7838` edge `-0.0044` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6246` n `113` status `ready` deltaP `-1.4374` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.9075` n `113` status `ready` deltaP `-3.4576` edge `0.0296` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3409` n `113` status `ready` deltaP `2.1991` edge `-0.0285` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8332` n `113` status `ready` deltaP `5.3758` edge `-0.0176` maxDD `-5.3474`
- `market_context_high->fx_24h` score `-2.1034` n `52` status `ready` deltaP `-4.3403` edge `0.0067` maxDD `-1.244`
- `market_context_high->index_4h` score `-2.1506` n `113` status `ready` deltaP `-7.7676` edge `-0.0365` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.0478` n `113` status `ready` deltaP `-2.0097` edge `-0.0532` maxDD `-11.3243`
- `market_context_high->crypto_alt_24h` score `-3.3521` n `52` status `ready` deltaP `5.5823` edge `-0.0201` maxDD `-29.7494`
- `market_context_high->metal_24h` score `-3.5305` n `52` status `ready` deltaP `-10.1362` edge `0.0006` maxDD `-7.1786`
- `market_context_high->equity_1h` score `-3.7636` n `113` status `ready` deltaP `0.0596` edge `-0.0867` maxDD `-12.1865`
- `market_context_high->index_24h` score `-4.1662` n `52` status `ready` deltaP `-9.9226` edge `-0.1528` maxDD `-4.925`
- `market_context_high->crypto_major_4h` score `-10.022` n `113` status `ready` deltaP `-12.7428` edge `-0.2504` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
