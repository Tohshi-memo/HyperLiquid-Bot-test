# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T11:37:17.562949+00:00`
- Price records: `672`
- Market context records: `1008`
- Flow alert records: `4810`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `13.1133` n `204` status `ready` deltaP `32.0741` edge `0.9378` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1698` n `204` status `ready` deltaP `10.9777` edge `0.3977` maxDD `-9.5387`
- `market_context_high->index_24h` score `-0.3363` n `204` status `ready` deltaP `4.3712` edge `0.1366` maxDD `-5.5016`
- `market_context_high->fx_1h` score `-0.5388` n `204` status `ready` deltaP `1.9902` edge `-0.0001` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5747` n `204` status `ready` deltaP `2.3541` edge `0.0172` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.6953` n `204` status `ready` deltaP `1.351` edge `0.0015` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7189` n `204` status `ready` deltaP `2.9764` edge `0.0056` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-0.7306` n `204` status `ready` deltaP `-0.0323` edge `0.0162` maxDD `-4.4826`
- `market_context_high->equity_24h` score `-0.8762` n `204` status `ready` deltaP `4.6771` edge `0.1506` maxDD `-10.3839`
- `market_context_high->crypto_major_1h` score `-1.246` n `204` status `ready` deltaP `4.6583` edge `-0.0185` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3857` n `204` status `ready` deltaP `-1.4529` edge `-0.024` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.5259` n `204` status `ready` deltaP `1.372` edge `0.0789` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7564` n `204` status `ready` deltaP `-1.9399` edge `0.0184` maxDD `-6.4798`
- `market_context_high->metal_1h` score `-1.819` n `204` status `ready` deltaP `0.1527` edge `-0.0383` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.9794` n `204` status `ready` deltaP `6.6027` edge `0.0783` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.0909` n `204` status `ready` deltaP `-0.9176` edge `0.0653` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3081` n `204` status `ready` deltaP `-2.0953` edge `0.0161` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.4445` n `204` status `ready` deltaP `-0.9129` edge `-0.022` maxDD `-19.7476`
- `market_context_high->metal_4h` score `-4.5902` n `204` status `ready` deltaP `-4.4625` edge `-0.1659` maxDD `-24.7606`
- `market_context_high->commodity_24h` score `-8.3656` n `204` status `ready` deltaP `2.0957` edge `0.3783` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
