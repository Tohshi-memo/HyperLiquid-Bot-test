# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T19:37:29.214668+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4999`

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

- `news_risk_high->crypto_alt_4h` score `0.01` n `146` status `ready` deltaP `4.7131` edge `0.2335` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4456` n `146` status `ready` deltaP `1.8825` edge `0.0531` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5735` n `146` status `ready` deltaP `-0.1271` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8913` n `126` status `ready` deltaP `12.5744` edge `0.1275` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0293` n `146` status `ready` deltaP `-0.1497` edge `-0.0048` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2522` n `146` status `ready` deltaP `-3.5061` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3327` n `146` status `ready` deltaP `-5.6968` edge `-0.0107` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-1.656` n `126` status `ready` deltaP `17.2371` edge `0.6233` maxDD `-65.3749`
- `news_risk_high->index_4h` score `-2.2333` n `146` status `ready` deltaP `-5.1036` edge `-0.0222` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2695` n `126` status `ready` deltaP `-16.9643` edge `-0.007` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.2738` n `146` status `ready` deltaP `-7.8788` edge `-0.0003` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.5125` n `126` status `ready` deltaP `-6.4237` edge `0.0049` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.6968` n `146` status `ready` deltaP `-6.636` edge `-0.0339` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1624` n `146` status `ready` deltaP `-7.7065` edge `-0.0396` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7144` n `146` status `ready` deltaP `-10.9506` edge `-0.0011` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.1558` n `126` status `ready` deltaP `12.376` edge `0.3942` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.8397` n `146` status `ready` deltaP `-6.843` edge `-0.0372` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1298` n `146` status `ready` deltaP `-14.536` edge `-0.0953` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-11.0462` n `126` status `ready` deltaP `-18.75` edge `-0.1145` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-12.0758` n `146` status `ready` deltaP `-3.1219` edge `-0.1494` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
