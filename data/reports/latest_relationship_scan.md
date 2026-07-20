# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T03:22:25.777905+00:00`
- Price records: `672`
- Market context records: `7314`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14831`

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

- `risk_on_high->crypto_major_1h` score `1.2589` n `32` status `ready` deltaP `19.9289` edge `0.053` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2589` n `32` status `ready` deltaP `19.9289` edge `0.053` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.242` n `32` status `ready` deltaP `4.5045` edge `0.0387` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.242` n `32` status `ready` deltaP `4.5045` edge `0.0387` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.2151` n `32` status `ready` deltaP `3.9977` edge `0.0192` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2151` n `32` status `ready` deltaP `3.9977` edge `0.0192` maxDD `-0.2339`
- `risk_on_high->crypto_alt_1h` score `0.083` n `32` status `ready` deltaP `-0.1497` edge `0.0487` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.083` n `32` status `ready` deltaP `-0.1497` edge `0.0487` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.2089` n `129` status `ready` deltaP `3.3382` edge `-0.0001` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5355` n `124` status `ready` deltaP `6.6181` edge `0.1231` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7362` n `129` status `ready` deltaP `-3.4151` edge `-0.0144` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7523` n `129` status `ready` deltaP `-4.4102` edge `-0.0062` maxDD `-1.868`
- `market_context_high->fx_24h` score `-0.7785` n `111` status `ready` deltaP `3.0877` edge `0.0024` maxDD `-2.1564`
- `market_context_high->crypto_major_1h` score `-0.8301` n `129` status `ready` deltaP `3.0927` edge `0.014` maxDD `-7.6171`
- `market_context_high->commodity_4h` score `-0.9512` n `124` status `ready` deltaP `-0.9758` edge `-0.0186` maxDD `-2.4139`
- `risk_on_high->index_1h` score `-0.9563` n `32` status `ready` deltaP `-14.2455` edge `0.0052` maxDD `-0.2932`
- `risk_on_and_context->index_1h` score `-0.9563` n `32` status `ready` deltaP `-14.2455` edge `0.0052` maxDD `-0.2932`
- `market_context_high->crypto_alt_1h` score `-1.1308` n `129` status `ready` deltaP `-1.3125` edge `0.0184` maxDD `-5.9775`
- `market_context_high->fx_4h` score `-1.1419` n `124` status `ready` deltaP `1.0826` edge `0.007` maxDD `-1.516`
- `risk_on_high->unknown_1h` score `-1.1888` n `32` status `ready` deltaP `-3.5554` edge `-0.0805` maxDD `-0.8568`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
