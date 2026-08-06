# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T14:52:30.223506+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11797`

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

- `market_context_high->unknown_24h` score `17.3377` n `101` status `ready` deltaP `3.871` edge `1.4233` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.2622` n `101` status `ready` deltaP `4.2027` edge `0.194` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.0863` n `113` status `ready` deltaP `13.0436` edge `0.0882` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.498` n `101` status `ready` deltaP `20.7938` edge `0.0458` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3535` n `115` status `ready` deltaP `6.9995` edge `0.0244` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.063` n `115` status `ready` deltaP `7.0346` edge `-0.0038` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2883` n `113` status `ready` deltaP `7.3994` edge `-0.0003` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5249` n `115` status `ready` deltaP `-1.7469` edge `-0.0062` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6664` n `115` status `ready` deltaP `-2.4954` edge `-0.0154` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7818` n `113` status `ready` deltaP `2.5253` edge `0.0064` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-1.0719` n `113` status `ready` deltaP `4.0754` edge `-0.0256` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.2403` n `101` status `ready` deltaP `-3.859` edge `0.0862` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.2854` n `115` status `ready` deltaP `-3.4288` edge `-0.0132` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.4438` n `115` status `ready` deltaP `3.0852` edge `-0.0492` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.6688` n `113` status `ready` deltaP `-7.3656` edge `-0.0394` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-2.8189` n `115` status `ready` deltaP `-8.1112` edge `-0.0435` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-2.8584` n `101` status `ready` deltaP `-5.1585` edge `-0.0595` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.1675` n `113` status `ready` deltaP `0.2348` edge `-0.2634` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.4442` n `101` status `ready` deltaP `8.495` edge `-0.0063` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.3632` n `113` status `ready` deltaP `-6.1205` edge `-0.1516` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
