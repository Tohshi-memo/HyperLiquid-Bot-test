# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T04:07:25.782935+00:00`
- Price records: `672`
- Market context records: `5944`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `6.8221` n `30` status `ready` deltaP `62.3264` edge `0.153` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.4764` n `30` status `ready` deltaP `39.2709` edge `0.2151` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.7165` n `30` status `ready` deltaP `38.4756` edge `0.0578` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1052` n `30` status `ready` deltaP `25.4291` edge `0.0198` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5603` n `221` status `ready` deltaP `10.5852` edge `0.1689` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.9081` n `30` status `ready` deltaP `11.0878` edge `0.0892` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2543` n `30` status `ready` deltaP `5.7685` edge `0.0403` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1257` n `226` status `ready` deltaP `5.8489` edge `0.0369` maxDD `-4.3608`
- `news_risk_high->index_24h` score `-0.2256` n `30` status `ready` deltaP `6.9791` edge `0.0117` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3383` n `226` status `ready` deltaP `3.3769` edge `0.0012` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.3861` n `30` status `ready` deltaP `2.2854` edge `-0.0281` maxDD `-1.2643`
- `market_context_high->index_1h` score `-0.5662` n `226` status `ready` deltaP `1.3341` edge `0.0052` maxDD `-0.9342`
- `market_context_high->commodity_1h` score `-0.6229` n `226` status `ready` deltaP `-3.6763` edge `-0.0038` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.815` n `226` status `ready` deltaP `-2.329` edge `-0.0014` maxDD `-0.7459`
- `market_context_high->crypto_major_1h` score `-0.8841` n `226` status `ready` deltaP `2.6218` edge `0.0248` maxDD `-8.1166`
- `market_context_high->crypto_alt_1h` score `-0.8897` n `226` status `ready` deltaP `2.1991` edge `0.0216` maxDD `-8.0256`
- `market_context_high->equity_24h` score `-0.9514` n `213` status `ready` deltaP `18.5324` edge `0.2621` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0563` n `30` status `ready` deltaP `-9.5509` edge `-0.0203` maxDD `-1.1161`
- `market_context_high->metal_4h` score `-1.6432` n `221` status `ready` deltaP `-2.5562` edge `-0.0304` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.6826` n `221` status `ready` deltaP `1.3974` edge `0.0192` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
