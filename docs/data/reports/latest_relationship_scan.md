# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T12:07:25.087469+00:00`
- Price records: `672`
- Market context records: `6085`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11147`

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

- `news_risk_high->fx_24h` score `8.1594` n `30` status `ready` deltaP `72.7431` edge `0.195` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.6406` n `30` status `ready` deltaP `31.875` edge `0.2723` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.3017` n `32` status `ready` deltaP `44.7409` edge `0.0648` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4195` n `32` status `ready` deltaP `29.0419` edge `0.0219` maxDD `-0.1113`
- `market_context_high->equity_4h` score `2.0311` n `201` status `ready` deltaP `10.3916` edge `0.1917` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.1084` n `32` status `ready` deltaP `12.9304` edge `0.1026` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `0.5944` n `30` status `ready` deltaP `18.6111` edge `-0.054` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.5878` n `32` status `ready` deltaP `8.6265` edge `0.064` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1023` n `30` status `ready` deltaP `9.2361` edge `0.0387` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.2868` n `201` status `ready` deltaP `4.7703` edge `0.0113` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.434` n `201` status `ready` deltaP `1.3056` edge `-0.0003` maxDD `-0.5659`
- `market_context_high->equity_1h` score `-0.4404` n `201` status `ready` deltaP `2.5337` edge `0.0382` maxDD `-4.2573`
- `market_context_high->metal_4h` score `-0.6482` n `201` status `ready` deltaP `5.2087` edge `0.03` maxDD `-3.4996`
- `market_context_high->index_4h` score `-0.7203` n `201` status `ready` deltaP `3.6274` edge `0.0299` maxDD `-1.381`
- `market_context_high->commodity_1h` score `-0.7293` n `201` status `ready` deltaP `-1.7458` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7334` n `32` status `ready` deltaP `-1.9461` edge `-0.0313` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7371` n `201` status `ready` deltaP `4.9729` edge `0.0476` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.7886` n `201` status `ready` deltaP `5.0168` edge `0.0422` maxDD `-9.807`
- `news_risk_high->index_1h` score `-0.9971` n `32` status `ready` deltaP `-8.1774` edge `-0.017` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1085` n `201` status `ready` deltaP `-1.5387` edge `0.0048` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
