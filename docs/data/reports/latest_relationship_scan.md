# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T23:37:27.385873+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9132`

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

- `market_context_high->unknown_24h` score `1432.5765` n `40` status `ready` deltaP `-22.5694` edge `119.5682` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `43.0459` n `103` status `ready` deltaP `-6.6289` edge `3.6894` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.8068` n `40` status `ready` deltaP `27.6736` edge `0.5923` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4228` n `40` status `ready` deltaP `52.4306` edge `0.1857` maxDD `0.0`
- `market_context_high->unknown_1h` score `3.0203` n `115` status `ready` deltaP `-2.9979` edge `0.3053` maxDD `-1.0231`
- `market_context_high->fx_24h` score `2.9735` n `40` status `ready` deltaP `33.8194` edge `0.0353` maxDD `-0.0374`
- `risk_on_high->crypto_alt_1h` score `2.2412` n `36` status `ready` deltaP `14.5043` edge `0.1456` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `2.2412` n `36` status `ready` deltaP `14.5043` edge `0.1456` maxDD `-2.4421`
- `market_context_high->crypto_major_24h` score `1.3624` n `40` status `ready` deltaP `-21.1111` edge `0.5691` maxDD `-17.8526`
- `risk_on_high->commodity_1h` score `0.915` n `36` status `ready` deltaP `19.9102` edge `0.0029` maxDD `-0.4661`
- `risk_on_and_context->commodity_1h` score `0.915` n `36` status `ready` deltaP `19.9102` edge `0.0029` maxDD `-0.4661`
- `risk_on_high->crypto_major_1h` score `0.6401` n `36` status `ready` deltaP `8.3333` edge `0.0918` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.6401` n `36` status `ready` deltaP `8.3333` edge `0.0918` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `0.571` n `36` status `ready` deltaP `11.7931` edge `0.0185` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `0.571` n `36` status `ready` deltaP `11.7931` edge `0.0185` maxDD `-0.2466`
- `market_context_high->commodity_4h` score `0.5133` n `103` status `ready` deltaP `12.241` edge `0.0145` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `0.2302` n `115` status `ready` deltaP `5.9295` edge `0.0934` maxDD `-4.9401`
- `market_context_high->commodity_1h` score `0.1487` n `115` status `ready` deltaP `6.6493` edge `0.0031` maxDD `-0.6025`
- `market_context_high->fx_4h` score `0.0683` n `103` status `ready` deltaP `7.8676` edge `0.0055` maxDD `-0.2692`
- `risk_on_high->fx_1h` score `0.0387` n `36` status `ready` deltaP `6.171` edge `-0.0008` maxDD `-0.164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
