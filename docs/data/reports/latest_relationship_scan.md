# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T13:22:22.277777+00:00`
- Price records: `672`
- Market context records: `2145`
- Flow alert records: `8071`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9158`

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

- `market_context_high->crypto_alt_4h` score `13.4314` n `156` status `ready` deltaP `37.8479` edge `0.9606` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9592` n `156` status `ready` deltaP `41.909` edge `0.7702` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.511` n `156` status `ready` deltaP `25.3947` edge `0.4482` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.2394` n `33` status `ready` deltaP `28.1966` edge `0.3991` maxDD `-3.0367`
- `market_context_high->equity_4h` score `5.0614` n `156` status `ready` deltaP `26.63` edge `0.3537` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.8583` n `155` status `ready` deltaP `15.4145` edge `0.3416` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.3324` n `156` status `ready` deltaP `17.6723` edge `0.2076` maxDD `-1.817`
- `market_context_high->equity_24h` score `3.3034` n `155` status `ready` deltaP `26.8986` edge `0.5858` maxDD `-33.1875`
- `market_context_high->metal_4h` score `3.1816` n `156` status `ready` deltaP `21.8223` edge `0.2584` maxDD `-4.7664`
- `market_context_high->crypto_alt_1h` score `3.1352` n `156` status `ready` deltaP `16.1753` edge `0.2398` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.0985` n `156` status `ready` deltaP `22.5101` edge `0.1765` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.9112` n `155` status `ready` deltaP `27.4709` edge `0.5915` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.3871` n `33` status `ready` deltaP `31.0375` edge `0.0104` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.2478` n `155` status `ready` deltaP `22.0284` edge `0.9999` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.4997` n `33` status `ready` deltaP `18.3435` edge `0.1423` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.1625` n `39` status `ready` deltaP `21.0464` edge `0.0035` maxDD `-1.7548`
- `market_context_high->equity_1h` score `0.8489` n `156` status `ready` deltaP `10.2718` edge `0.0811` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.6246` n `156` status `ready` deltaP `9.2315` edge `0.0575` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.5948` n `39` status `ready` deltaP `9.5732` edge `0.0114` maxDD `-0.0524`
- `news_risk_high->commodity_1h` score `0.5752` n `39` status `ready` deltaP `9.1241` edge `0.0809` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
