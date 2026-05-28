# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T11:07:19.219953+00:00`
- Price records: `672`
- Market context records: `2135`
- Flow alert records: `8043`
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

- `market_context_high->crypto_alt_4h` score `13.1663` n `158` status `ready` deltaP `36.7687` edge `0.9457` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8044` n `158` status `ready` deltaP `41.0698` edge `0.7629` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.2983` n `158` status `ready` deltaP `24.3555` edge `0.4374` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.019` n `158` status `ready` deltaP `26.6247` edge `0.3502` maxDD `-5.0894`
- `news_risk_high->commodity_4h` score `3.9514` n `32` status `ready` deltaP `27.2866` edge `0.3918` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.5173` n `157` status `ready` deltaP `14.3775` edge `0.3201` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.2086` n `158` status `ready` deltaP `17.5851` edge `0.2023` maxDD `-2.1721`
- `market_context_high->metal_4h` score `3.0929` n `158` status `ready` deltaP `21.4032` edge `0.2538` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.0449` n `158` status `ready` deltaP `22.0651` edge `0.175` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `3.0191` n `158` status `ready` deltaP `15.639` edge `0.2337` maxDD `-4.9097`
- `market_context_high->equity_24h` score `2.833` n `157` status `ready` deltaP `25.8039` edge `0.5539` maxDD `-33.1875`
- `news_risk_high->unknown_1h` score `2.8017` n `33` status `ready` deltaP `30.1715` edge `0.0626` maxDD `-1.7548`
- `news_risk_high->fx_4h` score `2.7399` n `32` status `ready` deltaP `34.2988` edge `0.0132` maxDD `-0.0826`
- `market_context_high->unknown_24h` score `2.4378` n `157` status `ready` deltaP `26.3384` edge `0.5596` maxDD `-35.8966`
- `news_risk_high->unknown_4h` score `2.2309` n `32` status `ready` deltaP `19.0549` edge `0.1312` maxDD `-2.7857`
- `market_context_high->crypto_major_24h` score `1.8171` n `157` status `ready` deltaP `21.6373` edge `0.9473` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.8083` n `158` status `ready` deltaP `10.0186` edge `0.0794` maxDD `-2.6402`
- `news_risk_high->commodity_1h` score `0.7946` n `33` status `ready` deltaP `7.8752` edge `0.0817` maxDD `-2.1052`
- `market_context_high->metal_1h` score `0.5583` n `158` status `ready` deltaP `8.6428` edge `0.0559` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.4266` n `157` status `ready` deltaP `12.2716` edge `0.363` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
