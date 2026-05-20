# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T04:52:21.486856+00:00`
- Price records: `672`
- Market context records: `1288`
- Flow alert records: `5619`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.5489` n `128` status `ready` deltaP `41.5798` edge `1.2984` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.7883` n `128` status `ready` deltaP `8.6806` edge `1.0912` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.19` n `128` status `ready` deltaP `26.6493` edge `0.7898` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.6487` n `128` status `ready` deltaP `29.5139` edge `0.3826` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.928` n `128` status `ready` deltaP `25.3472` edge `0.5673` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3952` n `146` status `ready` deltaP `12.2995` edge `0.1881` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3886` n `128` status `ready` deltaP `1.5625` edge `0.4616` maxDD `-10.1706`
- `market_context_high->unknown_4h` score `1.5873` n `146` status `ready` deltaP `2.675` edge `0.3333` maxDD `-10.8421`
- `market_context_high->commodity_24h` score `1.2855` n `128` status `ready` deltaP `-14.2361` edge `0.3502` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.3911` n `128` status `ready` deltaP `6.3369` edge `0.0368` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.274` n `155` status `ready` deltaP `4.3722` edge `0.0364` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1901` n `146` status `ready` deltaP `6.4442` edge `0.0877` maxDD `-3.5032`
- `market_context_high->index_1h` score `0.1178` n `155` status `ready` deltaP `6.4217` edge `0.0177` maxDD `-1.6329`
- `market_context_high->metal_4h` score `0.057` n `146` status `ready` deltaP `13.1619` edge `0.0601` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.0187` n `155` status `ready` deltaP `9.6794` edge `0.006` maxDD `-2.8509`
- `market_context_high->crypto_alt_1h` score `-0.3873` n `155` status `ready` deltaP `0.7041` edge `0.0327` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.5206` n `155` status `ready` deltaP `0.8538` edge `-0.0035` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.8099` n `155` status `ready` deltaP `-0.3689` edge `0.0007` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.8894` n `146` status `ready` deltaP `9.1254` edge `0.1571` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.9623` n `146` status `ready` deltaP `4.6525` edge `0.1165` maxDD `-13.3376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
