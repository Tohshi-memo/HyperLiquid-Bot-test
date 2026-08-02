# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T11:22:27.866463+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5900`

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

- `news_risk_high->unknown_24h` score `5185.0075` n `60` status `ready` deltaP `29.2708` edge `431.9309` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.5103` n `40` status `ready` deltaP `58.9236` edge `1.1061` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.6638` n `40` status `ready` deltaP `51.3194` edge `0.5593` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.5529` n `68` status `ready` deltaP `16.5261` edge `0.3456` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.6182` n `68` status `ready` deltaP `15.9164` edge `0.0668` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0183` n `40` status `ready` deltaP `12.9878` edge `0.1286` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.6839` n `68` status `ready` deltaP `10.2413` edge `0.071` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.6147` n `40` status `ready` deltaP `19.8476` edge `0.0261` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.5734` n `40` status `ready` deltaP `10.8982` edge `0.0383` maxDD `-1.3282`
- `market_context_high->crypto_alt_4h` score `0.5628` n `40` status `ready` deltaP `7.5915` edge `0.1121` maxDD `-4.9116`
- `market_context_high->fx_1h` score `0.4692` n `40` status `ready` deltaP `14.2964` edge `0.0026` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.26` n `68` status `ready` deltaP `13.8182` edge `0.0253` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1632` n `68` status `ready` deltaP `6.0796` edge `0.028` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1162` n `68` status `ready` deltaP `6.7806` edge `0.0379` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0427` n `68` status `ready` deltaP `3.267` edge `0.005` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0528` n `68` status `ready` deltaP `2.7651` edge `0.0071` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.0905` n `68` status `ready` deltaP `3.3639` edge `0.0063` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1735` n `68` status `ready` deltaP `2.9676` edge `0.03` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.3918` n `40` status `ready` deltaP `0.8982` edge `0.0065` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.7035` n `68` status `ready` deltaP `2.3688` edge `-0.028` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
