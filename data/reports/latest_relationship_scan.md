# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T04:27:46.798065+00:00`
- Price records: `672`
- Market context records: `6051`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11127`

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

- `news_risk_high->fx_24h` score `8.0144` n `30` status `ready` deltaP `71.875` edge `0.1887` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2235` n `30` status `ready` deltaP `43.6585` edge `0.0655` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2705` n `30` status `ready` deltaP `27.2255` edge `0.0216` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `2.0617` n `30` status `ready` deltaP `23.9931` edge `0.0324` maxDD `-0.3101`
- `news_risk_high->crypto_alt_24h` score `1.6665` n `30` status `ready` deltaP `26.493` edge `-0.023` maxDD `-0.5131`
- `market_context_high->equity_4h` score `1.3057` n `206` status `ready` deltaP `7.8794` edge `0.148` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.0321` n `30` status `ready` deltaP `11.5369` edge `0.1021` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.4203` n `30` status `ready` deltaP `6.6667` edge `0.0556` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1156` n `30` status `ready` deltaP `9.2361` edge `0.0404` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4695` n `206` status `ready` deltaP `2.6815` edge `0.0018` maxDD `-2.0564`
- `market_context_high->equity_24h` score `-0.5018` n `190` status `ready` deltaP `25.7456` edge `0.5103` maxDD `-44.3687`
- `news_risk_high->metal_1h` score `-0.506` n `30` status `ready` deltaP `0.1896` edge `-0.0295` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.5618` n `206` status `ready` deltaP `0.0087` edge `-0.0012` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6775` n `206` status `ready` deltaP `-1.683` edge `-0.0006` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.7856` n `206` status `ready` deltaP `4.9997` edge `0.0427` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.7862` n `206` status `ready` deltaP `4.8544` edge `0.0421` maxDD `-9.3536`
- `market_context_high->index_4h` score `-1.0366` n `206` status `ready` deltaP `0.891` edge `0.0145` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0368` n `30` status `ready` deltaP `-9.2515` edge `-0.0198` maxDD `-1.1161`
- `market_context_high->index_24h` score `-1.0369` n `190` status `ready` deltaP `2.7449` edge `0.0666` maxDD `-5.7048`
- `market_context_high->equity_1h` score `-1.0877` n `206` status `ready` deltaP `0.6308` edge `0.018` maxDD `-4.3608`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
