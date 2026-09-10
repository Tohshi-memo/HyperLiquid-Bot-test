# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T04:22:27.546559+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.6535` n `101` status `ready` deltaP `29.7717` edge `0.9623` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.6535` n `101` status `ready` deltaP `29.7717` edge `0.9623` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.4876` n `223` status `ready` deltaP `22.1661` edge `0.7256` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.239` n `101` status `ready` deltaP `37.4275` edge `0.3909` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.239` n `101` status `ready` deltaP `37.4275` edge `0.3909` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.5736` n `101` status `ready` deltaP `21.667` edge `0.9769` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.5736` n `101` status `ready` deltaP `21.667` edge `0.9769` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `5.1587` n `101` status `ready` deltaP `26.7689` edge `0.3373` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.1587` n `101` status `ready` deltaP `26.7689` edge `0.3373` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.9651` n `101` status `ready` deltaP `30.363` edge `0.0489` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9651` n `101` status `ready` deltaP `30.363` edge `0.0489` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.6281` n `223` status `ready` deltaP `14.2361` edge `0.1241` maxDD `0.0`
- `market_context_high->index_24h` score `2.3251` n `223` status `ready` deltaP `25.2616` edge `0.0647` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.1689` n `101` status `ready` deltaP `14.2361` edge `0.0025` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.1689` n `101` status `ready` deltaP `14.2361` edge `0.0025` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.1537` n `101` status `ready` deltaP `5.0068` edge `0.098` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.1537` n `101` status `ready` deltaP `5.0068` edge `0.098` maxDD `-1.1521`
- `risk_on_high->equity_4h` score `0.9642` n `101` status `ready` deltaP `19.8276` edge `-0.0176` maxDD `-1.0721`
- `risk_on_and_context->equity_4h` score `0.9642` n `101` status `ready` deltaP `19.8276` edge `-0.0176` maxDD `-1.0721`
- `risk_on_high->commodity_24h` score `0.9028` n `101` status `ready` deltaP `10.5989` edge `0.0323` maxDD `-0.5513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
