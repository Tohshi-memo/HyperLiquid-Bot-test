# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T21:37:23.187983+00:00`
- Price records: `490`
- Market context records: `583`
- Flow alert records: `1647`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.7098` n `146` status `ready` deltaP `7.1831` edge `0.3494` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0907` n `146` status `ready` deltaP `9.5473` edge `0.2273` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0728` n `146` status `ready` deltaP `11.4107` edge `0.0204` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2754` n `146` status `ready` deltaP `2.6999` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6208` n `146` status `ready` deltaP `1.4722` edge `0.0359` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6703` n `146` status `ready` deltaP `0.378` edge `-0.0031` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1759` n `146` status `ready` deltaP `-4.3886` edge `-0.0084` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2555` n `146` status `ready` deltaP `-1.9042` edge `-0.0109` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.2813` n `146` status `ready` deltaP `4.9186` edge `-0.0081` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.9189` n `146` status `ready` deltaP `4.0334` edge `-0.0145` maxDD `-11.4508`
- `market_context_high->index_24h` score `-2.1086` n `146` status `ready` deltaP `-6.0309` edge `0.064` maxDD `-5.9609`
- `market_context_high->crypto_alt_4h` score `-2.14` n `146` status `ready` deltaP `3.1414` edge `0.0577` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2608` n `146` status `ready` deltaP `0.1749` edge `-0.0373` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.952` n `146` status `ready` deltaP `11.5802` edge `0.0474` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2877` n `146` status `ready` deltaP `-4.4619` edge `-0.0483` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3729` n `146` status `ready` deltaP `-3.6549` edge `-0.0415` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.6008` n `146` status `ready` deltaP `-5.9662` edge `0.0898` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.1127` n `146` status `ready` deltaP `-10.0421` edge `-0.0153` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.5102` n `146` status `ready` deltaP `-4.5662` edge `-0.0306` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.0613` n `146` status `ready` deltaP `1.2513` edge `-0.2423` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
