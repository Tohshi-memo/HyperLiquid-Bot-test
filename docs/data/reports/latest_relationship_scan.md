# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T21:22:38.813989+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `6.8906` n `85` status `ready` deltaP `4.2002` edge `0.8522` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.7995` n `85` status `ready` deltaP `14.4786` edge `0.2777` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.5922` n `106` status `ready` deltaP `16.6762` edge `0.0888` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.532` n `85` status `ready` deltaP `12.146` edge `0.198` maxDD `-5.7715`
- `market_context_high->fx_24h` score `1.4868` n `85` status `ready` deltaP `30.2437` edge `0.0626` maxDD `-2.2217`
- `market_context_high->commodity_1h` score `1.0849` n `107` status `ready` deltaP `13.0659` edge `0.0376` maxDD `-0.7439`
- `market_context_high->equity_1h` score `0.0762` n `107` status `ready` deltaP `7.4865` edge `0.0393` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.3318` n `107` status `ready` deltaP `3.8698` edge `-0.0039` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.3845` n `107` status `ready` deltaP `-1.6691` edge `-0.0034` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5695` n `106` status `ready` deltaP `4.2108` edge `-0.0002` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.7198` n `106` status `ready` deltaP `0.9348` edge `-0.0057` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-0.8384` n `106` status `ready` deltaP `0.3452` edge `-0.0089` maxDD `-2.7373`
- `market_context_high->metal_1h` score `-0.9668` n `107` status `ready` deltaP `-3.6879` edge `-0.0064` maxDD `-0.9664`
- `market_context_high->equity_4h` score `-1.1672` n `106` status `ready` deltaP `6.8338` edge `-0.0091` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.4459` n `107` status `ready` deltaP `-6.1153` edge `-0.0168` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-2.0844` n `85` status `ready` deltaP `8.2333` edge `-0.0727` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.2205` n `107` status `ready` deltaP `-6.2245` edge `-0.0439` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.437` n `85` status `ready` deltaP `-20.1957` edge `-0.1617` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.5089` n `106` status `ready` deltaP `-5.9077` edge `-0.0882` maxDD `-6.5193`
- `market_context_high->crypto_major_4h` score `-7.317` n `106` status `ready` deltaP `-9.9488` edge `-0.194` maxDD `-18.954`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
