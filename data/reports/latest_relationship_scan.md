# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T16:22:36.441468+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9834`

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

- `market_context_high->unknown_4h` score `46.4898` n `46` status `ready` deltaP `7.0122` edge `3.8274` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `30.3085` n `46` status `ready` deltaP `14.4022` edge `2.4453` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.262` n `46` status `ready` deltaP `12.3189` edge `1.2831` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.4511` n `46` status `ready` deltaP `13.8889` edge `1.195` maxDD `0.0`
- `market_context_high->index_24h` score `5.5572` n `46` status `ready` deltaP `20.1314` edge `0.3376` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `3.1186` n `101` status `ready` deltaP `37.6065` edge `0.2797` maxDD `-3.4467`
- `news_risk_high->crypto_major_24h` score `2.5914` n `101` status `ready` deltaP `-10.953` edge `0.9748` maxDD `-46.1999`
- `news_risk_high->crypto_alt_1h` score `2.04` n `101` status `ready` deltaP `12.7883` edge `0.1313` maxDD `-2.058`
- `news_risk_high->crypto_alt_4h` score `1.8803` n `101` status `ready` deltaP `10.5349` edge `0.2074` maxDD `-7.675`
- `market_context_high->index_4h` score `1.874` n `46` status `ready` deltaP `22.2494` edge `0.0212` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.3123` n `101` status `ready` deltaP `13.9859` edge `0.0684` maxDD `-2.8494`
- `news_risk_high->crypto_major_4h` score `1.2257` n `101` status `ready` deltaP `13.2788` edge `0.1394` maxDD `-8.0625`
- `market_context_high->metal_24h` score `1.155` n `46` status `ready` deltaP `23.1356` edge `-0.0346` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.1184` n `101` status `ready` deltaP `17.9395` edge `0.0372` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.8424` n `46` status `ready` deltaP `7.3614` edge `0.0454` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.7234` n `46` status `ready` deltaP `6.1572` edge `0.0499` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6842` n `46` status `ready` deltaP `10.8045` edge `0.0103` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6568` n `101` status `ready` deltaP `15.1968` edge `0.0136` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.5516` n `101` status `ready` deltaP `19.3258` edge `0.0263` maxDD `-2.4203`
- `news_risk_high->fx_24h` score `0.3986` n `101` status `ready` deltaP `18.5935` edge `0.0861` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
