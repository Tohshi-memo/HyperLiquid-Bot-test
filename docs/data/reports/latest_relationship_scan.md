# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T08:07:16.140512+00:00`
- Price records: `672`
- Market context records: `993`
- Flow alert records: `4766`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `12.85` n `211` status `ready` deltaP `31.4378` edge `0.9201` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1375` n `211` status `ready` deltaP `10.7536` edge `0.3965` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.3522` n `211` status `ready` deltaP `1.9823` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5068` n `211` status `ready` deltaP `2.7819` edge `0.02` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6563` n `211` status `ready` deltaP `0.9563` edge `0.0158` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.6938` n `211` status `ready` deltaP `2.999` edge `0.1217` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.7439` n `211` status `ready` deltaP `0.5364` edge `0.0007` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7584` n `211` status `ready` deltaP `2.603` edge `0.0048` maxDD `-2.8282`
- `market_context_high->equity_24h` score `-1.1985` n `211` status `ready` deltaP `4.4705` edge `0.1308` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.237` n `211` status `ready` deltaP `4.5017` edge `-0.0163` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.5227` n `211` status `ready` deltaP `1.7276` edge `0.0768` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7568` n `211` status `ready` deltaP `-1.7893` edge `0.0178` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8991` n `211` status `ready` deltaP `-1.3111` edge `-0.0388` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0782` n `211` status `ready` deltaP `-0.8875` edge `-0.0233` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.9719` n `211` status `ready` deltaP `6.7713` edge `0.0778` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.2996` n `211` status `ready` deltaP `-2.1313` edge `0.056` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3559` n `211` status `ready` deltaP `-2.137` edge `0.0124` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.59` n `211` status `ready` deltaP `-1.5346` edge `-0.0221` maxDD `-20.2343`
- `market_context_high->metal_4h` score `-4.6131` n `211` status `ready` deltaP `-4.9536` edge `-0.1627` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.2824` n `211` status `ready` deltaP `2.5549` edge `0.3859` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
