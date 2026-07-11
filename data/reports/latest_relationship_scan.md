# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T21:37:26.438241+00:00`
- Price records: `672`
- Market context records: `6432`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.8531` n `32` status `ready` deltaP `30.5556` edge `0.7988` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.1548` n `146` status `ready` deltaP `20.8191` edge `0.8708` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.5055` n `32` status `ready` deltaP `54.5139` edge `0.1787` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1218` n `32` status `ready` deltaP `42.9116` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1113` n `32` status `ready` deltaP `35.2431` edge `0.1282` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.3498` n `32` status `ready` deltaP `12.1528` edge `0.4264` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.459` n `32` status `ready` deltaP `29.6407` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4625` n `32` status `ready` deltaP `13.6789` edge `0.143` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.2109` n `195` status `ready` deltaP `-5.5788` edge `0.2282` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8263` n `32` status `ready` deltaP `9.6744` edge `0.0876` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.1312` n `192` status `ready` deltaP `8.3207` edge `0.0231` maxDD `-0.4108`
- `market_context_high->metal_4h` score `0.0472` n `192` status `ready` deltaP `8.9177` edge `0.0408` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.219` n `32` status `ready` deltaP `7.1295` edge `-0.0313` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.4376` n `146` status `ready` deltaP `16.0411` edge `0.0938` maxDD `-11.8809`
- `market_context_high->unknown_4h` score `-0.4881` n `192` status `ready` deltaP `-14.596` edge `0.2972` maxDD `-10.5788`
- `market_context_high->metal_1h` score `-0.5517` n `195` status `ready` deltaP `0.7692` edge `0.0019` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.5799` n `32` status `ready` deltaP `0.0` edge `-0.0246` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.6044` n `195` status `ready` deltaP `-1.0909` edge `-0.0019` maxDD `-2.1314`
- `market_context_high->equity_4h` score `-0.6284` n `192` status `ready` deltaP `6.4533` edge `0.0463` maxDD `-8.2573`
- `market_context_high->index_1h` score `-0.6746` n `195` status `ready` deltaP `-2.6294` edge `0.003` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
