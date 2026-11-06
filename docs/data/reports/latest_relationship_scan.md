# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T21:22:34.040589+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4066`

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

- `news_risk_high->equity_4h` score `1.5358` n `85` status `ready` deltaP `13.42` edge `0.198` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7282` n `85` status `ready` deltaP `13.2245` edge `0.0203` maxDD `-0.4888`
- `news_risk_high->index_1h` score `0.3592` n `85` status `ready` deltaP `12.9729` edge `0.0049` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `0.2376` n `85` status `ready` deltaP `4.2462` edge `0.0571` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.0535` n `85` status `ready` deltaP `5.4501` edge `0.0014` maxDD `-0.2336`
- `news_risk_high->index_24h` score `-0.261` n `85` status `ready` deltaP `-0.4017` edge `0.1402` maxDD `-6.6786`
- `news_risk_high->metal_1h` score `-0.2805` n `85` status `ready` deltaP `0.5671` edge `-0.004` maxDD `-0.5256`
- `news_risk_high->fx_1h` score `-0.3159` n `85` status `ready` deltaP `-0.074` edge `-0.0002` maxDD `-0.1846`
- `news_risk_high->fx_24h` score `-0.5383` n `85` status `ready` deltaP `-4.245` edge `0.0277` maxDD `-0.2073`
- `news_risk_high->crypto_alt_1h` score `-0.6746` n `85` status `ready` deltaP `2.684` edge `0.0184` maxDD `-5.8225`
- `news_risk_high->crypto_major_4h` score `-0.7732` n `85` status `ready` deltaP `-0.1973` edge `0.0708` maxDD `-9.1553`
- `news_risk_high->crypto_major_1h` score `-0.8269` n `85` status `ready` deltaP `-2.5995` edge `0.0052` maxDD `-4.1772`
- `news_risk_high->metal_4h` score `-1.0609` n `85` status `ready` deltaP `-1.6751` edge `-0.0343` maxDD `-1.5773`
- `news_risk_high->equity_24h` score `-1.5708` n `85` status `ready` deltaP `25.8375` edge `0.785` maxDD `-86.0244`
- `news_risk_high->crypto_alt_4h` score `-1.9934` n `85` status `ready` deltaP `-3.8127` edge `0.0335` maxDD `-14.0916`
- `news_risk_high->commodity_1h` score `-2.8056` n `85` status `ready` deltaP `-16.6309` edge `-0.0052` maxDD `-1.7518`
- `news_risk_high->metal_24h` score `-2.9686` n `85` status `ready` deltaP `4.0371` edge `-0.2179` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.0594` n `85` status `ready` deltaP `-26.1227` edge `-0.0015` maxDD `-4.3442`
- `news_risk_high->crypto_major_24h` score `-7.32` n `85` status `ready` deltaP `-21.5313` edge `0.0554` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.2661` n `85` status `ready` deltaP `-25.9068` edge `-0.0225` maxDD `-28.8239`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
