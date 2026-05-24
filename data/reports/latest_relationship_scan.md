# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T13:52:16.487522+00:00`
- Price records: `672`
- Market context records: `1742`
- Flow alert records: `6919`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8852`

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

- `market_context_high->metal_24h` score `7.1191` n `157` status `ready` deltaP `26.3034` edge `0.6605` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.8071` n `196` status `ready` deltaP `20.3615` edge `0.5248` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `4.5194` n `157` status `ready` deltaP `15.6233` edge `0.8045` maxDD `-35.8966`
- `market_context_high->index_24h` score `4.3885` n `157` status `ready` deltaP `18.8466` edge `0.3629` maxDD `-4.1604`
- `market_context_high->crypto_major_4h` score `4.1201` n `196` status `ready` deltaP `21.1952` edge `0.4426` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.0383` n `196` status `ready` deltaP `13.3368` edge `0.3914` maxDD `-11.1695`
- `market_context_high->equity_4h` score `2.8918` n `196` status `ready` deltaP `15.3497` edge `0.2481` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.8818` n `157` status `ready` deltaP `17.3387` edge `0.6144` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7201` n `196` status `ready` deltaP `7.2712` edge `0.1139` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.7195` n `196` status `ready` deltaP `10.4935` edge `0.0989` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `0.6786` n `157` status `ready` deltaP `20.1205` edge `0.781` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.1734` n `157` status `ready` deltaP `21.1737` edge `1.0542` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.1525` n `196` status `ready` deltaP `4.598` edge `0.0894` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0167` n `196` status `ready` deltaP `4.6713` edge `0.0511` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2742` n `196` status `ready` deltaP `3.1682` edge `0.0192` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.3045` n `196` status `ready` deltaP `12.2916` edge `0.1482` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5051` n `196` status `ready` deltaP `6.2447` edge `0.0272` maxDD `-6.3532`
- `market_context_high->fx_24h` score `-0.6788` n `157` status `ready` deltaP `6.3208` edge `0.0062` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6887` n `196` status `ready` deltaP `-3.5653` edge `-0.0013` maxDD `-0.3914`
- `market_context_high->unknown_1h` score `-1.6534` n `196` status `ready` deltaP `0.1894` edge `0.0079` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
