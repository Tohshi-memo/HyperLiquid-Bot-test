# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T16:52:30.968717+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10537`

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

- `risk_on_high->unknown_4h` score `21.8479` n `139` status `ready` deltaP `1.3818` edge `1.933` maxDD `-3.7246`
- `risk_on_and_context->unknown_4h` score `21.8479` n `139` status `ready` deltaP `1.3818` edge `1.933` maxDD `-3.7246`
- `market_context_high->unknown_4h` score `9.5254` n `228` status `ready` deltaP `3.8083` edge `0.9169` maxDD `-4.5474`
- `news_risk_high->crypto_alt_24h` score `7.1147` n `37` status `ready` deltaP `25.1783` edge `0.452` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.7733` n `37` status `ready` deltaP `19.7917` edge `0.1825` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.532` n `37` status `ready` deltaP `17.0279` edge `0.2221` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3807` n `37` status `ready` deltaP `24.1513` edge `0.0595` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8071` n `37` status `ready` deltaP `10.3618` edge `0.1016` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5584` n `37` status `ready` deltaP `12.7853` edge `0.0837` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2598` n `37` status `ready` deltaP `15.0146` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.1559` n `37` status `ready` deltaP `6.0164` edge `0.0745` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1503` n `37` status `ready` deltaP `14.4239` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_alt_1h` score `0.9597` n `37` status `ready` deltaP `9.1763` edge `0.0453` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.8923` n `37` status `ready` deltaP `16.5776` edge `0.2815` maxDD `-18.2098`
- `news_risk_high->fx_24h` score `0.6021` n `37` status `ready` deltaP `16.31` edge `0.043` maxDD `-3.1244`
- `news_risk_high->crypto_alt_4h` score `0.5753` n `37` status `ready` deltaP `5.941` edge `0.0412` maxDD `-1.296`
- `market_context_high->equity_24h` score `0.5113` n `179` status `ready` deltaP `14.0964` edge `0.3832` maxDD `-20.7654`
- `risk_on_high->index_1h` score `-0.0035` n `148` status `ready` deltaP `6.9914` edge `-0.0022` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0035` n `148` status `ready` deltaP `6.9914` edge `-0.0022` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0247` n `37` status `ready` deltaP `5.7251` edge `0.0033` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
