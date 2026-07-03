# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T22:22:25.371376+00:00`
- Price records: `672`
- Market context records: `5600`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11433`

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

- `market_context_high->equity_24h` score `3.5467` n `174` status `ready` deltaP `15.0084` edge `0.7034` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.4246` n `214` status `ready` deltaP `12.8192` edge `0.2625` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.1538` n `174` status `ready` deltaP `20.57` edge `0.0564` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.7387` n `214` status `ready` deltaP `7.9112` edge `0.1729` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.549` n `214` status `ready` deltaP `6.6916` edge `0.165` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.2846` n `226` status `ready` deltaP `6.2517` edge `0.0353` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.3257` n `226` status `ready` deltaP `0.722` edge `0.001` maxDD `-0.472`
- `market_context_high->metal_1h` score `-0.5606` n `226` status `ready` deltaP `-0.7286` edge `0.0005` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5839` n `226` status `ready` deltaP `1.1248` edge `0.04` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.5892` n `226` status `ready` deltaP `4.132` edge `0.0479` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.7888` n `226` status `ready` deltaP `1.0015` edge `0.0061` maxDD `-0.9472`
- `market_context_high->crypto_major_24h` score `-0.8737` n `174` status `ready` deltaP `10.8477` edge `0.3089` maxDD `-29.6555`
- `market_context_high->commodity_1h` score `-1.2047` n `226` status `ready` deltaP `-2.5118` edge `-0.0071` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.4922` n `214` status `ready` deltaP `2.1114` edge `0.008` maxDD `-1.0471`
- `market_context_high->index_4h` score `-1.5786` n `214` status `ready` deltaP `2.4262` edge `0.0132` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.3213` n `174` status `ready` deltaP `10.7819` edge `0.0292` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9235` n `214` status `ready` deltaP `-12.037` edge `-0.0562` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1854` n `214` status `ready` deltaP `-5.5846` edge `-0.044` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.1123` n `174` status `ready` deltaP `-9.0218` edge `-0.2438` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-10.9414` n `174` status `ready` deltaP `0.6346` edge `-0.0463` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
