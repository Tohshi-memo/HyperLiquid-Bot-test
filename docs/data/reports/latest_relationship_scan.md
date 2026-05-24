# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T06:37:14.185796+00:00`
- Price records: `672`
- Market context records: `1709`
- Flow alert records: `6828`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->unknown_24h` score `8.2572` n `139` status `ready` deltaP `17.7367` edge `1.1019` maxDD `-35.8966`
- `market_context_high->metal_24h` score `6.5766` n `139` status `ready` deltaP `25.3578` edge `0.6216` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.0038` n `197` status `ready` deltaP `21.6758` edge `0.5389` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `4.182` n `197` status `ready` deltaP `23.3982` edge `0.4634` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.6388` n `139` status `ready` deltaP `16.6251` edge `0.3302` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.0068` n `197` status `ready` deltaP `16.4882` edge `0.2501` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.3625` n `139` status `ready` deltaP `15.4775` edge `0.5002` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.8969` n `197` status `ready` deltaP `7.8612` edge `0.1247` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.5058` n `197` status `ready` deltaP `8.4669` edge `0.0946` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.2649` n `197` status `ready` deltaP `5.2061` edge `0.095` maxDD `-3.9439`
- `market_context_high->crypto_alt_24h` score `0.1676` n `139` status `ready` deltaP `23.8468` edge `1.0359` maxDD `-88.8062`
- `market_context_high->equity_1h` score `-0.0028` n `197` status `ready` deltaP `4.3527` edge `0.0516` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.2301` n `197` status `ready` deltaP `13.0478` edge `0.1527` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.4783` n `197` status `ready` deltaP `0.7668` edge `0.0182` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.4858` n `197` status `ready` deltaP `5.8049` edge `0.0326` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6472` n `197` status `ready` deltaP `-2.8572` edge `-0.0007` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.8261` n `139` status `ready` deltaP `4.3601` edge `0.007` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.9698` n `139` status `ready` deltaP `22.0433` edge `0.5873` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.7703` n `197` status `ready` deltaP `-6.7553` edge `-0.0096` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.9998` n `197` status `ready` deltaP `0.4293` edge `-0.0138` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
