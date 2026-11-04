# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T06:52:26.620828+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4411`

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

- `news_risk_high->crypto_alt_4h` score `0.6424` n `146` status `ready` deltaP `9.2863` edge `0.2841` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4426` n `146` status `ready` deltaP `2.3316` edge `0.0505` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.709` n `146` status `ready` deltaP `-2.672` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7693` n `146` status `ready` deltaP `2.5449` edge `-0.0011` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2931` n `146` status `ready` deltaP `-4.7986` edge `-0.0116` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4654` n `146` status `ready` deltaP `-7.622` edge `-0.0119` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.509` n `146` status `ready` deltaP `11.2562` edge `0.1574` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.6784` n `146` status `ready` deltaP `2.0715` edge `0.0552` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.7575` n `146` status `ready` deltaP `0.5367` edge `0.0012` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3407` n `146` status `ready` deltaP `-17.8534` edge `-0.0102` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.445` n `146` status `ready` deltaP `-9.8249` edge `-0.0016` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.5543` n `146` status `ready` deltaP `-5.2887` edge `-0.0246` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.0976` n `146` status `ready` deltaP `-7.2574` edge `-0.0372` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8522` n `146` status `ready` deltaP `-12.6274` edge `-0.0014` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3972` n `146` status `ready` deltaP `-3.3369` edge `-0.0237` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.0671` n `146` status `ready` deltaP `-10.2677` edge `-0.0352` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-6.9183` n `146` status `ready` deltaP `19.8892` edge `0.6799` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-8.9673` n `146` status `ready` deltaP `17.4587` edge `0.5867` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.4917` n `146` status `ready` deltaP `0.6891` edge `-0.0428` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3483` n `146` status `ready` deltaP `-20.7834` edge `-0.0644` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
