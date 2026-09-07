# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T16:52:32.799543+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10441`

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

- `risk_on_high->unknown_24h` score `302.4853` n `99` status `ready` deltaP `23.6111` edge `25.0497` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `302.4853` n `99` status `ready` deltaP `23.6111` edge `25.0497` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `19.0783` n `99` status `ready` deltaP `34.1541` edge `1.4723` maxDD `-6.1443`
- `risk_on_and_context->crypto_major_24h` score `19.0783` n `99` status `ready` deltaP `34.1541` edge `1.4723` maxDD `-6.1443`
- `risk_on_high->crypto_alt_24h` score `13.8212` n `99` status `ready` deltaP `31.4552` edge `0.9482` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `13.8212` n `99` status `ready` deltaP `31.4552` edge `0.9482` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `7.8423` n `211` status `ready` deltaP `24.4084` edge `0.5483` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.5676` n `117` status `ready` deltaP `29.7204` edge `0.303` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.5676` n `117` status `ready` deltaP `29.7204` edge `0.303` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.8967` n `117` status `ready` deltaP `26.1335` edge `0.3197` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8967` n `117` status `ready` deltaP `26.1335` edge `0.3197` maxDD `-3.8693`
- `market_context_high->equity_24h` score `4.4984` n `211` status `ready` deltaP `16.8403` edge `0.2626` maxDD `0.0`
- `risk_on_high->equity_24h` score `3.7784` n `99` status `ready` deltaP `16.8403` edge `0.2026` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.7784` n `99` status `ready` deltaP `16.8403` edge `0.2026` maxDD `0.0`
- `risk_on_high->index_24h` score `2.0943` n `99` status `ready` deltaP `18.3239` edge `0.0566` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.0943` n `99` status `ready` deltaP `18.3239` edge `0.0566` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.3372` n `211` status `ready` deltaP `12.8234` edge `0.0653` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `1.004` n `117` status `ready` deltaP `4.6958` edge `0.0876` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.004` n `117` status `ready` deltaP `4.6958` edge `0.0876` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6706` n `99` status `ready` deltaP `16.8087` edge `0.0895` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
