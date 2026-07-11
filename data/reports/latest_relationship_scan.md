# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T16:07:27.883105+00:00`
- Price records: `672`
- Market context records: `6407`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11094`

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

- `news_risk_high->crypto_alt_24h` score `13.2866` n `32` status `ready` deltaP `34.375` edge `0.8928` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6883` n `32` status `ready` deltaP `56.4236` edge `0.1812` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.2464` n `32` status `ready` deltaP `36.6319` edge `0.1302` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1399` n `32` status `ready` deltaP `43.064` edge `0.0625` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0156` n `32` status `ready` deltaP `15.9722` edge `0.4863` maxDD `-4.2368`
- `market_context_high->unknown_24h` score `3.3875` n `146` status `ready` deltaP `10.5927` edge `0.5417` maxDD `-15.0689`
- `news_risk_high->fx_1h` score `2.447` n `32` status `ready` deltaP `29.491` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4554` n `32` status `ready` deltaP `13.9783` edge `0.1401` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8403` n `32` status `ready` deltaP `10.2732` edge `0.0854` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.5538` n `211` status `ready` deltaP `-5.7503` edge `0.1853` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3853` n `211` status `ready` deltaP `11.2538` edge `0.0409` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0361` n `211` status `ready` deltaP `7.3568` edge `0.0216` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2836` n `32` status `ready` deltaP `6.2313` edge `-0.0307` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3834` n `146` status `ready` deltaP `19.1091` edge `0.0975` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4736` n `211` status `ready` deltaP `2.1824` edge `0.0025` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.629` n `32` status `ready` deltaP `-0.8982` edge `-0.0249` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.6608` n `211` status `ready` deltaP `-0.0114` edge `-0.0016` maxDD `-0.9376`
- `market_context_high->commodity_1h` score `-0.7128` n `211` status `ready` deltaP `-3.0557` edge `-0.0027` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7211` n `211` status `ready` deltaP `-3.48` edge `0.0027` maxDD `-0.7564`
- `news_risk_high->index_24h` score `-0.7557` n `32` status `ready` deltaP `0.5208` edge `-0.0132` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
