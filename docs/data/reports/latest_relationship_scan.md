# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T23:38:06.229079+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9940`

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

- `market_context_high->unknown_4h` score `27.376` n `57` status `ready` deltaP `2.3588` edge `2.2806` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `11.6759` n `101` status `ready` deltaP `0.6789` edge `1.6543` maxDD `-46.1999`
- `market_context_high->crypto_major_24h` score `7.7768` n `51` status `ready` deltaP `4.8917` edge `1.2261` maxDD `-44.5185`
- `news_risk_high->crypto_alt_24h` score `7.0283` n `101` status `ready` deltaP `1.064` edge `1.0667` maxDD `-32.7147`
- `market_context_high->equity_24h` score `4.1719` n `51` status `ready` deltaP `-1.8791` edge `0.6192` maxDD `-16.3877`
- `news_risk_high->crypto_alt_4h` score `3.208` n `101` status `ready` deltaP `15.5654` edge `0.2845` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.442` n `101` status `ready` deltaP `30.4885` edge `0.2404` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.3817` n `101` status `ready` deltaP `14.5847` edge `0.1478` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.2298` n `101` status `ready` deltaP `16.7849` edge `0.1997` maxDD `-8.0625`
- `market_context_high->index_24h` score `1.976` n `51` status `ready` deltaP `2.114` edge `0.2243` maxDD `-1.5646`
- `news_risk_high->crypto_major_1h` score `1.6132` n `101` status `ready` deltaP `15.932` edge `0.0805` maxDD `-2.8494`
- `market_context_high->equity_1h` score `0.5198` n `57` status `ready` deltaP `3.5771` edge `0.0448` maxDD `-0.36`
- `news_risk_high->fx_4h` score `0.4692` n `101` status `ready` deltaP `11.3846` edge `0.0268` maxDD `-0.421`
- `news_risk_high->metal_1h` score `0.4388` n `101` status `ready` deltaP `12.8016` edge `0.0114` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.434` n `57` status `ready` deltaP `7.577` edge `0.0112` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4247` n `57` status `ready` deltaP `9.7568` edge `0.006` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.2623` n `57` status `ready` deltaP `5.3498` edge `0.017` maxDD `-0.1314`
- `market_context_high->metal_24h` score `0.2533` n `51` status `ready` deltaP `17.0241` edge `-0.069` maxDD `-0.2042`
- `news_risk_high->metal_4h` score `0.1967` n `101` status `ready` deltaP `13.4403` edge `0.0322` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.0707` n `57` status `ready` deltaP `10.882` edge `0.0002` maxDD `-1.0949`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
