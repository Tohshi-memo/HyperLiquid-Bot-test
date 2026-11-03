# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T14:22:32.837297+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.2368` n `146` status `ready` deltaP `6.3899` edge `0.2514` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5103` n `146` status `ready` deltaP `1.2837` edge `0.0488` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6296` n `146` status `ready` deltaP `-1.175` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9287` n `146` status `ready` deltaP `0.8982` edge `-0.0034` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2292` n `146` status `ready` deltaP `-4.0501` edge `-0.0084` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.3543` n `146` status `ready` deltaP `-5.3354` edge `-0.0129` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.7702` n `146` status `ready` deltaP `11.9506` edge `0.131` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.9621` n `146` status `ready` deltaP `-0.8799` edge `0.0385` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.0121` n `146` status `ready` deltaP `-2.6646` edge `-0.0101` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3215` n `146` status `ready` deltaP `-16.4645` edge `-0.017` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4726` n `146` status `ready` deltaP `-10.1243` edge `-0.0019` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.696` n `146` status `ready` deltaP `-6.9354` edge `-0.0318` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2822` n `146` status `ready` deltaP `-8.6047` edge `-0.0436` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.2749` n `146` status `ready` deltaP `-15.6762` edge `-0.0163` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.4116` n `146` status `ready` deltaP `-4.2516` edge `-0.0188` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.891` n `146` status `ready` deltaP `21.4517` edge `0.8012` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.849` n `146` status `ready` deltaP `-13.6214` edge `-0.078` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.8448` n `146` status `ready` deltaP `16.5906` edge `0.6075` maxDD `-102.7472`
- `news_risk_high->equity_4h` score `-11.1774` n `146` status `ready` deltaP `-0.6828` edge `-0.0908` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.5913` n `146` status `ready` deltaP `-21.8251` edge `-0.0777` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
