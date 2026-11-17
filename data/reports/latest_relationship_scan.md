# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T21:37:40.539578+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4053`

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

- `market_context_high->unknown_24h` score `1490.9598` n `98` status `ready` deltaP `3.4722` edge `124.2235` maxDD `0.0`
- `news_risk_high->equity_24h` score `49.286` n `31` status `ready` deltaP `64.4994` edge `3.7478` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `20.53` n `31` status `ready` deltaP `55.6402` edge `1.3399` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.5042` n `98` status `ready` deltaP `46.5384` edge `2.0045` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.6385` n `98` status `ready` deltaP `32.7735` edge `1.8706` maxDD `-13.3222`
- `news_risk_high->crypto_major_24h` score `14.2725` n `31` status `ready` deltaP `23.6615` edge `1.7864` maxDD `-6.8139`
- `news_risk_high->index_24h` score `8.2672` n `31` status `ready` deltaP `55.9924` edge `0.346` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.5161` n `31` status `ready` deltaP `54.8611` edge `0.2606` maxDD `0.0`
- `news_risk_high->metal_4h` score `7.0755` n `31` status `ready` deltaP `55.9205` edge `0.2213` maxDD `-0.0246`
- `news_risk_high->equity_1h` score `5.776` n `31` status `ready` deltaP `26.8881` edge `0.3239` maxDD `-0.4122`
- `news_risk_high->crypto_alt_24h` score `5.2826` n `31` status `ready` deltaP `1.6017` edge `0.8801` maxDD `-29.0448`
- `news_risk_high->crypto_major_4h` score `4.6874` n `31` status `ready` deltaP `19.2171` edge `0.3052` maxDD `-1.7491`
- `news_risk_high->crypto_alt_4h` score `4.5999` n `31` status `ready` deltaP `29.047` edge `0.4728` maxDD `-4.137`
- `news_risk_high->index_4h` score `4.2425` n `31` status `ready` deltaP `34.9381` edge `0.1431` maxDD `-0.1319`
- `news_risk_high->metal_1h` score `2.5631` n `31` status `ready` deltaP `26.8881` edge `0.0561` maxDD `-0.0743`
- `news_risk_high->crypto_major_1h` score `2.3498` n `31` status `ready` deltaP `16.1628` edge `0.1232` maxDD `-1.4777`
- `news_risk_high->crypto_alt_1h` score `1.8117` n `31` status `ready` deltaP `20.4365` edge `0.1487` maxDD `-2.5469`
- `news_risk_high->index_1h` score `1.7996` n `31` status `ready` deltaP `20.8856` edge `0.0325` maxDD `-0.0751`
- `news_risk_high->commodity_4h` score `1.6449` n `31` status `ready` deltaP `27.0898` edge `0.0513` maxDD `-0.3479`
- `market_context_high->metal_1h` score `-0.4758` n `98` status `ready` deltaP `-0.3666` edge `0.0016` maxDD `-2.1461`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
