# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T20:22:27.518586+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4184`

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

- `news_risk_high->equity_4h` score `1.7304` n `89` status `ready` deltaP `14.8071` edge `0.2137` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.8202` n `89` status `ready` deltaP `14.2539` edge `0.0211` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.3406` n `89` status `ready` deltaP `5.1319` edge `0.0644` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.2747` n `89` status `ready` deltaP `11.347` edge `0.0049` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `-0.1978` n `89` status `ready` deltaP `2.8998` edge `-0.0001` maxDD `-0.2337`
- `news_risk_high->metal_1h` score `-0.329` n `89` status `ready` deltaP `-0.1867` edge `-0.0052` maxDD `-0.5256`
- `news_risk_high->fx_1h` score `-0.3677` n `89` status `ready` deltaP `-1.0832` edge `-0.0001` maxDD `-0.1858`
- `news_risk_high->crypto_major_4h` score `-0.5088` n `89` status `ready` deltaP `1.5723` edge `0.0929` maxDD `-9.1553`
- `news_risk_high->index_24h` score `-0.6086` n `89` status `ready` deltaP `-1.0846` edge `0.14` maxDD `-6.6786`
- `news_risk_high->crypto_alt_1h` score `-0.6284` n `89` status `ready` deltaP `2.6576` edge `0.0245` maxDD `-5.8225`
- `news_risk_high->crypto_major_1h` score `-0.809` n `89` status `ready` deltaP `-2.5113` edge `0.0069` maxDD `-4.1772`
- `news_risk_high->fx_24h` score `-0.8587` n `89` status `ready` deltaP `-7.3647` edge `0.0218` maxDD `-0.2073`
- `news_risk_high->metal_4h` score `-1.0012` n `89` status `ready` deltaP `-0.7365` edge `-0.0329` maxDD `-1.5773`
- `news_risk_high->equity_24h` score `-1.0275` n `89` status `ready` deltaP `27.1065` edge `0.8462` maxDD `-86.0244`
- `news_risk_high->crypto_alt_4h` score `-1.4439` n `89` status `ready` deltaP `-1.9903` edge `0.0918` maxDD `-14.0916`
- `news_risk_high->metal_24h` score `-2.9451` n `89` status `ready` deltaP `3.8888` edge `-0.2139` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.0322` n `89` status `ready` deltaP `-18.1642` edge `-0.0093` maxDD `-2.1165`
- `news_risk_high->commodity_4h` score `-4.1886` n `89` status `ready` deltaP `-26.5176` edge `-0.0033` maxDD `-4.8507`
- `news_risk_high->crypto_major_24h` score `-6.9109` n `89` status `ready` deltaP `-18.6143` edge `0.0884` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.2922` n `89` status `ready` deltaP `-25.5837` edge `-0.0153` maxDD `-29.7458`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
