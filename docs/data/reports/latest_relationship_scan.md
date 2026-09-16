# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T15:07:30.441493+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11441`

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

- `news_risk_high->unknown_4h` score `368.6194` n `83` status `ready` deltaP `-21.0531` edge `30.9481` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `23.3259` n `78` status `ready` deltaP `47.7698` edge `1.6644` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.7085` n `78` status `ready` deltaP `39.7303` edge `1.6079` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.4046` n `78` status `ready` deltaP `46.0336` edge `1.0709` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.497` n `78` status `ready` deltaP `52.0432` edge `0.2954` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.1458` n `78` status `ready` deltaP `35.7104` edge `0.3195` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.5013` n `52` status `ready` deltaP `34.8958` edge `0.2258` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.5013` n `52` status `ready` deltaP `34.8958` edge `0.2258` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.2021` n `149` status `ready` deltaP `28.1844` edge `0.2148` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3693` n `52` status `ready` deltaP `31.9311` edge `-0.0112` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3693` n `52` status `ready` deltaP `31.9311` edge `-0.0112` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2344` n `149` status `ready` deltaP `29.1562` edge `0.0134` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.2084` n `52` status `ready` deltaP `28.5764` edge `0.0285` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2084` n `52` status `ready` deltaP `28.5764` edge `0.0285` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.1081` n `149` status `ready` deltaP `25.0787` edge `0.0503` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9132` n `149` status `ready` deltaP `14.2648` edge `0.0187` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.4286` n `83` status `ready` deltaP `13.1079` edge `0.0304` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.371` n `52` status `ready` deltaP `9.6975` edge `0.1444` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.371` n `52` status `ready` deltaP `9.6975` edge `0.1444` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.2899` n `52` status `ready` deltaP `7.3469` edge `0.0104` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
