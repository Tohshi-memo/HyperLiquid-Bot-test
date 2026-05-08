# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T14:37:18.558128+00:00`
- Price records: `654`
- Market context records: `764`
- Flow alert records: `2155`
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

- `market_context_high->crypto_major_24h` score `13.3711` n `147` status `ready` deltaP `31.6583` edge `0.9366` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.7551` n `147` status `ready` deltaP `7.3842` edge `0.5185` maxDD `-0.0508`
- `risk_on_high->metal_1h` score `1.3128` n `32` status `ready` deltaP `15.1058` edge `0.0317` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.3128` n `32` status `ready` deltaP `15.1058` edge `0.0317` maxDD `-0.5074`
- `market_context_high->index_24h` score `0.5692` n `147` status `ready` deltaP `3.3362` edge `0.2247` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.4232` n `32` status `ready` deltaP `10.5166` edge `0.0031` maxDD `-0.1827`
- `risk_on_and_context->fx_1h` score `0.4232` n `32` status `ready` deltaP `10.5166` edge `0.0031` maxDD `-0.1827`
- `risk_on_high->commodity_1h` score `0.2026` n `32` status `ready` deltaP `6.6854` edge `0.019` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2026` n `32` status `ready` deltaP `6.6854` edge `0.019` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `0.1207` n `32` status `ready` deltaP `6.9135` edge `-0.0021` maxDD `-0.948`
- `risk_on_and_context->crypto_major_1h` score `0.1207` n `32` status `ready` deltaP `6.9135` edge `-0.0021` maxDD `-0.948`
- `market_context_high->equity_24h` score `0.027` n `147` status `ready` deltaP `1.864` edge `0.2503` maxDD `-10.5047`
- `risk_on_high->crypto_alt_1h` score `-0.3616` n `32` status `ready` deltaP `3.7308` edge `-0.0226` maxDD `-0.9258`
- `risk_on_and_context->crypto_alt_1h` score `-0.3616` n `32` status `ready` deltaP `3.7308` edge `-0.0226` maxDD `-0.9258`
- `risk_on_high->index_1h` score `-0.3676` n `32` status `ready` deltaP `-1.6157` edge `0.0085` maxDD `-0.2687`
- `risk_on_and_context->index_1h` score `-0.3676` n `32` status `ready` deltaP `-1.6157` edge `0.0085` maxDD `-0.2687`
- `market_context_high->fx_4h` score `-0.3969` n `168` status `ready` deltaP `4.2681` edge `0.0078` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.4956` n `180` status `ready` deltaP `1.7871` edge `0.0099` maxDD `-2.8282`
- `market_context_high->fx_1h` score `-0.5005` n `180` status `ready` deltaP `2.1138` edge `0.002` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5439` n `180` status `ready` deltaP `1.8937` edge `0.0395` maxDD `-3.7959`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
