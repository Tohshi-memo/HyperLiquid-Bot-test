# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T14:52:35.287083+00:00`
- Price records: `672`
- Market context records: `5257`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `25.4853` n `146` status `ready` deltaP `29.3784` edge `1.9469` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `10.5192` n `146` status `ready` deltaP `28.9003` edge `1.0501` maxDD `-22.6266`
- `market_context_high->crypto_alt_4h` score `3.9185` n `160` status `ready` deltaP `13.3232` edge `0.4018` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.6527` n `160` status `ready` deltaP `13.5061` edge `0.4436` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.3764` n `146` status `ready` deltaP `19.4326` edge `0.7147` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.6333` n `160` status `ready` deltaP `16.1738` edge `0.1305` maxDD `-5.5109`
- `market_context_high->crypto_alt_24h` score `1.0138` n `146` status `ready` deltaP `15.7605` edge `0.5478` maxDD `-34.8045`
- `market_context_high->crypto_alt_1h` score `0.6607` n `168` status `ready` deltaP `5.3714` edge `0.1154` maxDD `-5.0257`
- `market_context_high->fx_24h` score `0.4976` n `146` status `ready` deltaP `12.5547` edge `0.0473` maxDD `-0.8294`
- `market_context_high->equity_4h` score `0.48` n `160` status `ready` deltaP `8.0945` edge `0.1499` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.4514` n `168` status `ready` deltaP `6.2803` edge `0.1203` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.1879` n `146` status `ready` deltaP `20.8476` edge `0.0486` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.1185` n `168` status `ready` deltaP `6.8256` edge `0.0609` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0654` n `168` status `ready` deltaP `5.0435` edge `0.0113` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0669` n `168` status `ready` deltaP `5.2217` edge `0.0188` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3026` n `168` status `ready` deltaP `1.0265` edge `-0.0004` maxDD `-0.6194`
- `market_context_high->unknown_1h` score `-0.411` n `168` status `ready` deltaP `7.8593` edge `-0.0225` maxDD `-2.7986`
- `market_context_high->index_4h` score `-0.7434` n `160` status `ready` deltaP `4.5732` edge `0.0193` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.8152` n `160` status `ready` deltaP `-0.2439` edge `0.0005` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-1.2447` n `168` status `ready` deltaP `-2.0887` edge `-0.0057` maxDD `-2.728`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
