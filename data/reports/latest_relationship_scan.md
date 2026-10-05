# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T03:22:30.677553+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5368`

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

- `market_context_high->unknown_1h` score `115.0647` n `100` status `ready` deltaP `-0.8862` edge `9.6361` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `71.5948` n `95` status `ready` deltaP `2.4743` edge `5.9809` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `11.1` n `57` status `ready` deltaP `30.1535` edge `0.7376` maxDD `-0.423`
- `market_context_high->crypto_alt_24h` score `9.7347` n `57` status `ready` deltaP `25.3929` edge `0.7039` maxDD `-2.9571`
- `news_risk_high->crypto_major_4h` score `9.3333` n `65` status `ready` deltaP `32.3992` edge `0.5821` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.153` n `65` status `ready` deltaP `20.2439` edge `0.5122` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.3444` n `65` status `ready` deltaP `15.5476` edge `0.2684` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.226` n `95` status `ready` deltaP `17.9862` edge `0.3026` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.3961` n `65` status `ready` deltaP `23.6111` edge `0.1256` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8877` n `65` status `ready` deltaP `31.7613` edge `0.0551` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.7634` n `65` status `ready` deltaP `20.7293` edge `0.1531` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.5228` n `65` status `ready` deltaP `10.1658` edge `0.178` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0734` n `65` status `ready` deltaP `25.6172` edge `0.017` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `2.0299` n `65` status `ready` deltaP `18.621` edge `0.0866` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `1.9882` n `100` status `ready` deltaP `14.012` edge `0.1173` maxDD `-2.2692`
- `market_context_high->fx_24h` score `1.5088` n `57` status `ready` deltaP `19.2983` edge `0.0892` maxDD `-1.703`
- `market_context_high->fx_4h` score `1.5001` n `95` status `ready` deltaP `25.7815` edge `0.0288` maxDD `-0.3868`
- `market_context_high->equity_24h` score `1.4577` n `57` status `ready` deltaP `4.1575` edge `0.114` maxDD `-0.6196`
- `news_risk_high->crypto_alt_1h` score `1.2656` n `65` status `ready` deltaP `3.9705` edge `0.1309` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.0328` n `95` status `ready` deltaP `3.4018` edge `0.2423` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
