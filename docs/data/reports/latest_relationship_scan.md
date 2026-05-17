# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T10:22:15.911682+00:00`
- Price records: `672`
- Market context records: `1003`
- Flow alert records: `4794`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `12.9921` n `209` status `ready` deltaP `31.8788` edge `0.929` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.183` n `209` status `ready` deltaP `10.9024` edge `0.3993` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.3544` n `209` status `ready` deltaP `1.9096` edge `-0.0001` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5677` n `209` status `ready` deltaP `2.3057` edge `0.0181` maxDD `-3.7959`
- `market_context_high->index_24h` score `-0.661` n `209` status `ready` deltaP `3.3195` edge `0.1212` maxDD `-5.8728`
- `market_context_high->equity_1h` score `-0.6649` n `209` status `ready` deltaP `0.7886` edge `0.0162` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.7132` n `209` status `ready` deltaP `3.0928` edge `0.0053` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.7447` n `209` status `ready` deltaP `0.4901` edge `0.0009` maxDD `-1.6381`
- `market_context_high->equity_24h` score `-1.201` n `209` status `ready` deltaP `4.6032` edge `0.1297` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.2108` n `209` status `ready` deltaP `5.0504` edge `-0.0166` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3479` n `209` status `ready` deltaP `-0.8466` edge `-0.0232` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.5069` n `209` status `ready` deltaP `1.85` edge `0.0773` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7482` n `209` status `ready` deltaP `-1.6975` edge `0.0179` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8561` n `209` status `ready` deltaP `-0.5443` edge `-0.0384` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.918` n `209` status `ready` deltaP `7.0246` edge `0.0806` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.2295` n `209` status `ready` deltaP `-1.749` edge `0.0593` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3119` n `209` status `ready` deltaP `-2.0228` edge `0.0153` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.5247` n `209` status `ready` deltaP `-1.7628` edge `-0.0227` maxDD `-20.061`
- `market_context_high->metal_4h` score `-4.6201` n `209` status `ready` deltaP `-4.8334` edge `-0.1644` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.1785` n `209` status `ready` deltaP `2.7525` edge `0.3979` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
