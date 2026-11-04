# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T10:22:29.545473+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4038`

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

- `news_risk_high->crypto_alt_4h` score `0.1281` n `146` status `ready` deltaP `7.9143` edge `0.2273` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4449` n `146` status `ready` deltaP `2.3316` edge `0.0502` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7277` n `146` status `ready` deltaP `-2.9714` edge `-0.0034` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8556` n `146` status `ready` deltaP `1.6467` edge `-0.0023` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.353` n `146` status `ready` deltaP `-5.6968` edge `-0.0133` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4701` n `146` status `ready` deltaP `-7.622` edge `-0.0125` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.801` n `146` status `ready` deltaP `0.509` edge `0.0499` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.8342` n `146` status `ready` deltaP `0.2318` edge `-0.0066` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-2.1054` n `146` status `ready` deltaP `8.8256` edge `0.1239` maxDD `-16.6552`
- `news_risk_high->fx_24h` score `-2.361` n `146` status `ready` deltaP `-17.8534` edge `-0.0128` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4007` n `146` status `ready` deltaP `-9.3758` edge `-0.0009` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6073` n `146` status `ready` deltaP `-5.5881` edge `-0.0294` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1012` n `146` status `ready` deltaP `-7.2574` edge `-0.0375` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8168` n `146` status `ready` deltaP `-12.1701` edge `-0.0015` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6744` n `146` status `ready` deltaP `-4.2516` edge `-0.0407` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.7133` n `146` status `ready` deltaP `-11.6397` edge `-0.0799` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.0876` n `146` status `ready` deltaP `17.4587` edge `0.5462` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-10.3113` n `146` status `ready` deltaP `15.0281` edge `0.4909` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.3072` n `146` status `ready` deltaP `-0.8353` edge `-0.1006` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2883` n `146` status `ready` deltaP `-20.7834` edge `-0.0594` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
