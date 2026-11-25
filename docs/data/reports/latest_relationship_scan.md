# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T02:37:33.326025+00:00`
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

- `market_context_high->unknown_1h` score `32251.4053` n `45` status `ready` deltaP `2.1656` edge `2687.6121` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21990.6901` n `45` status `ready` deltaP `3.1776` edge `1832.5502` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1016.4503` n `31` status `ready` deltaP `2.3807` edge `84.7059` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `737.7426` n `31` status `ready` deltaP `4.3962` edge `61.4549` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.9447` n `31` status `ready` deltaP `50.1736` edge `2.9109` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.6194` n `31` status `ready` deltaP `44.0972` edge `2.9243` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.1047` n `31` status `ready` deltaP `48.9583` edge `2.599` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8553` n `31` status `ready` deltaP `27.3701` edge `0.8925` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1927` n `31` status `ready` deltaP `41.2355` edge `0.6853` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.3601` n `31` status `ready` deltaP `34.7856` edge `0.6795` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.3556` n `31` status `ready` deltaP `17.6927` edge `0.9668` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.791` n `31` status `ready` deltaP `42.8819` edge `0.1967` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.513` n `31` status `ready` deltaP `46.7462` edge `0.1606` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.68` n `31` status `ready` deltaP `19.0892` edge `0.1981` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.1111` n `31` status `ready` deltaP `33.5661` edge `0.0615` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7681` n `31` status `ready` deltaP `12.7052` edge `0.3163` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.6114` n `45` status `ready` deltaP `31.9173` edge `0.0333` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.6016` n `31` status `ready` deltaP `30.7949` edge `0.02` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.4148` n `31` status `ready` deltaP `12.7052` edge `0.2606` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5672` n `31` status `ready` deltaP `29.8821` edge `0.0296` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
