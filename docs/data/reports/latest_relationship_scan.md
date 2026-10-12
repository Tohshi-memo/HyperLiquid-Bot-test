# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T00:22:26.068003+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9488`

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

- `market_context_high->unknown_24h` score `1369.6541` n `41` status `ready` deltaP `-21.9596` edge `114.3206` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `40.8794` n `106` status `ready` deltaP `-8.3698` edge `3.5288` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.9563` n `41` status `ready` deltaP `28.2224` edge `0.6011` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4084` n `41` status `ready` deltaP `52.4306` edge `0.1845` maxDD `0.0`
- `market_context_high->fx_24h` score `2.76` n `41` status `ready` deltaP `31.3897` edge `0.0337` maxDD `-0.0374`
- `risk_on_high->crypto_alt_1h` score `2.4929` n `39` status `ready` deltaP `16.8548` edge `0.1509` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `2.4929` n `39` status `ready` deltaP `16.8548` edge `0.1509` maxDD `-2.4421`
- `market_context_high->unknown_1h` score `2.2833` n `118` status `ready` deltaP `-3.1209` edge `0.2447` maxDD `-1.0231`
- `market_context_high->crypto_major_24h` score `1.8775` n `41` status `ready` deltaP `-19.0379` edge `0.5982` maxDD `-17.8526`
- `risk_on_high->crypto_major_1h` score `1.3036` n `39` status `ready` deltaP `11.5385` edge `0.097` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.3036` n `39` status `ready` deltaP `11.5385` edge `0.097` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `1.1607` n `39` status `ready` deltaP `14.5709` edge `0.0235` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.1607` n `39` status `ready` deltaP `14.5709` edge `0.0235` maxDD `-0.2466`
- `risk_on_high->equity_1h` score `0.3849` n `39` status `ready` deltaP `2.8367` edge `0.0377` maxDD `-0.296`
- `risk_on_and_context->equity_1h` score `0.3849` n `39` status `ready` deltaP `2.8367` edge `0.0377` maxDD `-0.296`
- `market_context_high->crypto_alt_1h` score `0.3077` n `118` status `ready` deltaP `6.9243` edge `0.0967` maxDD `-4.9401`
- `risk_on_high->commodity_1h` score `0.2211` n `39` status `ready` deltaP `14.141` edge `-0.0253` maxDD `-1.583`
- `risk_on_and_context->commodity_1h` score `0.2211` n `39` status `ready` deltaP `14.141` edge `-0.0253` maxDD `-1.583`
- `market_context_high->commodity_4h` score `0.221` n `106` status `ready` deltaP `10.2076` edge `0.0037` maxDD `-1.6002`
- `market_context_high->metal_4h` score `0.0565` n `106` status `ready` deltaP `8.3669` edge `0.0212` maxDD `-1.1153`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
