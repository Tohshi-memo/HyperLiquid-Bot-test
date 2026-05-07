# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T00:07:26.124182+00:00`
- Price records: `500`
- Market context records: `594`
- Flow alert records: `1679`
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

- `market_context_high->crypto_alt_24h` score `4.5575` n `146` status `ready` deltaP `6.9884` edge `0.338` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.4353` n `146` status `ready` deltaP `10.3452` edge `0.2507` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0778` n `146` status `ready` deltaP `11.5525` edge `0.0201` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.305` n `146` status `ready` deltaP `2.1745` edge `0.0042` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6253` n `146` status `ready` deltaP `1.4005` edge `0.036` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6575` n `146` status `ready` deltaP `0.593` edge `-0.0029` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1675` n `146` status `ready` deltaP `-4.3139` edge `-0.0082` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2445` n `146` status `ready` deltaP `5.1094` edge `-0.0063` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2695` n `146` status `ready` deltaP `-2.0492` edge `-0.0111` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.8549` n `146` status `ready` deltaP `4.5487` edge `-0.0126` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.143` n `146` status `ready` deltaP `2.9095` edge `0.059` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2335` n `146` status `ready` deltaP `0.2768` edge `-0.0357` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.3843` n `146` status `ready` deltaP `-6.5822` edge `0.0447` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-2.8181` n `146` status `ready` deltaP `12.4137` edge `0.053` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2874` n `146` status `ready` deltaP `-4.5184` edge `-0.0479` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3246` n `146` status `ready` deltaP `-3.6815` edge `-0.0373` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.7929` n `146` status `ready` deltaP `-7.2117` edge `0.0821` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.3717` n `146` status `ready` deltaP `-3.7329` edge `-0.0184` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.4155` n `146` status `ready` deltaP `-10.4075` edge `-0.0381` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-5.091` n `146` status `ready` deltaP `0.4755` edge `-0.2396` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
