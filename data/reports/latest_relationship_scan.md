# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T14:07:30.697631+00:00`
- Price records: `672`
- Market context records: `8203`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8238.4971` n `43` status `ready` deltaP `36.9792` edge `686.2949` maxDD `0.0`
- `market_context_high->equity_24h` score `22.5587` n `38` status `ready` deltaP `44.2525` edge `1.6759` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.7617` n `39` status `ready` deltaP `46.6737` edge `0.5066` maxDD `-0.0094`
- `market_context_high->metal_24h` score `9.1015` n `38` status `ready` deltaP `47.0486` edge `0.4448` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.538` n `38` status `ready` deltaP `21.9572` edge `1.0832` maxDD `-5.4639`
- `news_risk_high->equity_4h` score `6.9307` n `54` status `ready` deltaP `25.1637` edge `0.4695` maxDD `-3.4427`
- `market_context_high->crypto_major_24h` score `6.9164` n `38` status `ready` deltaP `21.4364` edge `0.9907` maxDD `-14.418`
- `market_context_high->index_4h` score `4.088` n `39` status `ready` deltaP `38.4967` edge `0.0883` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.8581` n `39` status `ready` deltaP `37.6095` edge `0.0886` maxDD `-0.0926`
- `market_context_high->equity_1h` score `3.4186` n `39` status `ready` deltaP `17.5841` edge `0.1823` maxDD `-0.1718`
- `market_context_high->index_24h` score `3.1246` n `38` status `ready` deltaP `29.6784` edge `0.2647` maxDD `-0.9576`
- `news_risk_high->equity_1h` score `3.1169` n `54` status `ready` deltaP `22.4274` edge `0.1411` maxDD `-1.1366`
- `market_context_high->crypto_alt_4h` score `2.9555` n `39` status `ready` deltaP `10.9835` edge `0.2175` maxDD `-1.5544`
- `news_risk_high->crypto_major_4h` score `2.7178` n `54` status `ready` deltaP `13.8325` edge `0.3256` maxDD `-2.8833`
- `news_risk_high->index_4h` score `2.6373` n `54` status `ready` deltaP `22.1149` edge `0.0914` maxDD `-0.191`
- `news_risk_high->crypto_major_1h` score `2.0081` n `54` status `ready` deltaP `13.6006` edge `0.1164` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8866` n `54` status `ready` deltaP `15.153` edge `0.0996` maxDD `-1.1388`
- `market_context_high->fx_24h` score `1.8608` n `38` status `ready` deltaP `34.8593` edge `0.071` maxDD `-0.5196`
- `market_context_high->crypto_major_4h` score `1.7349` n `39` status `ready` deltaP `13.5476` edge `0.238` maxDD `-4.4715`
- `market_context_high->metal_1h` score `1.5957` n `39` status `ready` deltaP `17.8835` edge `0.0312` maxDD `-0.0623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
