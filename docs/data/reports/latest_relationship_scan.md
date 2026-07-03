# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T14:52:25.722934+00:00`
- Price records: `672`
- Market context records: `5567`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11396`

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

- `market_context_high->equity_24h` score `4.4556` n `179` status `ready` deltaP `15.5542` edge `0.7755` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.2956` n `191` status `ready` deltaP `11.3428` edge `0.2616` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.1462` n `179` status `ready` deltaP `14.6017` edge `0.4522` maxDD `-29.6555`
- `market_context_high->equity_4h` score `0.7779` n `191` status `ready` deltaP `6.9284` edge `0.1825` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.7639` n `179` status `ready` deltaP `16.6851` edge `0.0498` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.7618` n `191` status `ready` deltaP `6.7896` edge `0.1823` maxDD `-9.46`
- `market_context_high->index_1h` score `-0.1201` n `201` status `ready` deltaP `4.5193` edge `0.0092` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.2243` n `201` status `ready` deltaP `5.6551` edge `0.0443` maxDD `-5.0555`
- `market_context_high->fx_4h` score `-0.2881` n `191` status `ready` deltaP `5.9674` edge `0.0096` maxDD `-0.8712`
- `market_context_high->fx_1h` score `-0.4124` n `201` status `ready` deltaP `1.6884` edge `0.0012` maxDD `-0.4122`
- `market_context_high->crypto_alt_1h` score `-0.4994` n `201` status `ready` deltaP `1.0852` edge `0.0473` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.5257` n `201` status `ready` deltaP `-0.2972` edge `0.0021` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.646` n `201` status `ready` deltaP `2.9873` edge `0.0508` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.2428` n `201` status `ready` deltaP `-2.9873` edge `-0.0071` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.564` n `191` status `ready` deltaP `2.1437` edge `0.0163` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.9926` n `179` status `ready` deltaP `12.9636` edge `0.0568` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.1632` n `191` status `ready` deltaP `-14.1593` edge `-0.0633` maxDD `-12.4941`
- `market_context_high->commodity_4h` score `-4.4939` n `191` status `ready` deltaP `-7.7305` edge `-0.0554` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.7803` n `179` status `ready` deltaP `-6.961` edge `-0.2133` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-8.5925` n `179` status `ready` deltaP `4.9154` edge `0.1209` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
