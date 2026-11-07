# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T03:07:26.459012+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `1.0418` n `68` status `ready` deltaP `8.42` edge `0.1555` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7277` n `68` status `ready` deltaP `13.0829` edge `0.0212` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.2809` n `68` status `ready` deltaP `8.6295` edge `0.1453` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0331` n `68` status `ready` deltaP `6.9567` edge `0.0032` maxDD `-0.2931`
- `news_risk_high->fx_24h` score `-0.1229` n `68` status `ready` deltaP `-3.0126` edge `0.0541` maxDD `-0.2073`
- `news_risk_high->fx_4h` score `-0.1447` n `68` status `ready` deltaP `3.3806` edge `0.0035` maxDD `-0.2336`
- `news_risk_high->equity_1h` score `-0.1946` n `68` status `ready` deltaP `-2.2191` edge `0.0448` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.2928` n `68` status `ready` deltaP `-0.0792` edge `0.0016` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.4939` n `68` status `ready` deltaP `-3.1173` edge `-0.0068` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.2418` n `68` status `ready` deltaP `-4.2234` edge `-0.0405` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.6953` n `68` status `ready` deltaP `-6.9942` edge `-0.0103` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-2.1289` n `68` status `ready` deltaP `-14.2832` edge `-0.0036` maxDD `-1.2868`
- `news_risk_high->crypto_major_1h` score `-2.3453` n `68` status `ready` deltaP `-9.5192` edge `-0.0381` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-2.5151` n `68` status `ready` deltaP `-5.8295` edge `-0.0532` maxDD `-5.4024`
- `news_risk_high->crypto_alt_4h` score `-2.812` n `68` status `ready` deltaP `-7.4515` edge `-0.0488` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.5017` n `68` status `ready` deltaP `-2.3897` edge `-0.2434` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-3.7515` n `68` status `ready` deltaP `23.366` edge `0.5219` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.6127` n `68` status `ready` deltaP `-31.9942` edge `-0.0113` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-10.3357` n `68` status `ready` deltaP `-29.5343` edge `-0.0965` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.424` n `68` status `ready` deltaP `-29.136` edge `-0.0741` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
