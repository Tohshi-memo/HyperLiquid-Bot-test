# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T23:37:35.927650+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.392` n `146` status `ready` deltaP `7.0776` edge `0.1662` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4499` n `146` status `ready` deltaP `3.3007` edge `0.0431` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6451` n `146` status `ready` deltaP `3.3632` edge `0.0038` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.6838` n `146` status `ready` deltaP `-2.2923` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.3969` n `146` status `ready` deltaP `-6.4688` edge `-0.0108` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5144` n `146` status `ready` deltaP `-8.0195` edge `-0.0185` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6306` n `146` status `ready` deltaP `1.5221` edge `0.0109` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.2775` n `146` status `ready` deltaP `-5.3668` edge `0.0114` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4677` n `146` status `ready` deltaP `-10.4982` edge `0.001` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.6113` n `146` status `ready` deltaP `-12.1628` edge `0.0305` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.6153` n `146` status `ready` deltaP `-21.259` edge `-0.0227` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-2.8403` n `146` status `ready` deltaP `-5.3914` edge `-0.0282` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8776` n `146` status `ready` deltaP `-14.5358` edge `0.0092` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6782` n `146` status `ready` deltaP `-12.4049` edge `-0.07` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.3502` n `146` status `ready` deltaP `-9.7413` edge `-0.0623` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-8.9521` n `146` status `ready` deltaP `-16.4573` edge `-0.2781` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.2229` n `146` status `ready` deltaP `-14.6253` edge `0.155` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.4258` n `146` status `ready` deltaP `2.2831` edge `0.0354` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-12.0234` n `146` status `ready` deltaP `9.9778` edge `0.3819` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.2017` n `146` status `ready` deltaP `2.8843` edge `-0.2687` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
