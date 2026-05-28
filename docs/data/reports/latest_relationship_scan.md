# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T14:37:26.524569+00:00`
- Price records: `672`
- Market context records: `2150`
- Flow alert records: `8086`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `market_context_high->crypto_alt_4h` score `13.6429` n `151` status `ready` deltaP `38.1219` edge `0.9764` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9957` n `151` status `ready` deltaP `42.2003` edge `0.7713` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.4818` n `151` status `ready` deltaP `25.1343` edge `0.4475` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.8301` n `151` status `ready` deltaP `26.1842` edge `0.3374` maxDD `-5.0894`
- `news_risk_high->commodity_4h` score `4.0895` n `34` status `ready` deltaP `28.7572` edge `0.3997` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.735` n `151` status `ready` deltaP `14.6236` edge `0.3366` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.5624` n `151` status `ready` deltaP `19.0467` edge `0.2176` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.3265` n `151` status `ready` deltaP `17.0371` edge `0.25` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.2955` n `151` status `ready` deltaP `23.9976` edge `0.183` maxDD `-1.8022`
- `market_context_high->metal_4h` score `3.1823` n `151` status `ready` deltaP `21.7705` edge `0.2588` maxDD `-4.7664`
- `market_context_high->equity_24h` score `3.1189` n `151` status `ready` deltaP `26.3325` edge `0.5742` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.8184` n `151` status `ready` deltaP `27.1811` edge `0.5857` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.3713` n `34` status `ready` deltaP `30.7209` edge `0.0112` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1892` n `151` status `ready` deltaP `21.1576` edge `0.9982` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.3288` n `34` status `ready` deltaP `16.9925` edge `0.1294` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0555` n `43` status `ready` deltaP `19.0189` edge `0.0081` maxDD `-1.7548`
- `market_context_high->equity_1h` score `0.8647` n `151` status `ready` deltaP `10.5138` edge `0.0808` maxDD `-2.6402`
- `news_risk_high->commodity_1h` score `0.7869` n `43` status `ready` deltaP `10.4651` edge `0.0991` maxDD `-2.1052`
- `market_context_high->metal_1h` score `0.6586` n `151` status `ready` deltaP `9.326` edge `0.0597` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.4885` n `43` status `ready` deltaP `8.4389` edge `0.0101` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
