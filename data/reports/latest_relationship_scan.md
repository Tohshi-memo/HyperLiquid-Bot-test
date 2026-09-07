# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T11:07:25.193224+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10429`

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

- `risk_on_high->unknown_24h` score `418.0863` n `93` status `ready` deltaP `26.3889` edge `34.6646` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `418.0863` n `93` status `ready` deltaP `26.3889` edge `34.6646` maxDD `0.0`
- `market_context_high->unknown_1h` score `24.1656` n `241` status `ready` deltaP `-2.3778` edge `2.1021` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `22.13` n `93` status `ready` deltaP `37.7184` edge `1.6444` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.13` n `93` status `ready` deltaP `37.7184` edge `1.6444` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.0697` n `93` status `ready` deltaP `31.7708` edge `1.044` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.0697` n `93` status `ready` deltaP `31.7708` edge `1.044` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.1405` n `188` status `ready` deltaP `24.8559` edge `0.6535` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.1019` n `188` status `ready` deltaP `20.8333` edge `0.3696` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.5002` n `117` status `ready` deltaP `29.568` edge `0.2984` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.5002` n `117` status `ready` deltaP `29.568` edge `0.2984` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `4.9703` n `93` status `ready` deltaP `20.8333` edge `0.2753` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.9703` n `93` status `ready` deltaP `20.8333` edge `0.2753` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3821` n `117` status `ready` deltaP `24.4567` edge `0.288` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3821` n `117` status `ready` deltaP `24.4567` edge `0.288` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.4617` n `93` status `ready` deltaP `20.9061` edge `0.07` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.4617` n `93` status `ready` deltaP `20.9061` edge `0.07` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.2357` n `188` status `ready` deltaP `18.2808` edge `0.0859` maxDD `-0.0505`
- `risk_on_high->crypto_alt_1h` score `0.9716` n `117` status `ready` deltaP `4.6958` edge `0.0849` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9716` n `117` status `ready` deltaP `4.6958` edge `0.0849` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
