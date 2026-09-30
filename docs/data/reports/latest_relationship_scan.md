# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T06:37:32.633741+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7458`

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

- `news_risk_high->unknown_24h` score `1200.4588` n `135` status `ready` deltaP `1.9097` edge `100.0255` maxDD `0.0`
- `market_context_high->unknown_1h` score `769.5536` n `32` status `ready` deltaP `9.7305` edge `64.0646` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.4549` n `135` status `ready` deltaP `28.5532` edge `1.3685` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `8.3648` n `135` status `ready` deltaP `28.5532` edge `0.7416` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.8681` n `135` status `ready` deltaP `23.9931` edge `0.8111` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.8943` n `135` status `ready` deltaP `34.7454` edge `0.1407` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.5541` n `135` status `ready` deltaP `26.9213` edge `0.2441` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.9944` n `135` status `ready` deltaP `29.9333` edge `0.2101` maxDD `-9.143`
- `market_context_high->crypto_alt_1h` score `2.1792` n `32` status `ready` deltaP `12.0509` edge `0.1627` maxDD `-3.5821`
- `news_risk_high->crypto_alt_4h` score `1.941` n `135` status `ready` deltaP `11.4171` edge `0.3516` maxDD `-15.9436`
- `market_context_high->crypto_major_1h` score `1.7122` n `32` status `ready` deltaP `7.4663` edge `0.1539` maxDD `-3.546`
- `market_context_high->fx_1h` score `1.4455` n `32` status `ready` deltaP `20.116` edge `0.0086` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.1377` n `135` status `ready` deltaP `9.5509` edge `0.1222` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9463` n `135` status `ready` deltaP `9.7006` edge `0.0765` maxDD `-1.6514`
- `market_context_high->equity_1h` score `0.7566` n `32` status `ready` deltaP `12.2006` edge `0.0582` maxDD `-2.4027`
- `news_risk_high->index_1h` score `0.546` n `135` status `ready` deltaP `9.4167` edge `0.0115` maxDD `-0.302`
- `market_context_high->metal_1h` score `0.2023` n `32` status `ready` deltaP `4.0419` edge `0.012` maxDD `-0.4338`
- `market_context_high->index_1h` score `0.0524` n `32` status `ready` deltaP `4.0232` edge `0.0136` maxDD `-0.3627`
- `news_risk_high->index_4h` score `-0.087` n `135` status `ready` deltaP `7.4063` edge `0.0287` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.5072` n `135` status `ready` deltaP `2.4894` edge `0.0694` maxDD `-7.2607`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
