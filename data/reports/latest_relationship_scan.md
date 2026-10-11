# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T23:22:29.022922+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9132`

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

- `market_context_high->unknown_24h` score `1419.7617` n `40` status `ready` deltaP `-22.5694` edge `118.5003` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `43.7918` n `102` status `ready` deltaP `-6.0198` edge `3.7475` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.808` n `40` status `ready` deltaP `27.6736` edge `0.5924` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4216` n `40` status `ready` deltaP `52.4306` edge `0.1856` maxDD `0.0`
- `market_context_high->unknown_1h` score `3.1436` n `114` status `ready` deltaP `-3.1962` edge `0.3169` maxDD `-1.0231`
- `market_context_high->fx_24h` score `2.9886` n `40` status `ready` deltaP `33.9931` edge `0.0354` maxDD `-0.0374`
- `risk_on_high->crypto_alt_1h` score `2.121` n `35` status `ready` deltaP `13.6313` edge `0.1414` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `2.121` n `35` status `ready` deltaP `13.6313` edge `0.1414` maxDD `-2.4421`
- `risk_on_high->commodity_1h` score `1.7353` n `35` status `ready` deltaP `22.0531` edge `0.0119` maxDD `-0.1449`
- `risk_on_and_context->commodity_1h` score `1.7353` n `35` status `ready` deltaP `22.0531` edge `0.0119` maxDD `-0.1449`
- `market_context_high->crypto_major_24h` score `1.3708` n `40` status `ready` deltaP `-21.1111` edge `0.5698` maxDD `-17.8526`
- `market_context_high->commodity_4h` score `0.6008` n `102` status `ready` deltaP `12.9453` edge `0.0171` maxDD `-1.6002`
- `risk_on_high->crypto_major_1h` score `0.5649` n `35` status `ready` deltaP `7.1429` edge `0.0901` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.5649` n `35` status `ready` deltaP `7.1429` edge `0.0901` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `0.5049` n `35` status `ready` deltaP `10.7613` edge `0.0169` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `0.5049` n `35` status `ready` deltaP `10.7613` edge `0.0169` maxDD `-0.2466`
- `market_context_high->commodity_1h` score `0.3021` n `114` status `ready` deltaP `7.1909` edge `0.0056` maxDD `-0.6025`
- `market_context_high->crypto_alt_1h` score `0.1983` n `114` status `ready` deltaP `5.5862` edge `0.0916` maxDD `-4.9401`
- `market_context_high->fx_4h` score `0.1332` n `102` status `ready` deltaP `8.4768` edge `0.0056` maxDD `-0.2692`
- `risk_on_high->fx_1h` score `-0.0222` n `35` status `ready` deltaP `5.0599` edge `-0.0012` maxDD `-0.164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
