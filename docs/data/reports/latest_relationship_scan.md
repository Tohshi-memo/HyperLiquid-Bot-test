# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T03:52:25.407116+00:00`
- Price records: `672`
- Market context records: `6048`
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

- `news_risk_high->fx_24h` score `8.0096` n `30` status `ready` deltaP `71.875` edge `0.1883` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2211` n `30` status `ready` deltaP `43.6585` edge `0.0653` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2969` n `30` status `ready` deltaP `27.5249` edge `0.0218` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `2.1555` n `30` status `ready` deltaP `24.3403` edge `0.0379` maxDD `-0.3101`
- `news_risk_high->crypto_alt_24h` score `1.4707` n `30` status `ready` deltaP `26.1458` edge `-0.037` maxDD `-0.5131`
- `market_context_high->equity_4h` score `1.3661` n `206` status `ready` deltaP `8.1843` edge `0.151` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.0141` n `30` status `ready` deltaP `11.3872` edge `0.1008` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.4032` n `30` status `ready` deltaP `6.517` edge `0.0544` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1226` n `30` status `ready` deltaP `9.2361` edge `0.0413` maxDD `-2.3058`
- `market_context_high->equity_24h` score `-0.1564` n `188` status `ready` deltaP `26.5071` edge `0.5205` maxDD `-42.715`
- `market_context_high->metal_1h` score `-0.461` n `206` status `ready` deltaP `2.8312` edge `0.0019` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4974` n `30` status `ready` deltaP `0.3393` edge `-0.0294` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.5354` n `206` status `ready` deltaP `0.3081` edge `-0.001` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6894` n `206` status `ready` deltaP `-1.8327` edge `-0.0006` maxDD `-0.5708`
- `market_context_high->crypto_alt_1h` score `-0.8033` n `206` status `ready` deltaP `4.7047` edge `0.0409` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8036` n `206` status `ready` deltaP `4.85` edge `0.0414` maxDD `-9.807`
- `market_context_high->index_24h` score `-0.9577` n `188` status `ready` deltaP `3.2432` edge `0.0686` maxDD `-5.6021`
- `market_context_high->index_4h` score `-1.0271` n `206` status `ready` deltaP `1.0434` edge `0.0147` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.047` n `30` status `ready` deltaP `-9.4012` edge `-0.0201` maxDD `-1.1161`
- `market_context_high->equity_1h` score `-1.0925` n `206` status `ready` deltaP `0.6308` edge `0.0176` maxDD `-4.3608`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
