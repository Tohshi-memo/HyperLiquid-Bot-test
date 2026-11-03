# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T19:23:46.695989+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4500`

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

- `news_risk_high->crypto_alt_4h` score `0.2803` n `146` status `ready` deltaP `7.1521` edge `0.2519` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4301` n `146` status `ready` deltaP `2.1819` edge `0.0531` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7121` n `146` status `ready` deltaP `-2.672` edge `-0.0034` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8963` n `146` status `ready` deltaP `1.1976` edge `-0.0027` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1505` n `146` status `ready` deltaP `-2.8525` edge `-0.0063` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5102` n `146` status `ready` deltaP `-8.0793` edge `-0.0146` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.5835` n `146` status `ready` deltaP `12.1242` edge `0.1454` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.7394` n `146` status `ready` deltaP `1.7243` edge `0.0497` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.0246` n `146` status `ready` deltaP `-2.6646` edge `-0.0117` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2724` n `146` status `ready` deltaP `-16.4645` edge `-0.0107` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5828` n `146` status `ready` deltaP `-11.3219` edge `-0.0031` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6898` n `146` status `ready` deltaP `-7.0851` edge `-0.03` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1827` n `146` status `ready` deltaP `-7.8562` edge `-0.0403` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0887` n `146` status `ready` deltaP `-14.6091` edge `-0.0079` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.2972` n `146` status `ready` deltaP `-3.0321` edge `-0.0174` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.9166` n `146` status `ready` deltaP `21.7989` edge `0.7956` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.9368` n `146` status `ready` deltaP `-13.7738` edge `-0.0843` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-7.9238` n `146` status `ready` deltaP `18.8476` edge `0.6644` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.5646` n `146` status `ready` deltaP `-2.2072` edge `-0.1129` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.1709` n `146` status `ready` deltaP `-19.9153` edge `-0.0554` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
