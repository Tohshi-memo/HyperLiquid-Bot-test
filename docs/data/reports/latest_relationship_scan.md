# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T14:52:13.265539+00:00`
- Price records: `655`
- Market context records: `765`
- Flow alert records: `2159`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `13.388` n `147` status `ready` deltaP `31.7647` edge `0.9373` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.7348` n `147` status `ready` deltaP `7.3698` edge `0.5169` maxDD `-0.0508`
- `risk_on_high->metal_1h` score `1.3269` n `32` status `ready` deltaP `15.193` edge `0.0323` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.3269` n `32` status `ready` deltaP `15.193` edge `0.0323` maxDD `-0.5074`
- `market_context_high->index_24h` score `0.5695` n `147` status `ready` deltaP `3.28` edge `0.2251` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.4196` n `32` status `ready` deltaP `10.4473` edge `0.0031` maxDD `-0.1827`
- `risk_on_and_context->fx_1h` score `0.4196` n `32` status `ready` deltaP `10.4473` edge `0.0031` maxDD `-0.1827`
- `risk_on_high->commodity_1h` score `0.1929` n `32` status `ready` deltaP `6.6026` edge `0.0183` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.1929` n `32` status `ready` deltaP `6.6026` edge `0.0183` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `0.1099` n `32` status `ready` deltaP `6.8404` edge `-0.003` maxDD `-0.948`
- `risk_on_and_context->crypto_major_1h` score `0.1099` n `32` status `ready` deltaP `6.8404` edge `-0.003` maxDD `-0.948`
- `market_context_high->equity_24h` score `0.0244` n `147` status `ready` deltaP `1.8165` edge `0.2504` maxDD `-10.5047`
- `risk_on_high->index_1h` score `-0.3588` n `32` status `ready` deltaP `-1.5214` edge `0.0086` maxDD `-0.2687`
- `risk_on_and_context->index_1h` score `-0.3588` n `32` status `ready` deltaP `-1.5214` edge `0.0086` maxDD `-0.2687`
- `risk_on_high->crypto_alt_1h` score `-0.3823` n `32` status `ready` deltaP `3.6674` edge `-0.0239` maxDD `-0.9258`
- `risk_on_and_context->crypto_alt_1h` score `-0.3823` n `32` status `ready` deltaP `3.6674` edge `-0.0239` maxDD `-0.9258`
- `market_context_high->fx_4h` score `-0.4119` n `169` status `ready` deltaP `4.0106` edge `0.0076` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.4872` n `181` status `ready` deltaP `2.2809` edge `0.002` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5097` n `181` status `ready` deltaP `2.0964` edge `0.041` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5119` n `181` status `ready` deltaP `1.5345` edge `0.0095` maxDD `-2.8282`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
