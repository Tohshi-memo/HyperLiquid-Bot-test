# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T07:52:27.950800+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4300`

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

- `news_risk_high->crypto_alt_4h` score `-0.0503` n `139` status `ready` deltaP `7.6636` edge `0.2061` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4503` n `139` status `ready` deltaP `3.5034` edge `0.0417` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.664` n `139` status `ready` deltaP `-1.973` edge `-0.0019` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7695` n `139` status `ready` deltaP `2.2433` edge `0.0009` maxDD `-1.3981`
- `news_risk_high->index_4h` score `-1.3168` n `139` status `ready` deltaP `3.1036` edge `0.0083` maxDD `-3.8248`
- `news_risk_high->fx_4h` score `-1.5471` n `139` status `ready` deltaP `-9.0729` edge `-0.0127` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.8321` n `139` status `ready` deltaP `-10.2312` edge `0.0793` maxDD `-6.6786`
- `news_risk_high->metal_1h` score `-2.0576` n `139` status `ready` deltaP `-6.2067` edge `-0.0149` maxDD `-2.5487`
- `news_risk_high->crypto_major_1h` score `-2.2548` n `139` status `ready` deltaP `-4.7721` edge `-0.0125` maxDD `-7.1534`
- `news_risk_high->fx_24h` score `-2.4859` n `139` status `ready` deltaP `-23.6887` edge `-0.0253` maxDD `-1.8382`
- `news_risk_high->commodity_1h` score `-2.6362` n `139` status `ready` deltaP `-12.0493` edge `-0.0027` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-3.4253` n `139` status `ready` deltaP `-5.0381` edge `0.0038` maxDD `-15.4525`
- `news_risk_high->crypto_major_4h` score `-3.4799` n `139` status `ready` deltaP `-6.9497` edge `0.0298` maxDD `-16.2102`
- `news_risk_high->commodity_4h` score `-4.4017` n `139` status `ready` deltaP `-18.7171` edge `-0.0066` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.0446` n `139` status `ready` deltaP `-11.1269` edge `-0.0682` maxDD `-8.2402`
- `news_risk_high->equity_24h` score `-5.1147` n `139` status `ready` deltaP `12.7717` edge `0.7056` maxDD `-86.0244`
- `news_risk_high->metal_24h` score `-7.7552` n `139` status `ready` deltaP `-14.3548` edge `-0.2723` maxDD `-12.5948`
- `news_risk_high->equity_4h` score `-8.0813` n `139` status `ready` deltaP `3.5609` edge `0.0332` maxDD `-46.0972`
- `news_risk_high->commodity_24h` score `-10.7678` n `139` status `ready` deltaP `-20.1962` edge `0.0634` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-12.2797` n `139` status `ready` deltaP `6.3516` edge `0.0828` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
