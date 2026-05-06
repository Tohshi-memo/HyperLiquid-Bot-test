# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T21:07:15.201710+00:00`
- Price records: `488`
- Market context records: `581`
- Flow alert records: `1640`
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

- `market_context_high->crypto_alt_24h` score `4.7274` n `146` status `ready` deltaP `7.2233` edge `0.3506` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0475` n `146` status `ready` deltaP `9.6379` edge `0.2231` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0624` n `146` status `ready` deltaP `11.2107` edge `0.0204` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2871` n `146` status `ready` deltaP `2.4743` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5946` n `146` status `ready` deltaP `1.6952` edge `0.0366` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6896` n `146` status `ready` deltaP `0.1256` edge `-0.0039` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1807` n `146` status `ready` deltaP `-4.4039` edge `-0.0087` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2737` n `146` status `ready` deltaP `4.8795` edge `-0.0072` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3053` n `146` status `ready` deltaP `-2.1661` edge `-0.0133` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.9208` n `146` status `ready` deltaP `4.0105` edge `-0.0145` maxDD `-11.4508`
- `market_context_high->index_24h` score `-2.0527` n `146` status `ready` deltaP `-5.9173` edge `0.0679` maxDD `-5.9609`
- `market_context_high->crypto_alt_4h` score `-2.1282` n `146` status `ready` deltaP `3.2737` edge `0.0578` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.244` n `146` status `ready` deltaP `0.3249` edge `-0.0369` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.9615` n `146` status `ready` deltaP `11.5364` edge `0.0469` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2925` n `146` status `ready` deltaP `-4.4917` edge `-0.0485` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3622` n `146` status `ready` deltaP `-3.5212` edge `-0.0415` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.5648` n `146` status `ready` deltaP `-5.7107` edge `0.0911` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.025` n `146` status `ready` deltaP `-9.9668` edge `-0.0085` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.537` n `146` status `ready` deltaP `-4.7381` edge `-0.0329` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.0594` n `146` status `ready` deltaP `1.4105` edge `-0.2432` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
