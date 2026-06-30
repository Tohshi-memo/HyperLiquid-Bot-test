# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T17:22:33.084443+00:00`
- Price records: `672`
- Market context records: `5269`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9652`

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

- `market_context_high->unknown_24h` score `26.1328` n `149` status `ready` deltaP `29.7341` edge `1.9885` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `9.6669` n `149` status `ready` deltaP `27.5074` edge `0.9826` maxDD `-22.166`
- `market_context_high->crypto_alt_4h` score `4.3249` n `164` status `ready` deltaP `15.8536` edge `0.4188` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8186` n `164` status `ready` deltaP `14.6341` edge `0.4499` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.5488` n `149` status `ready` deltaP `19.667` edge `0.7275` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.3617` n `164` status `ready` deltaP `15.8537` edge `0.11` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.7749` n `164` status `ready` deltaP `8.8415` edge `0.1695` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.536` n `149` status `ready` deltaP `12.8857` edge `0.0483` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4484` n `176` status `ready` deltaP `4.5182` edge `0.1034` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.2361` n `149` status `ready` deltaP `21.0244` edge `0.0536` maxDD `-7.413`
- `market_context_high->crypto_major_1h` score `0.2337` n `176` status `ready` deltaP `5.5083` edge `0.1073` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.0685` n `176` status `ready` deltaP `6.4848` edge `0.059` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.011` n `176` status `ready` deltaP `5.6478` edge `0.0118` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.2586` n `176` status `ready` deltaP `3.8003` edge `0.0123` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3113` n `176` status `ready` deltaP `0.7145` edge `0.0001` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.6248` n `164` status `ready` deltaP `5.3354` edge `0.0241` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.7158` n `164` status `ready` deltaP `1.3719` edge `0.002` maxDD `-1.567`
- `market_context_high->crypto_alt_24h` score `-0.8347` n `149` status `ready` deltaP `14.6987` edge `0.4875` maxDD `-43.0675`
- `market_context_high->commodity_1h` score `-1.4334` n `176` status `ready` deltaP `-3.4397` edge `-0.0074` maxDD `-3.1295`
- `market_context_high->metal_4h` score `-1.5903` n `164` status `ready` deltaP `-2.2866` edge `0.0117` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
