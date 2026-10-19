# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T12:07:29.754534+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8614`

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

- `market_context_high->commodity_24h` score `1.77` n `76` status `ready` deltaP `16.8672` edge `0.1202` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.6768` n `43` status `ready` deltaP `14.6729` edge `0.0164` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.6768` n `43` status `ready` deltaP `14.6729` edge `0.0164` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.5154` n `43` status `ready` deltaP `10.9191` edge `0.0005` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5154` n `43` status `ready` deltaP `10.9191` edge `0.0005` maxDD `-0.4273`
- `market_context_high->crypto_major_24h` score `0.3076` n `76` status `ready` deltaP `0.5299` edge `0.6456` maxDD `-35.1086`
- `market_context_high->crypto_major_1h` score `0.2157` n `77` status `ready` deltaP `3.449` edge `0.0928` maxDD `-3.7178`
- `market_context_high->crypto_major_4h` score `0.1929` n `77` status `ready` deltaP `3.3873` edge `0.3426` maxDD `-15.2359`
- `risk_on_high->equity_24h` score `0.0619` n `43` status `ready` deltaP `-21.0233` edge `0.6562` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `0.0619` n `43` status `ready` deltaP `-21.0233` edge `0.6562` maxDD `-28.5375`
- `risk_on_high->fx_4h` score `0.042` n `43` status `ready` deltaP `3.3765` edge `0.0074` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.042` n `43` status `ready` deltaP `3.3765` edge `0.0074` maxDD `-0.1126`
- `risk_on_high->commodity_24h` score `-0.0808` n `43` status `ready` deltaP `12.2467` edge `-0.0086` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.0808` n `43` status `ready` deltaP `12.2467` edge `-0.0086` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `-0.2622` n `43` status `ready` deltaP `0.2619` edge `-0.0007` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2622` n `43` status `ready` deltaP `0.2619` edge `-0.0007` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.3769` n `77` status `ready` deltaP `-0.5522` edge `0.0073` maxDD `-0.4687`
- `risk_on_high->equity_4h` score `-0.3816` n `43` status `ready` deltaP `4.6795` edge `0.0723` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `-0.3816` n `43` status `ready` deltaP `4.6795` edge `0.0723` maxDD `-4.824`
- `market_context_high->fx_4h` score `-0.4434` n `77` status `ready` deltaP `0.2656` edge `0.0051` maxDD `-0.7635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
