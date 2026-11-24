# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T23:22:31.475904+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4068`

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

- `market_context_high->unknown_1h` score `32266.391` n `45` status `ready` deltaP `1.5668` edge `2688.8649` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22005.4057` n `45` status `ready` deltaP `3.1776` edge `1833.7765` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1031.436` n `31` status `ready` deltaP `1.7819` edge `85.9587` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `752.4582` n `31` status `ready` deltaP `4.3962` edge `62.6812` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.6411` n `31` status `ready` deltaP `50.1736` edge `2.8856` maxDD `0.0`
- `news_risk_high->equity_24h` score `37.5879` n `31` status `ready` deltaP `43.9236` edge `2.8395` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.4099` n `31` status `ready` deltaP `48.9583` edge `2.5411` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8273` n `31` status `ready` deltaP `27.0653` edge `0.8922` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.0834` n `31` status `ready` deltaP `41.2355` edge `0.6762` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.297` n `31` status `ready` deltaP `34.1759` edge `0.6783` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.297` n `31` status `ready` deltaP `17.5403` edge `0.9603` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.7811` n `31` status `ready` deltaP `49.0032` edge `0.1679` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.5984` n `31` status `ready` deltaP `41.8403` edge `0.1876` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.6776` n `31` status `ready` deltaP `18.9395` edge `0.1989` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0405` n `31` status `ready` deltaP `32.8039` edge `0.0607` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.7319` n `45` status `ready` deltaP `33.2893` edge `0.0342` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.7229` n `31` status `ready` deltaP `12.4058` edge `0.3125` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.58` n `31` status `ready` deltaP `30.4955` edge `0.0202` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.4039` n `31` status `ready` deltaP `12.4058` edge `0.2612` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6256` n `31` status `ready` deltaP `30.4809` edge `0.0331` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
