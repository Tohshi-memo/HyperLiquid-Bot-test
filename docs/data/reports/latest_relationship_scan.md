# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T11:37:17.907246+00:00`
- Price records: `672`
- Market context records: `2137`
- Flow alert records: `8049`
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

- `market_context_high->crypto_alt_4h` score `13.1615` n `158` status `ready` deltaP `36.7687` edge `0.9453` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7804` n `158` status `ready` deltaP `41.0698` edge `0.7609` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.3838` n `158` status `ready` deltaP `24.6604` edge `0.4425` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.1072` n `33` status `ready` deltaP `28.0442` edge `0.3891` maxDD `-3.0367`
- `market_context_high->equity_4h` score `5.0118` n `158` status `ready` deltaP `26.6247` edge `0.3496` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.5858` n `157` status `ready` deltaP `14.6177` edge `0.3242` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.2134` n `158` status `ready` deltaP `17.5851` edge `0.2027` maxDD `-2.1721`
- `market_context_high->metal_4h` score `3.0857` n `158` status `ready` deltaP `21.4032` edge `0.2532` maxDD `-4.7664`
- `market_context_high->crypto_alt_1h` score `3.0442` n `158` status `ready` deltaP `15.7887` edge `0.2348` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.0365` n `158` status `ready` deltaP `22.0651` edge `0.1743` maxDD `-1.8022`
- `market_context_high->equity_24h` score `2.9495` n `157` status `ready` deltaP `26.0606` edge `0.5619` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.5707` n `157` status `ready` deltaP `26.5894` edge `0.569` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.4455` n `33` status `ready` deltaP `31.6473` edge `0.0112` maxDD `-0.1382`
- `news_risk_high->unknown_1h` score `2.4328` n `34` status `ready` deltaP `27.9148` edge `0.0469` maxDD `-1.7548`
- `market_context_high->crypto_major_24h` score `1.8683` n `157` status `ready` deltaP `21.571` edge `0.9543` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.3038` n `33` status `ready` deltaP `17.2765` edge `0.1243` maxDD `-2.7857`
- `news_risk_high->commodity_1h` score `0.9857` n `34` status `ready` deltaP `8.8235` edge `0.0913` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.8406` n `158` status `ready` deltaP `10.318` edge `0.0801` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.5967` n `158` status `ready` deltaP `8.9422` edge `0.0571` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.4689` n `157` status `ready` deltaP `12.5456` edge `0.3666` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
