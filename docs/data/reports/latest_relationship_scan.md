# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T11:07:34.341114+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9968`

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

- `market_context_high->unknown_1h` score `65.9478` n `47` status `ready` deltaP `10.2657` edge `5.4343` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `42.6266` n `46` status `ready` deltaP `29.8536` edge `3.3688` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `28.2853` n `46` status `ready` deltaP `24.8264` edge `2.1916` maxDD `0.0`
- `market_context_high->equity_24h` score `24.6756` n `46` status `ready` deltaP `27.2494` edge `1.8847` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `8.8855` n `103` status `ready` deltaP `2.1626` edge `1.6303` maxDD `-63.6743`
- `market_context_high->index_24h` score `8.1137` n `46` status `ready` deltaP `36.2772` edge `0.443` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `6.0232` n `103` status `ready` deltaP `-0.4163` edge `1.206` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.4393` n `46` status `ready` deltaP `30.2537` edge `0.1083` maxDD `-0.2042`
- `market_context_high->index_4h` score `3.0105` n `47` status `ready` deltaP `34.3312` edge `0.0374` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5283` n `47` status `ready` deltaP `17.1445` edge `0.1382` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.4969` n `114` status `ready` deltaP `13.3969` edge `0.1678` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `2.0925` n `114` status `ready` deltaP `15.343` edge `0.1156` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.7253` n `114` status `ready` deltaP `25.1659` edge `0.0396` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.4188` n `103` status `ready` deltaP `18.0184` edge `0.116` maxDD `-2.431`
- `news_risk_high->fx_24h` score `1.2988` n `103` status `ready` deltaP `30.1847` edge `0.1284` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9954` n `47` status `ready` deltaP `15.0592` edge `0.0104` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.9023` n `103` status `ready` deltaP `22.1279` edge `0.113` maxDD `-7.2536`
- `market_context_high->equity_1h` score `0.8875` n `47` status `ready` deltaP `10.8676` edge `0.0418` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.7091` n `114` status `ready` deltaP `15.5741` edge `0.0146` maxDD `-0.7468`
- `news_risk_high->crypto_major_4h` score `0.5705` n `114` status `ready` deltaP `12.3288` edge `0.1785` maxDD `-13.719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
