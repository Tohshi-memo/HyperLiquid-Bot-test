# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T23:07:29.051726+00:00`
- Price records: `672`
- Market context records: `5087`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10352`

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

- `market_context_high->unknown_24h` score `13.5214` n `74` status `ready` deltaP `27.0364` edge `0.9808` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `9.94` n `107` status `ready` deltaP `1.5879` edge `0.8819` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `8.9384` n `95` status `ready` deltaP `21.688` edge `0.7025` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.5923` n `95` status `ready` deltaP `15.9306` edge `0.4863` maxDD `-6.7853`
- `market_context_high->crypto_major_4h` score `4.4654` n `95` status `ready` deltaP `14.4352` edge `0.4805` maxDD `-12.0362`
- `market_context_high->equity_4h` score `2.4509` n `95` status `ready` deltaP `13.7532` edge `0.2257` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.2613` n `107` status `ready` deltaP `11.5325` edge `0.0814` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.5183` n `107` status `ready` deltaP `5.3668` edge `0.1019` maxDD `-4.8921`
- `market_context_high->index_1h` score `0.5088` n `107` status `ready` deltaP `8.13` edge `0.018` maxDD `-0.3843`
- `market_context_high->index_4h` score `0.4416` n `95` status `ready` deltaP `9.7529` edge `0.0479` maxDD `-1.0893`
- `market_context_high->metal_1h` score `0.4058` n `107` status `ready` deltaP `10.6021` edge `0.031` maxDD `-1.3057`
- `market_context_high->crypto_major_1h` score `0.2576` n `107` status `ready` deltaP `6.6414` edge `0.1133` maxDD `-6.9636`
- `market_context_high->metal_4h` score `0.2337` n `95` status `ready` deltaP `7.524` edge `0.0877` maxDD `-1.9651`
- `market_context_high->commodity_4h` score `-0.6684` n `95` status `ready` deltaP `7.8578` edge `0.0041` maxDD `-3.9745`
- `market_context_high->commodity_1h` score `-0.8024` n `107` status `ready` deltaP `0.2085` edge `0.002` maxDD `-1.6202`
- `market_context_high->fx_24h` score `-1.156` n `74` status `ready` deltaP `-1.4499` edge `-0.0063` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.324` n `74` status `ready` deltaP `11.036` edge `0.0529` maxDD `-15.0303`
- `market_context_high->fx_1h` score `-1.8389` n `107` status `ready` deltaP `-12.5763` edge `-0.0053` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-2.166` n `95` status `ready` deltaP `-9.6951` edge `-0.0107` maxDD `-1.7469`
- `market_context_high->metal_24h` score `-4.5382` n `74` status `ready` deltaP `-5.2412` edge `-0.0014` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
