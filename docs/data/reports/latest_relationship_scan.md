# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T08:23:06.425571+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10224`

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

- `risk_on_high->crypto_alt_24h` score `7.6221` n `117` status `ready` deltaP `19.164` edge `0.5304` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `7.6221` n `117` status `ready` deltaP `19.164` edge `0.5304` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.3276` n `117` status `ready` deltaP `30.635` edge `0.2769` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3276` n `117` status `ready` deltaP `30.635` edge `0.2769` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `3.8521` n `117` status `ready` deltaP `17.1074` edge `0.7866` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `3.8521` n `117` status `ready` deltaP `17.1074` edge `0.7866` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `3.3879` n `117` status `ready` deltaP `21.1031` edge `0.2275` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.3879` n `117` status `ready` deltaP `21.1031` edge `0.2275` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `2.5747` n `241` status `ready` deltaP `11.8192` edge `0.2185` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.6784` n `117` status `ready` deltaP `18.2692` edge `0.0223` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.6784` n `117` status `ready` deltaP `18.2692` edge `0.0223` maxDD `-0.0051`
- `market_context_high->index_24h` score `0.9569` n `241` status `ready` deltaP `13.3644` edge `0.03` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.829` n `117` status `ready` deltaP `3.4982` edge `0.081` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.829` n `117` status `ready` deltaP `3.4982` edge `0.081` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.2848` n `117` status `ready` deltaP `17.6549` edge `0.0344` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.2848` n `117` status `ready` deltaP `17.6549` edge `0.0344` maxDD `-0.9131`
- `risk_on_high->metal_1h` score `0.1243` n `117` status `ready` deltaP `7.5836` edge `-0.0016` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1243` n `117` status `ready` deltaP `7.5836` edge `-0.0016` maxDD `-0.3081`
- `risk_on_high->index_1h` score `0.118` n `117` status `ready` deltaP `8.5202` edge `-0.0053` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.118` n `117` status `ready` deltaP `8.5202` edge `-0.0053` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
