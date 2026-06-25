# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T18:37:36.653406+00:00`
- Price records: `672`
- Market context records: `4749`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7470`

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

- `market_context_high->unknown_1h` score `82.9053` n `137` status `ready` deltaP `13.2797` edge `6.862` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.9508` n `134` status `ready` deltaP `12.4864` edge `0.5337` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.207` n `124` status `ready` deltaP `15.7482` edge `0.2546` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.3705` n `134` status `ready` deltaP `7.7676` edge `0.0076` maxDD `-5.5505`
- `market_context_high->commodity_1h` score `-0.4803` n `137` status `ready` deltaP `2.5165` edge `0.0228` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.5095` n `134` status `ready` deltaP `6.7005` edge `0.0586` maxDD `-8.8203`
- `market_context_high->fx_4h` score `-0.9336` n `134` status `ready` deltaP `-1.4447` edge `-0.0032` maxDD `-1.882`
- `market_context_high->equity_1h` score `-0.9383` n `137` status `ready` deltaP `-1.544` edge `-0.0148` maxDD `-5.2828`
- `market_context_high->fx_1h` score `-1.1972` n `137` status `ready` deltaP `-4.2397` edge `-0.005` maxDD `-0.9869`
- `market_context_high->index_1h` score `-1.4766` n `137` status `ready` deltaP `-2.3296` edge `-0.0071` maxDD `-2.6999`
- `market_context_high->commodity_4h` score `-1.5754` n `134` status `ready` deltaP `7.2283` edge `0.0176` maxDD `-9.0989`
- `market_context_high->metal_1h` score `-2.5091` n `137` status `ready` deltaP `-3.0421` edge `-0.0684` maxDD `-15.3067`
- `market_context_high->commodity_24h` score `-2.5373` n `124` status `ready` deltaP `17.1875` edge `0.071` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-2.6736` n `137` status `ready` deltaP `-0.1967` edge `-0.0436` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.1917` n `137` status `ready` deltaP `0.4207` edge `-0.0689` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-4.3505` n `124` status `ready` deltaP `-14.953` edge `-0.0209` maxDD `-4.6897`
- `market_context_high->crypto_alt_4h` score `-5.6804` n `134` status `ready` deltaP `1.6768` edge `-0.0439` maxDD `-50.3098`
- `market_context_high->index_24h` score `-7.2717` n `124` status `ready` deltaP `-11.4472` edge `-0.1093` maxDD `-23.629`
- `market_context_high->crypto_major_4h` score `-8.3757` n `134` status `ready` deltaP `1.8612` edge `-0.1497` maxDD `-69.5875`
- `market_context_high->metal_4h` score `-8.4338` n `134` status `ready` deltaP `2.9441` edge `-0.2768` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
