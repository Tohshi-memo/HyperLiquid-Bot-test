# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T04:37:26.468429+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4178`

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

- `news_risk_high->equity_4h` score `1.0714` n `67` status `ready` deltaP `8.5139` edge `0.1545` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7264` n `67` status `ready` deltaP `13.112` edge `0.0209` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.2668` n `67` status `ready` deltaP `8.5535` edge `0.144` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0364` n `67` status `ready` deltaP `7.0203` edge `0.0032` maxDD `-0.2931`
- `news_risk_high->fx_24h` score `-0.0482` n `67` status `ready` deltaP `-2.4539` edge `0.0566` maxDD `-0.2073`
- `news_risk_high->equity_1h` score `-0.1546` n `67` status `ready` deltaP `-1.4948` edge `0.0451` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.1664` n `67` status `ready` deltaP `2.9623` edge `0.0035` maxDD `-0.2336`
- `news_risk_high->fx_1h` score `-0.3282` n `67` status `ready` deltaP `-0.7597` edge `0.0016` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.4632` n `67` status `ready` deltaP `-2.5427` edge `-0.0067` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.2791` n `67` status `ready` deltaP `-4.9258` edge `-0.0406` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.6487` n `67` status `ready` deltaP `-6.5322` edge `-0.0074` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.9885` n `67` status `ready` deltaP `-13.2854` edge `-0.0029` maxDD `-1.2722`
- `news_risk_high->crypto_major_1h` score `-2.2028` n `67` status `ready` deltaP `-9.0982` edge `-0.0337` maxDD `-3.8037`
- `news_risk_high->crypto_alt_1h` score `-2.4027` n `67` status `ready` deltaP `-5.215` edge `-0.0499` maxDD `-5.2444`
- `news_risk_high->crypto_alt_4h` score `-2.7355` n `67` status `ready` deltaP `-6.837` edge `-0.0431` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.5599` n `67` status `ready` deltaP `-2.9384` edge `-0.2472` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-3.9748` n `67` status `ready` deltaP `22.9271` edge `0.4962` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.5369` n `67` status `ready` deltaP `-31.2955` edge `-0.0103` maxDD `-4.0643`
- `news_risk_high->commodity_24h` score `-10.3631` n `67` status `ready` deltaP `-29.4466` edge `-0.0997` maxDD `-28.0733`
- `news_risk_high->crypto_major_24h` score `-13.574` n `67` status `ready` deltaP `-29.2418` edge `-0.0859` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
