# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T15:26:32.093666+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11785`

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

- `market_context_high->unknown_24h` score `37.5797` n `103` status `ready` deltaP `3.8902` edge `3.11` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.1187` n `103` status `ready` deltaP `3.6542` edge `0.1857` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.0524` n `113` status `ready` deltaP `12.7387` edge `0.0874` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.548` n `103` status `ready` deltaP `21.6205` edge `0.0467` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4166` n `117` status `ready` deltaP `7.6079` edge `0.0256` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0464` n `117` status `ready` deltaP `6.7289` edge `-0.0039` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3065` n `113` status `ready` deltaP `7.0945` edge `-0.0006` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5097` n `117` status `ready` deltaP `-1.6492` edge `-0.0049` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6527` n `117` status `ready` deltaP `-2.3977` edge `-0.0143` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7551` n `113` status `ready` deltaP `2.8302` edge `0.0078` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.7727` n `117` status `ready` deltaP `-2.866` edge `-0.0089` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.1033` n `113` status `ready` deltaP `3.7705` edge `-0.0276` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.3255` n `103` status `ready` deltaP `-4.6268` edge `0.0804` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.331` n `117` status `ready` deltaP `3.7541` edge `-0.0392` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.668` n `113` status `ready` deltaP `-7.3656` edge `-0.0393` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-2.6588` n `117` status `ready` deltaP `-7.1153` edge `-0.0368` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-2.7629` n `103` status `ready` deltaP `-4.7751` edge `-0.0541` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.1925` n `113` status `ready` deltaP `0.2348` edge `-0.2666` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.2991` n `103` status `ready` deltaP `9.5908` edge `0.005` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.3524` n `113` status `ready` deltaP `-6.1205` edge `-0.1507` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
