# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T18:52:33.967337+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7160`

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

- `news_risk_high->unknown_24h` score `2590.3843` n `139` status `ready` deltaP `1.3889` edge `215.8561` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.7367` n `139` status `ready` deltaP `30.8516` edge `1.5009` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.5625` n `139` status `ready` deltaP `32.3591` edge `0.8358` maxDD `-11.039`
- `news_risk_high->crypto_major_24h` score `7.5985` n `139` status `ready` deltaP `24.8938` edge `0.9107` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.0999` n `139` status `ready` deltaP `38.3381` edge `0.1556` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.6236` n `139` status `ready` deltaP `31.2388` edge `0.2792` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `3.0025` n `142` status `ready` deltaP `29.8094` edge `0.2116` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.906` n `142` status `ready` deltaP `10.9198` edge `0.352` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.0547` n `142` status `ready` deltaP `8.3179` edge `0.1235` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.733` n `142` status `ready` deltaP `8.4507` edge `0.0707` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.5353` n `142` status `ready` deltaP `9.3489` edge `0.0113` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.2546` n `142` status `ready` deltaP `11.1216` edge `0.0324` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2403` n `142` status `ready` deltaP `3.3377` edge `0.0752` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4714` n `142` status `ready` deltaP `1.4632` edge `0.0139` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2028` n `142` status `ready` deltaP `-6.3251` edge `0.0374` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.2834` n `142` status `ready` deltaP `9.4362` edge `-0.0061` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.3387` n `142` status `ready` deltaP `-3.0059` edge `0.1199` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.7942` n `142` status `ready` deltaP `-8.6953` edge `-0.0035` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8752` n `142` status `ready` deltaP `-9.4543` edge `-0.0099` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3483` n `142` status `ready` deltaP `-9.7647` edge `0.0059` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
