# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T01:07:24.534592+00:00`
- Price records: `672`
- Market context records: `6037`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11125`

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

- `news_risk_high->fx_24h` score `7.9724` n `30` status `ready` deltaP `71.875` edge `0.1852` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2771` n `30` status `ready` deltaP `44.2683` edge `0.0659` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.6527` n `30` status `ready` deltaP `26.25` edge `0.0666` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2693` n `30` status `ready` deltaP `27.2255` edge `0.0215` maxDD `-0.1113`
- `market_context_high->equity_24h` score `1.7372` n `180` status `ready` deltaP `29.7223` edge `0.5697` maxDD `-31.6107`
- `market_context_high->equity_4h` score `1.5937` n `206` status `ready` deltaP `8.7941` edge `0.1659` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `0.8395` n `30` status `ready` deltaP `10.3393` edge `0.0854` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2146` n `30` status `ready` deltaP `5.4691` edge `0.0372` maxDD `-1.6923`
- `news_risk_high->crypto_alt_24h` score `0.1767` n `30` status `ready` deltaP `24.2361` edge `-0.1321` maxDD `-0.5131`
- `news_risk_high->index_24h` score `0.1351` n `30` status `ready` deltaP `9.2361` edge `0.0429` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4236` n `206` status `ready` deltaP `3.2803` edge `0.0037` maxDD `-2.0564`
- `market_context_high->index_24h` score `-0.4444` n `180` status `ready` deltaP `5.3472` edge `0.0774` maxDD `-5.6021`
- `news_risk_high->metal_1h` score `-0.4601` n `30` status `ready` deltaP `0.7884` edge `-0.0276` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.563` n `206` status `ready` deltaP `0.0087` edge `-0.0013` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6775` n `206` status `ready` deltaP `-1.683` edge `-0.0006` maxDD `-0.5708`
- `market_context_high->index_4h` score `-0.9663` n `206` status `ready` deltaP `1.9581` edge `0.0164` maxDD `-1.9335`
- `market_context_high->metal_4h` score `-0.9709` n `206` status `ready` deltaP `4.7907` edge `0.0059` maxDD `-3.4996`
- `market_context_high->crypto_major_1h` score `-0.9782` n `206` status `ready` deltaP `3.8021` edge `0.026` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.992` n `206` status `ready` deltaP `3.6568` edge `0.0237` maxDD `-9.3536`
- `news_risk_high->index_1h` score `-1.0657` n `30` status `ready` deltaP `-9.7006` edge `-0.0205` maxDD `-1.1161`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
