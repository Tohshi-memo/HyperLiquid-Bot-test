# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T06:22:14.360521+00:00`
- Price records: `525`
- Market context records: `621`
- Flow alert records: `1755`
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

- `market_context_high->crypto_alt_24h` score `5.2095` n `146` status `ready` deltaP `7.4736` edge `0.3891` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `5.0784` n `146` status `ready` deltaP `14.6246` edge `0.3591` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.093` n `146` status `ready` deltaP `8.9123` edge `0.0158` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3254` n `146` status `ready` deltaP `1.917` edge `0.0033` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6035` n `146` status `ready` deltaP `1.5235` edge `0.037` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7085` n `146` status `ready` deltaP `-0.3564` edge `-0.0031` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.0485` n `146` status `ready` deltaP `-3.2761` edge `-0.0052` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1618` n `146` status `ready` deltaP `5.8423` edge `-0.0043` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3079` n `146` status `ready` deltaP `-2.484` edge `-0.0114` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.6398` n `146` status `ready` deltaP `4.9237` edge `0.0875` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.6945` n `146` status `ready` deltaP `5.6543` edge `-0.0066` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-2.2501` n `146` status `ready` deltaP `14.3539` edge `0.0874` maxDD `-22.648`
- `market_context_high->index_4h` score `-2.317` n `146` status `ready` deltaP `-0.8721` edge `-0.035` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.8047` n `146` status `ready` deltaP `-7.8469` edge `0.0181` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.2698` n `146` status `ready` deltaP `-3.4464` edge `-0.0343` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3159` n `146` status `ready` deltaP `-4.6499` edge `-0.0494` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.712` n `146` status `ready` deltaP `-6.5455` edge `0.0844` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2723` n `146` status `ready` deltaP `-2.527` edge `-0.0137` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.6319` n `146` status `ready` deltaP `2.5984` edge `-0.2155` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.7802` n `146` status `ready` deltaP `-11.2457` edge `-0.0629` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
