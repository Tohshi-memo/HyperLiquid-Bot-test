# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T16:37:28.694511+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12636`

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

- `market_context_high->unknown_24h` score `6947.2924` n `89` status `ready` deltaP `13.2042` edge `578.8582` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `4937.4445` n `44` status `ready` deltaP `15.4514` edge `411.3507` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `4937.4445` n `44` status `ready` deltaP `15.4514` edge `411.3507` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.0055` n `82` status `ready` deltaP `-5.2505` edge `31.9943` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `22.8877` n `63` status `ready` deltaP `50.8433` edge `1.6584` maxDD `-5.8705`
- `news_risk_high->crypto_alt_24h` score `17.0442` n `63` status `ready` deltaP `27.9514` edge `1.2828` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `16.8162` n `44` status `ready` deltaP `38.81` edge `1.1656` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.8162` n `44` status `ready` deltaP `38.81` edge `1.1656` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.0` n `89` status `ready` deltaP `32.1961` edge `1.1181` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `11.1555` n `63` status `ready` deltaP `30.5804` edge `0.7592` maxDD `-1.3422`
- `risk_on_high->equity_24h` score `9.5143` n `44` status `ready` deltaP `40.1042` edge `0.5255` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.5143` n `44` status `ready` deltaP `40.1042` edge `0.5255` maxDD `0.0`
- `market_context_high->equity_24h` score `9.1315` n `89` status `ready` deltaP `40.1042` edge `0.4936` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.5216` n `44` status `ready` deltaP `41.505` edge `0.4706` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.5216` n `44` status `ready` deltaP `41.505` edge `0.4706` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `7.5331` n `63` status `ready` deltaP `48.1647` edge `0.3269` maxDD `-0.2858`
- `news_risk_high->index_24h` score `7.3744` n `63` status `ready` deltaP `48.1399` edge `0.3071` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8715` n `44` status `ready` deltaP `49.2582` edge `0.0818` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8715` n `44` status `ready` deltaP `49.2582` edge `0.0818` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1316` n `44` status `ready` deltaP `36.1835` edge `0.1124` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
