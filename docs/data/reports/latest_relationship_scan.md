# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T17:07:26.704163+00:00`
- Price records: `672`
- Market context records: `7050`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.4035` n `198` status `ready` deltaP `14.5787` edge `0.0106` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.3127` n `198` status `ready` deltaP `2.619` edge `0.0016` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.5737` n `198` status `ready` deltaP `1.2339` edge `0.0304` maxDD `-4.5815`
- `market_context_high->commodity_1h` score `-0.7834` n `198` status `ready` deltaP `-3.4053` edge `-0.0161` maxDD `-1.9306`
- `market_context_high->index_1h` score `-0.8` n `198` status `ready` deltaP `-1.1765` edge `-0.0036` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8251` n `198` status `ready` deltaP `-4.0193` edge `-0.0022` maxDD `-2.1427`
- `market_context_high->unknown_1h` score `-0.913` n `198` status `ready` deltaP `-2.6553` edge `0.015` maxDD `-2.204`
- `market_context_high->crypto_major_1h` score `-0.9614` n `198` status `ready` deltaP `3.4976` edge `0.0318` maxDD `-7.1523`
- `market_context_high->unknown_4h` score `-1.3768` n `198` status `ready` deltaP `-5.6911` edge `0.1022` maxDD `-5.9862`
- `market_context_high->equity_1h` score `-1.9457` n `198` status `ready` deltaP `3.2752` edge `-0.029` maxDD `-14.716`
- `market_context_high->metal_4h` score `-2.0971` n `198` status `ready` deltaP `3.7894` edge `0.0042` maxDD `-5.5324`
- `market_context_high->index_4h` score `-2.1635` n `198` status `ready` deltaP `2.9148` edge `-0.0269` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.2172` n `198` status `ready` deltaP `-0.5524` edge `-0.0502` maxDD `-4.4704`
- `market_context_high->commodity_4h` score `-2.2719` n `198` status `ready` deltaP `-5.2491` edge `-0.0383` maxDD `-2.9494`
- `market_context_high->crypto_alt_4h` score `-2.5929` n `198` status `ready` deltaP `2.7917` edge `0.0275` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.7977` n `198` status `ready` deltaP `4.45` edge `0.0401` maxDD `-24.6094`
- `market_context_high->unknown_24h` score `-3.0601` n `198` status `ready` deltaP `-12.2159` edge `0.2038` maxDD `-23.5076`
- `market_context_high->fx_24h` score `-3.5216` n `198` status `ready` deltaP `-0.1736` edge `-0.0096` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.6876` n `198` status `ready` deltaP `3.1719` edge `-0.1197` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.0091` n `198` status `ready` deltaP `-16.935` edge `-0.0785` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
