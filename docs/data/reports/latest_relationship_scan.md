# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T10:52:21.108359+00:00`
- Price records: `543`
- Market context records: `639`
- Flow alert records: `1810`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_major_24h` score `6.3818` n `146` status `ready` deltaP `17.7316` edge `0.447` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.7155` n `146` status `ready` deltaP `8.2636` edge `0.426` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1066` n `146` status `ready` deltaP `8.6972` edge `0.0155` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3491` n `146` status `ready` deltaP `1.5222` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5316` n `146` status `ready` deltaP `1.777` edge `0.0413` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6793` n `146` status `ready` deltaP `0.0243` edge `-0.0019` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.135` n `146` status `ready` deltaP `-4.1172` edge `-0.0068` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1731` n `146` status `ready` deltaP `5.942` edge `-0.0059` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3052` n `146` status `ready` deltaP `-2.4056` edge `-0.0117` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6655` n `146` status `ready` deltaP `5.9712` edge `-0.0063` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1164` n `146` status `ready` deltaP `3.7964` edge `0.0553` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.3415` n `146` status `ready` deltaP `-1.0883` edge `-0.0356` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.5241` n `146` status `ready` deltaP `13.284` edge `0.0717` maxDD `-22.648`
- `market_context_high->index_24h` score `-3.0253` n `146` status `ready` deltaP `-8.6691` edge `0.0052` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.3285` n `146` status `ready` deltaP `-5.1415` edge `0.107` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.4384` n `146` status `ready` deltaP `-5.1453` edge `-0.0563` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.4813` n `146` status `ready` deltaP `-4.53` edge `-0.0447` maxDD `-10.5498`
- `market_context_high->fx_24h` score `-4.3915` n `146` status `ready` deltaP `-3.9643` edge `-0.0194` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.8126` n `146` status `ready` deltaP `1.2698` edge `-0.2217` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.8478` n `146` status `ready` deltaP `-11.7907` edge `-0.0649` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
