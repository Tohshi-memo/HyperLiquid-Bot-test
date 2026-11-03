# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T07:07:28.911794+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `news_risk_high->crypto_alt_4h` score `0.2459` n `146` status `ready` deltaP `6.0851` edge `0.2546` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3841` n `146` status `ready` deltaP `2.4813` edge `0.057` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6031` n `146` status `ready` deltaP `-0.7259` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9191` n `146` status `ready` deltaP `1.0479` edge `-0.0036` maxDD `-1.3981`
- `news_risk_high->metal_24h` score `-0.9986` n `136` status `ready` deltaP `10.9171` edge `0.1248` maxDD `-14.0483`
- `news_risk_high->fx_4h` score `-1.2341` n `146` status `ready` deltaP `-3.3537` edge `-0.0107` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2845` n `146` status `ready` deltaP `-4.9483` edge `-0.0095` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.0679` n `146` status `ready` deltaP `-3.1219` edge `-0.0142` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.1927` n `136` status `ready` deltaP `-3.0943` edge `0.0237` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.3852` n `146` status `ready` deltaP `-9.0764` edge `-0.0016` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4006` n `136` status `ready` deltaP `-17.79` edge `-0.0183` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7031` n `146` status `ready` deltaP `-6.9354` edge `-0.0327` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1935` n `146` status `ready` deltaP `-8.0059` edge `-0.0402` maxDD `-9.4709`
- `news_risk_high->crypto_alt_24h` score `-3.452` n `136` status `ready` deltaP `20.4963` edge `0.7798` maxDD `-94.7206`
- `news_risk_high->commodity_4h` score `-3.8364` n `146` status `ready` deltaP `-12.475` edge `-0.0011` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.5524` n `136` status `ready` deltaP `15.6352` edge `0.5259` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.8139` n `146` status `ready` deltaP `-7.3004` edge `-0.032` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.985` n `146` status `ready` deltaP `-13.9263` edge `-0.0873` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-11.576` n `146` status `ready` deltaP `-1.7499` edge `-0.1169` maxDD `-52.2214`
- `news_risk_high->crypto_major_24h` score `-12.1408` n `136` status `ready` deltaP `-12.8064` edge `0.0391` maxDD `-63.2368`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
