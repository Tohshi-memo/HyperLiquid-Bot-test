# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T08:37:38.534351+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4042`

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

- `news_risk_high->crypto_alt_4h` score `-0.1731` n `136` status `ready` deltaP `6.7431` edge `0.1965` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4783` n `136` status `ready` deltaP `2.994` edge `0.0415` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6741` n `136` status `ready` deltaP `-2.1354` edge `-0.0021` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7536` n `136` status `ready` deltaP `2.2719` edge `0.001` maxDD `-1.3155`
- `news_risk_high->index_4h` score `-1.1428` n `136` status `ready` deltaP `3.7572` edge `0.0097` maxDD `-3.5004`
- `news_risk_high->metal_1h` score `-1.3168` n `136` status `ready` deltaP `-5.7194` edge `-0.0155` maxDD `-2.5487`
- `news_risk_high->fx_4h` score `-1.4867` n `136` status `ready` deltaP `-8.6083` edge `-0.0124` maxDD `-1.6648`
- `news_risk_high->index_24h` score `-1.6292` n `136` status `ready` deltaP `-9.3425` edge `0.0869` maxDD `-6.6786`
- `news_risk_high->crypto_major_1h` score `-1.987` n `136` status `ready` deltaP `-4.3325` edge `-0.0057` maxDD `-6.1465`
- `news_risk_high->fx_24h` score `-2.2936` n `136` status `ready` deltaP `-22.5778` edge `-0.023` maxDD `-1.6422`
- `news_risk_high->commodity_1h` score `-2.743` n `136` status `ready` deltaP `-13.0988` edge `-0.0046` maxDD `-3.2657`
- `news_risk_high->crypto_major_4h` score `-3.0941` n `136` status `ready` deltaP `-6.2769` edge `0.0362` maxDD `-14.8423`
- `news_risk_high->equity_1h` score `-3.1638` n `136` status `ready` deltaP `-4.5351` edge `0.0075` maxDD `-14.2732`
- `news_risk_high->equity_24h` score `-4.1815` n `136` status `ready` deltaP `14.0571` edge `0.7623` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.5363` n `136` status `ready` deltaP `-19.7991` edge `-0.0106` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8319` n `136` status `ready` deltaP `-10.6797` edge `-0.069` maxDD `-7.9965`
- `news_risk_high->metal_24h` score `-7.2218` n `136` status `ready` deltaP `-13.1487` edge `-0.2653` maxDD `-11.2423`
- `news_risk_high->equity_4h` score `-7.2577` n `136` status `ready` deltaP `4.2145` edge `0.0454` maxDD `-42.9308`
- `news_risk_high->commodity_24h` score `-10.8503` n `136` status `ready` deltaP `-21.1505` edge `0.0521` maxDD `-43.5567`
- `news_risk_high->crypto_alt_24h` score `-12.3328` n `136` status `ready` deltaP `5.8391` edge `0.0794` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
