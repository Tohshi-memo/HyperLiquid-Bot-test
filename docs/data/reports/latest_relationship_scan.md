# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T12:07:15.299594+00:00`
- Price records: `672`
- Market context records: `1010`
- Flow alert records: `4816`
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

- `market_context_high->crypto_major_24h` score `13.1832` n `202` status `ready` deltaP `32.1524` edge `0.9431` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1794` n `202` status `ready` deltaP `11.0081` edge `0.3983` maxDD `-9.5387`
- `market_context_high->index_24h` score `-0.175` n `202` status `ready` deltaP `4.9474` edge `0.1433` maxDD `-5.2693`
- `market_context_high->commodity_1h` score `-0.5402` n `202` status `ready` deltaP `2.6946` edge `0.0178` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.5642` n `202` status `ready` deltaP `1.703` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->equity_24h` score `-0.6022` n `202` status `ready` deltaP `5.2542` edge `0.1601` maxDD `-10.2918`
- `market_context_high->fx_4h` score `-0.6749` n `202` status `ready` deltaP `1.713` edge `0.0017` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7433` n `202` status `ready` deltaP `2.656` edge `0.0057` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-0.753` n `202` status `ready` deltaP `-0.3721` edge `0.0166` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.2571` n `202` status `ready` deltaP `4.5355` edge `-0.0191` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3944` n `202` status `ready` deltaP `-1.5904` edge `-0.0242` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.4967` n `202` status `ready` deltaP `1.467` edge `0.0807` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7124` n `202` status `ready` deltaP `-1.541` edge `0.0194` maxDD `-6.4794`
- `market_context_high->metal_1h` score `-1.8194` n `202` status `ready` deltaP `0.206` edge `-0.0387` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-3.0436` n `202` status `ready` deltaP `6.2047` edge `0.0756` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.0632` n `202` status `ready` deltaP `-0.7954` edge `0.0668` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.2929` n `202` status `ready` deltaP `-2.1447` edge `0.0177` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.4103` n `202` status `ready` deltaP `-0.5573` edge `-0.0217` maxDD `-19.6109`
- `market_context_high->metal_4h` score `-4.578` n `202` status `ready` deltaP `-4.2713` edge `-0.1662` maxDD `-24.713`
- `market_context_high->commodity_24h` score `-8.4329` n `202` status `ready` deltaP `1.8207` edge `0.3715` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
