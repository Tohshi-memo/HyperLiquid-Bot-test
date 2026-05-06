# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T18:22:24.508032+00:00`
- Price records: `477`
- Market context records: `569`
- Flow alert records: `1606`
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

- `market_context_high->crypto_alt_24h` score `4.8601` n `144` status `ready` deltaP `7.4421` edge `0.3602` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `2.9614` n `144` status `ready` deltaP `9.7769` edge `0.215` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0004` n `146` status `ready` deltaP `10.0792` edge `0.02` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2988` n `146` status `ready` deltaP `2.2651` edge `0.0044` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5331` n `146` status `ready` deltaP `2.103` edge `0.039` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6516` n `146` status `ready` deltaP `0.6177` edge `-0.0023` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.126` n `146` status `ready` deltaP `-3.539` edge `-0.0099` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.233` n `146` status `ready` deltaP `-1.7277` edge `-0.0102` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3263` n `146` status `ready` deltaP `4.3413` edge `-0.008` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.8138` n `144` status `ready` deltaP `-5.6605` edge `0.0861` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.9299` n `146` status `ready` deltaP `3.9865` edge `-0.0151` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.097` n `146` status `ready` deltaP `1.1735` edge `-0.0303` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.2553` n `146` status `ready` deltaP `2.7204` edge `0.0509` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-3.1529` n `146` status `ready` deltaP `-2.7652` edge `-0.0291` maxDD `-10.5498`
- `market_context_high->crypto_major_4h` score `-3.1578` n `146` status `ready` deltaP `10.3126` edge `0.0387` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.242` n `146` status `ready` deltaP `-4.1313` edge `-0.0467` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5297` n `146` status `ready` deltaP `-5.7972` edge `0.0946` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.6678` n `144` status `ready` deltaP `-9.8806` edge `0.0207` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.5244` n `144` status `ready` deltaP `-5.3161` edge `-0.0396` maxDD `-20.0671`
- `market_context_high->unknown_4h` score `-5.3463` n `146` status `ready` deltaP `-0.0758` edge `-0.2572` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
