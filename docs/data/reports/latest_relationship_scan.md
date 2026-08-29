# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T13:22:25.477694+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11392`

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

- `news_risk_high->unknown_24h` score `50.3073` n `56` status `ready` deltaP `15.6746` edge `4.1423` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.7143` n `56` status `ready` deltaP `37.1032` edge `2.0328` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.9202` n `107` status `ready` deltaP `18.9123` edge `0.6905` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.3643` n `80` status `ready` deltaP `11.5854` edge `0.5121` maxDD `-1.7183`
- `market_context_high->metal_24h` score `4.2693` n `107` status `ready` deltaP `31.8292` edge `0.2455` maxDD `-3.1535`
- `news_risk_high->equity_24h` score `2.8772` n `56` status `ready` deltaP `24.6528` edge `0.3937` maxDD `-12.4677`
- `news_risk_high->unknown_1h` score `2.6643` n `80` status `ready` deltaP `5.6737` edge `0.2199` maxDD `-0.8558`
- `news_risk_high->crypto_major_24h` score `2.5269` n `56` status `ready` deltaP `21.0069` edge `0.4238` maxDD `-16.524`
- `market_context_high->unknown_4h` score `2.4975` n `113` status `ready` deltaP `17.1164` edge `0.1372` maxDD `-0.788`
- `news_risk_high->fx_4h` score `2.4059` n `80` status `ready` deltaP `34.9695` edge `0.0223` maxDD `-0.3953`
- `news_risk_high->metal_24h` score `1.8451` n `56` status `ready` deltaP `38.0208` edge `0.0545` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.5152` n `56` status `ready` deltaP `20.9325` edge `0.0287` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `1.1375` n `125` status `ready` deltaP `9.3737` edge `0.0804` maxDD `-1.5148`
- `news_risk_high->fx_1h` score `0.7735` n `80` status `ready` deltaP `14.6407` edge `0.0057` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4019` n `80` status `ready` deltaP `11.7515` edge `0.0052` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.3139` n `113` status `ready` deltaP `6.5225` edge `0.008` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.391` n `80` status `ready` deltaP `0.3069` edge `-0.0085` maxDD `-0.8275`
- `market_context_high->crypto_major_4h` score `-0.4337` n `113` status `ready` deltaP `16.1895` edge `0.201` maxDD `-20.9394`
- `market_context_high->commodity_1h` score `-0.5059` n `125` status `ready` deltaP `-0.3485` edge `0.0079` maxDD `-1.635`
- `news_risk_high->index_4h` score `-0.5206` n `80` status `ready` deltaP `2.0732` edge `-0.0164` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
