# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T15:37:33.825077+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7456`

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

- `news_risk_high->unknown_1h` score `3426.1776` n `31` status `ready` deltaP `2.231` edge `285.5175` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3254.9649` n `31` status `ready` deltaP `3.634` edge `271.2285` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.6217` n `31` status `ready` deltaP `37.2617` edge `1.8034` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.5436` n `31` status `ready` deltaP `35.3553` edge `1.3096` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.034` n `31` status `ready` deltaP `29.2894` edge `0.8909` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.3228` n `31` status `ready` deltaP `24.1689` edge `0.7028` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.9069` n `31` status `ready` deltaP `18.3025` edge `0.777` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.8852` n `31` status `ready` deltaP `32.8039` edge `0.3198` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0924` n `31` status `ready` deltaP `41.969` edge `0.1574` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9446` n `31` status `ready` deltaP `17.0403` edge `0.2426` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.6279` n `31` status `ready` deltaP `32.0417` edge `0.0314` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4573` n `31` status `ready` deltaP `26.5165` edge `0.028` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3439` n `31` status `ready` deltaP `28.6991` edge `0.0125` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2635` n `31` status `ready` deltaP `14.8976` edge `0.108` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.0667` n `31` status `ready` deltaP `6.8669` edge `0.2653` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9587` n `31` status `ready` deltaP `10.7591` edge `0.2151` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1449` n `31` status `ready` deltaP `24.7923` edge `0.0094` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.475` n `31` status `ready` deltaP `10.9608` edge `0.0276` maxDD `-0.5151`
- `market_context_high->fx_1h` score `0.4406` n `65` status `ready` deltaP `11.5385` edge `0.0017` maxDD `-0.1042`
- `news_risk_high->metal_4h` score `0.4131` n `31` status `ready` deltaP `12.5098` edge `0.0253` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
