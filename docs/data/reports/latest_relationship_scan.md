# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T19:52:31.931953+00:00`
- Price records: `672`
- Market context records: `2694`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `9.834` n `111` status `ready` deltaP `16.1787` edge `1.061` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6611` n `111` status `ready` deltaP `17.652` edge `0.6369` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8748` n `141` status `ready` deltaP `5.876` edge `0.1387` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.2177` n `141` status `ready` deltaP `11.5897` edge `0.0348` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1378` n `143` status `ready` deltaP `3.35` edge `0.0094` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1487` n `143` status `ready` deltaP `2.8988` edge `0.0411` maxDD `-3.1587`
- `market_context_high->commodity_1h` score `-0.4416` n `143` status `ready` deltaP `1.8488` edge `0.0064` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4668` n `143` status `ready` deltaP `0.2513` edge `0.0038` maxDD `-0.2164`
- `market_context_high->fx_24h` score `-0.4865` n `111` status `ready` deltaP `7.5216` edge `-0.0035` maxDD `-0.6418`
- `market_context_high->crypto_alt_1h` score `-0.5058` n `143` status `ready` deltaP `6.5942` edge `0.0672` maxDD `-10.747`
- `market_context_high->crypto_alt_4h` score `-0.5362` n `141` status `ready` deltaP `16.4343` edge `0.2785` maxDD `-28.6198`
- `market_context_high->crypto_major_24h` score `-0.7207` n `111` status `ready` deltaP `5.9967` edge `0.6239` maxDD `-44.169`
- `market_context_high->metal_1h` score `-0.7543` n `143` status `ready` deltaP `-1.3997` edge `-0.0028` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-0.7844` n `141` status `ready` deltaP `-0.9644` edge `0.0106` maxDD `-0.5631`
- `market_context_high->commodity_24h` score `-0.801` n `111` status `ready` deltaP `6.7474` edge `0.1617` maxDD `-12.4171`
- `market_context_high->index_24h` score `-0.8815` n `111` status `ready` deltaP `3.8429` edge `-0.001` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `-0.9768` n `143` status `ready` deltaP `3.6473` edge `0.0374` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-0.9854` n `141` status `ready` deltaP `4.9018` edge `0.033` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.2259` n `143` status `ready` deltaP `-4.4857` edge `0.0116` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-2.0614` n `141` status `ready` deltaP `-1.5201` edge `-0.0212` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
