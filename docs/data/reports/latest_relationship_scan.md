# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T04:22:32.835389+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6587`

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

- `market_context_high->equity_24h` score `10.5883` n `32` status `ready` deltaP `17.3611` edge `1.0039` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.7346` n `32` status `ready` deltaP `8.8542` edge `0.2276` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.4691` n `32` status `ready` deltaP `17.5347` edge `0.1177` maxDD `-2.3671`
- `market_context_high->metal_1h` score `0.909` n `73` status `ready` deltaP `11.3444` edge `0.0329` maxDD `-0.6226`
- `market_context_high->metal_4h` score `0.8097` n `61` status `ready` deltaP `11.1505` edge `0.082` maxDD `-1.2025`
- `market_context_high->equity_1h` score `0.736` n `73` status `ready` deltaP `2.9304` edge `0.1615` maxDD `-5.5762`
- `market_context_high->fx_24h` score `0.6808` n `32` status `ready` deltaP `10.7639` edge `-0.0062` maxDD `-0.0397`
- `market_context_high->commodity_4h` score `0.5841` n `61` status `ready` deltaP `3.7185` edge `0.0711` maxDD `-1.1102`
- `market_context_high->commodity_1h` score `0.2489` n `73` status `ready` deltaP `8.5227` edge `0.0227` maxDD `-1.7019`
- `market_context_high->index_4h` score `0.2136` n `61` status `ready` deltaP `13.3246` edge `0.0314` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.2279` n `73` status `ready` deltaP `2.631` edge `0.0218` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.5857` n `73` status `ready` deltaP `10.4831` edge `0.0443` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-0.8988` n `73` status `ready` deltaP `-10.8276` edge `-0.0036` maxDD `-0.4893`
- `market_context_high->fx_4h` score `-1.4922` n `61` status `ready` deltaP `-7.2221` edge `-0.0049` maxDD `-1.3941`
- `market_context_high->metal_24h` score `-1.5352` n `32` status `ready` deltaP `0.8681` edge `-0.1473` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-1.7597` n `73` status `ready` deltaP `3.2073` edge `-0.0371` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-1.8267` n `61` status `ready` deltaP `8.9389` edge `0.0842` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-4.6726` n `32` status `ready` deltaP `-4.8611` edge `0.0073` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-6.5299` n `61` status `ready` deltaP `7.9069` edge `-0.13` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-8.9638` n `32` status `ready` deltaP `-18.75` edge `-0.1641` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
