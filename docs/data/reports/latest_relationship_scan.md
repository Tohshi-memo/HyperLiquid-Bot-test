# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T23:52:28.354023+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4319`

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

- `news_risk_high->crypto_alt_4h` score `-0.3975` n `146` status `ready` deltaP `7.0776` edge `0.1655` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4538` n `146` status `ready` deltaP `3.3007` edge `0.0426` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6307` n `146` status `ready` deltaP `3.5127` edge `0.004` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.6838` n `146` status `ready` deltaP `-2.2923` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.3969` n `146` status `ready` deltaP `-6.4688` edge `-0.0108` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5151` n `146` status `ready` deltaP `-8.0195` edge `-0.0186` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6275` n `146` status `ready` deltaP `1.5221` edge `0.0113` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.2666` n `146` status `ready` deltaP `-5.3668` edge `0.0128` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4797` n `146` status `ready` deltaP `-10.6477` edge `0.001` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.5964` n `146` status `ready` deltaP `-12.1628` edge `0.0324` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.6274` n `146` status `ready` deltaP `-21.432` edge `-0.0231` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-2.8547` n `146` status `ready` deltaP `-5.3914` edge `-0.0294` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8764` n `146` status `ready` deltaP `-14.5358` edge `0.0093` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6782` n `146` status `ready` deltaP `-12.4049` edge `-0.07` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.3478` n `146` status `ready` deltaP `-9.7413` edge `-0.0621` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-8.9701` n `146` status `ready` deltaP `-16.4573` edge `-0.2796` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.2409` n `146` status `ready` deltaP `-14.6253` edge `0.1535` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.379` n `146` status `ready` deltaP `2.2831` edge `0.0393` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.8854` n `146` status `ready` deltaP `9.9778` edge `0.3934` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.0967` n `146` status `ready` deltaP `3.0574` edge `-0.2564` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
