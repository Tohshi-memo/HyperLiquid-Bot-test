# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T10:22:27.403636+00:00`
- Price records: `672`
- Market context records: `6077`
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

- `news_risk_high->fx_24h` score `8.1618` n `30` status `ready` deltaP `72.7431` edge `0.1952` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `4.5486` n `30` status `ready` deltaP `30.6597` edge `0.1894` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.3699` n `31` status `ready` deltaP `45.3531` edge `0.0664` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.471` n `32` status `ready` deltaP `29.6407` edge `0.0222` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.7419` n `206` status `ready` deltaP `9.2514` edge `0.1752` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.1778` n `32` status `ready` deltaP `13.6789` edge `0.1065` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `0.952` n `30` status `ready` deltaP `19.8264` edge `-0.0323` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.6556` n `32` status `ready` deltaP `9.2253` edge `0.0687` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0984` n `30` status `ready` deltaP `9.2361` edge `0.0382` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3464` n `206` status `ready` deltaP `3.8791` edge `0.0096` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.4959` n `206` status `ready` deltaP `0.7572` edge `-0.0007` maxDD `-0.6538`
- `market_context_high->metal_4h` score `-0.7065` n `206` status `ready` deltaP `5.0956` edge `0.0259` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7427` n `32` status `ready` deltaP `-1.9461` edge `-0.0325` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7612` n `206` status `ready` deltaP `4.7047` edge `0.0463` maxDD `-9.3536`
- `market_context_high->commodity_1h` score `-0.7902` n `206` status `ready` deltaP `-2.2818` edge `-0.006` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.809` n `206` status `ready` deltaP `4.85` edge `0.0407` maxDD `-9.807`
- `market_context_high->equity_1h` score `-0.8107` n `206` status `ready` deltaP `1.9781` edge `0.0321` maxDD `-4.3608`
- `market_context_high->index_4h` score `-0.8857` n `206` status `ready` deltaP `2.2629` edge `0.0247` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-0.9489` n `32` status `ready` deltaP `-7.4289` edge `-0.0158` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1768` n `206` status `ready` deltaP `-1.9374` edge `0.0047` maxDD `-1.1879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
