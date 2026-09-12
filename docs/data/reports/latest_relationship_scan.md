# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T18:37:28.959610+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12827`

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

- `market_context_high->unknown_24h` score `8894.4403` n `81` status `ready` deltaP `12.9823` edge `741.122` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `6207.0565` n `41` status `ready` deltaP `15.4514` edge `517.1517` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `6207.0565` n `41` status `ready` deltaP `15.4514` edge `517.1517` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.3848` n `82` status `ready` deltaP `-5.4002` edge `32.0269` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `20.7217` n `69` status `ready` deltaP `46.324` edge `1.5376` maxDD `-6.9028`
- `news_risk_high->crypto_alt_24h` score `17.1988` n `69` status `ready` deltaP `29.8837` edge `1.2828` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `16.2289` n `41` status `ready` deltaP `37.9785` edge `1.1222` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.2289` n `41` status `ready` deltaP `37.9785` edge `1.1222` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.2052` n `81` status `ready` deltaP `30.4205` edge `1.0637` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `9.8234` n `41` status `ready` deltaP `41.4931` edge `0.542` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.8234` n `41` status `ready` deltaP `41.4931` edge `0.542` maxDD `0.0`
- `market_context_high->equity_24h` score `9.4718` n `81` status `ready` deltaP `41.4931` edge `0.5127` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.1961` n `69` status `ready` deltaP `24.1018` edge `0.6864` maxDD `-3.1258`
- `risk_on_high->crypto_alt_4h` score `8.0396` n `47` status `ready` deltaP `39.965` edge `0.4407` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.0396` n `47` status `ready` deltaP `39.965` edge `0.4407` maxDD `-1.9733`
- `news_risk_high->index_24h` score `6.6973` n `69` status `ready` deltaP `43.9009` edge `0.2831` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `6.445` n `69` status `ready` deltaP `41.1232` edge `0.307` maxDD `-0.526`
- `risk_on_high->index_24h` score `4.925` n `41` status `ready` deltaP `49.6273` edge `0.0838` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.925` n `41` status `ready` deltaP `49.6273` edge `0.0838` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `3.7646` n `47` status `ready` deltaP `32.6608` edge `0.1053` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
