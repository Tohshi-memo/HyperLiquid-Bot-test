# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T03:37:27.830398+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4160`

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

- `news_risk_high->equity_4h` score `1.0228` n `68` status `ready` deltaP `8.1151` edge `0.1551` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7009` n `68` status `ready` deltaP `12.778` edge `0.021` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.2566` n `68` status `ready` deltaP `8.2823` edge `0.1445` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0253` n `68` status `ready` deltaP `6.807` edge `0.0032` maxDD `-0.2931`
- `news_risk_high->fx_24h` score `-0.0915` n `68` status `ready` deltaP `-2.6654` edge `0.0544` maxDD `-0.2073`
- `news_risk_high->fx_4h` score `-0.1447` n `68` status `ready` deltaP `3.3806` edge `0.0035` maxDD `-0.2336`
- `news_risk_high->equity_1h` score `-0.1938` n `68` status `ready` deltaP `-2.2191` edge `0.0449` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.2928` n `68` status `ready` deltaP `-0.0792` edge `0.0016` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.4939` n `68` status `ready` deltaP `-3.1173` edge `-0.0068` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.2418` n `68` status `ready` deltaP `-4.2234` edge `-0.0405` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.7142` n `68` status `ready` deltaP `-7.1467` edge `-0.0117` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-2.1277` n `68` status `ready` deltaP `-14.2832` edge `-0.0035` maxDD `-1.2868`
- `news_risk_high->crypto_major_1h` score `-2.3369` n `68` status `ready` deltaP `-9.5192` edge `-0.0374` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-2.4887` n `68` status `ready` deltaP `-5.6798` edge `-0.052` maxDD `-5.4024`
- `news_risk_high->crypto_alt_4h` score `-2.819` n `68` status `ready` deltaP `-7.4515` edge `-0.0497` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.5056` n `68` status `ready` deltaP `-2.3897` edge `-0.2439` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-3.7804` n `68` status `ready` deltaP `23.366` edge `0.5182` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.5969` n `68` status `ready` deltaP `-31.8418` edge `-0.011` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-10.3297` n `68` status `ready` deltaP `-29.5343` edge `-0.096` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.4384` n `68` status `ready` deltaP `-29.136` edge `-0.0753` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
