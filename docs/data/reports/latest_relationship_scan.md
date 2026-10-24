# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T22:07:28.324327+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `19.4332` n `100` status `ready` deltaP `-0.8598` edge `1.6587` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.8943` n `66` status `ready` deltaP `24.9685` edge `0.0823` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `1.0572` n `100` status `ready` deltaP `13.5488` edge `0.054` maxDD `-1.165`
- `market_context_high->commodity_1h` score `0.1909` n `107` status `ready` deltaP `7.8264` edge `0.0138` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.2074` n `107` status `ready` deltaP `0.957` edge `0.0025` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.44` n `100` status `ready` deltaP `-0.2073` edge `0.0056` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.0864` n `107` status `ready` deltaP `-2.7814` edge `-0.0068` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.3144` n `107` status `ready` deltaP `-3.5257` edge `-0.0066` maxDD `-1.6873`
- `market_context_high->fx_24h` score `-2.629` n `66` status `ready` deltaP `-8.9962` edge `-0.0046` maxDD `-2.0274`
- `market_context_high->crypto_major_1h` score `-3.2779` n `107` status `ready` deltaP `-4.8044` edge `-0.0612` maxDD `-11.0607`
- `market_context_high->metal_4h` score `-3.531` n `100` status `ready` deltaP `-11.4512` edge `-0.0306` maxDD `-5.985`
- `market_context_high->metal_24h` score `-4.0651` n `66` status `ready` deltaP `-13.3996` edge `0.0188` maxDD `-7.7914`
- `market_context_high->equity_1h` score `-4.2015` n `107` status `ready` deltaP `-2.7044` edge `-0.0992` maxDD `-12.6316`
- `market_context_high->crypto_alt_1h` score `-4.4363` n `107` status `ready` deltaP `-7.3409` edge `-0.0865` maxDD `-15.4068`
- `market_context_high->crypto_major_24h` score `-4.9646` n `66` status `ready` deltaP `-8.8384` edge `-0.1934` maxDD `-24.0664`
- `market_context_high->index_4h` score `-5.0661` n `100` status `ready` deltaP `-25.5122` edge `-0.0518` maxDD `-5.3565`
- `market_context_high->index_24h` score `-8.3169` n `66` status `ready` deltaP `-38.1786` edge `-0.1687` maxDD `-7.5879`
- `market_context_high->crypto_alt_24h` score `-13.6876` n `66` status `ready` deltaP `-5.8397` edge `-0.6055` maxDD `-77.8309`
- `market_context_high->crypto_major_4h` score `-15.7599` n `100` status `ready` deltaP `-29.0549` edge `-0.3901` maxDD `-47.6956`
- `market_context_high->equity_4h` score `-17.2856` n `100` status `ready` deltaP `-24.75` edge `-0.4801` maxDD `-51.2958`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
