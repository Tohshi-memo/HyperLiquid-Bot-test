# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T05:22:31.466086+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `30.852` n `134` status `ready` deltaP `-17.0377` edge `2.93` maxDD `-9.6329`
- `market_context_high->commodity_4h` score `0.7022` n `169` status `ready` deltaP `10.7662` edge `0.0582` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6753` n `180` status `ready` deltaP `9.3114` edge `0.0285` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.573` n `134` status `ready` deltaP `18.29` edge `0.0323` maxDD `-1.4613`
- `market_context_high->commodity_24h` score `0.0598` n `134` status `ready` deltaP `11.6408` edge `0.1539` maxDD `-12.2408`
- `market_context_high->fx_4h` score `-0.2201` n `169` status `ready` deltaP `4.2077` edge `0.0042` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.2763` n `180` status `ready` deltaP `1.6866` edge `-0.0015` maxDD `-0.613`
- `market_context_high->index_1h` score `-0.8647` n `180` status `ready` deltaP `-7.0758` edge `-0.0049` maxDD `-1.0359`
- `market_context_high->index_4h` score `-0.9498` n `169` status `ready` deltaP `-3.5017` edge `-0.009` maxDD `-1.4875`
- `market_context_high->metal_1h` score `-1.4162` n `180` status `ready` deltaP `-6.4371` edge `-0.0115` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.5145` n `180` status `ready` deltaP `-6.8662` edge `-0.0207` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-2.347` n `134` status `ready` deltaP `0.5785` edge `-0.067` maxDD `-2.9283`
- `market_context_high->crypto_alt_1h` score `-2.6345` n `180` status `ready` deltaP `-9.1084` edge `-0.0403` maxDD `-6.4812`
- `market_context_high->index_24h` score `-2.6693` n `134` status `ready` deltaP `-13.1385` edge `-0.0451` maxDD `-6.7627`
- `market_context_high->metal_4h` score `-3.351` n `169` status `ready` deltaP `-9.2189` edge `-0.0414` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.4611` n `180` status `ready` deltaP `-7.8011` edge `-0.046` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.0356` n `169` status `ready` deltaP `-12.9862` edge `-0.1199` maxDD `-15.8728`
- `market_context_high->crypto_alt_4h` score `-6.5882` n `169` status `ready` deltaP `-11.9721` edge `-0.1344` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-7.0322` n `134` status `ready` deltaP `-15.0209` edge `-0.2243` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-9.089` n `134` status `ready` deltaP `-11.2638` edge `-0.2025` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
