# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T14:37:25.931050+00:00`
- Price records: `672`
- Market context records: `7038`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `market_context_high->fx_4h` score `-0.1508` n `208` status `ready` deltaP `13.2622` edge `0.0099` maxDD `-1.0784`
- `market_context_high->fx_1h` score `-0.2026` n `208` status `ready` deltaP `2.6082` edge `0.0019` maxDD `-0.2872`
- `market_context_high->crypto_alt_1h` score `-0.3118` n `208` status `ready` deltaP `2.0498` edge `0.0328` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7219` n `208` status `ready` deltaP `-0.0806` edge `-0.0009` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7472` n `208` status `ready` deltaP `-2.7609` edge `-0.0006` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-0.7692` n `208` status `ready` deltaP `-3.207` edge `-0.0156` maxDD `-1.9306`
- `market_context_high->crypto_major_1h` score `-0.9261` n `208` status `ready` deltaP `3.9095` edge `0.032` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-1.0753` n `208` status `ready` deltaP `-2.5939` edge `0.0066` maxDD `-2.6467`
- `market_context_high->equity_1h` score `-1.7866` n `208` status `ready` deltaP `4.3096` edge `-0.0155` maxDD `-14.716`
- `market_context_high->unknown_24h` score `-1.8073` n `200` status `ready` deltaP `-9.25` edge `0.3075` maxDD `-20.5367`
- `market_context_high->unknown_4h` score `-1.8108` n `208` status `ready` deltaP `-6.0507` edge `0.0899` maxDD `-7.3702`
- `market_context_high->index_4h` score `-1.9836` n `208` status `ready` deltaP `5.1594` edge `-0.0188` maxDD `-12.2591`
- `market_context_high->commodity_4h` score `-2.0304` n `208` status `ready` deltaP `-3.2951` edge `-0.0312` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.0462` n `208` status `ready` deltaP `4.1979` edge `0.008` maxDD `-5.5324`
- `market_context_high->commodity_24h` score `-2.2849` n `200` status `ready` deltaP `-0.2292` edge `-0.058` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.5536` n `208` status `ready` deltaP `2.7674` edge `0.0327` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.8385` n `208` status `ready` deltaP `3.9517` edge `0.0382` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.7382` n `200` status `ready` deltaP `-2.6111` edge `-0.0116` maxDD `-3.9338`
- `market_context_high->equity_4h` score `-7.2543` n `208` status `ready` deltaP `5.265` edge `-0.0781` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.2783` n `200` status `ready` deltaP `-14.1389` edge `-0.0672` maxDD `-41.9383`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
