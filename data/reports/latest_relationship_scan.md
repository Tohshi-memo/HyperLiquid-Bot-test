# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T20:07:31.614648+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4931`

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

- `news_risk_high->crypto_alt_4h` score `0.0804` n `146` status `ready` deltaP `5.018` edge `0.2405` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4534` n `146` status `ready` deltaP `1.7328` edge `0.0531` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5899` n `146` status `ready` deltaP `-0.4265` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8913` n `126` status `ready` deltaP `12.5744` edge `0.1275` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0017` n `146` status `ready` deltaP `0.1497` edge `-0.0045` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2601` n `146` status `ready` deltaP `-3.6585` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3156` n `146` status `ready` deltaP `-5.3974` edge `-0.0105` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-1.5264` n `126` status `ready` deltaP `17.5843` edge `0.6376` maxDD `-65.3749`
- `news_risk_high->index_4h` score `-2.2081` n `146` status `ready` deltaP `-4.7987` edge `-0.021` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2881` n `146` status `ready` deltaP `-8.0285` edge `-0.0005` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.2961` n `126` status `ready` deltaP `-17.3116` edge `-0.0081` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.5024` n `126` status `ready` deltaP `-6.4237` edge `0.0062` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.6665` n `146` status `ready` deltaP `-6.3366` edge `-0.032` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1863` n `146` status `ready` deltaP `-7.8562` edge `-0.0406` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7024` n `146` status `ready` deltaP `-10.9506` edge `-0.0001` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.0184` n `126` status `ready` deltaP `12.7232` edge `0.4095` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.8215` n `146` status `ready` deltaP `-6.6906` edge `-0.0367` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0466` n `146` status `ready` deltaP `-14.2312` edge `-0.0904` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.8997` n `126` status `ready` deltaP `-18.4028` edge `-0.1046` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.9374` n `146` status `ready` deltaP `-2.817` edge `-0.1399` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
