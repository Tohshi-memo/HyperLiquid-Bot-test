# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T12:07:11.292285+00:00`
- Price records: `548`
- Market context records: `644`
- Flow alert records: `1826`
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

- `market_context_high->crypto_major_24h` score `6.8889` n `146` status `ready` deltaP `18.5507` edge `0.4838` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.9623` n `146` status `ready` deltaP `8.8284` edge `0.4428` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.14` n `146` status `ready` deltaP `8.2192` edge `0.0144` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3313` n `146` status `ready` deltaP `1.8493` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4542` n `146` status `ready` deltaP `2.2045` edge `0.0449` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6765` n `146` status `ready` deltaP `0.033` edge `-0.0016` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1593` n `146` status `ready` deltaP `-4.3614` edge `-0.0072` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2192` n `146` status `ready` deltaP `5.5601` edge `-0.0072` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2783` n `146` status `ready` deltaP `-2.1892` edge `-0.0109` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6909` n `146` status `ready` deltaP `5.7287` edge `-0.0068` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0605` n `146` status `ready` deltaP `4.0607` edge `0.0582` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2602` n `146` status `ready` deltaP `-0.4618` edge `-0.033` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.4104` n `146` status `ready` deltaP `13.8351` edge `0.0775` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9323` n `146` status `ready` deltaP `-8.6626` edge `0.0129` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.2794` n `146` status `ready` deltaP `-4.7686` edge `0.1086` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.4065` n `146` status `ready` deltaP `-4.0603` edge `-0.0416` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4483` n `146` status `ready` deltaP `-5.1647` edge `-0.057` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.4547` n `146` status `ready` deltaP `-4.715` edge `-0.0225` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6629` n `146` status `ready` deltaP `-11.2646` edge `-0.053` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8337` n `146` status `ready` deltaP `0.9166` edge `-0.2211` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
