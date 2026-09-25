# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T00:22:31.550405+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10157`

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

- `market_context_high->unknown_1h` score `83.8724` n `47` status `ready` deltaP `9.5172` edge `6.933` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.0837` n `47` status `ready` deltaP `30.4226` edge `3.7601` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.0408` n `47` status `ready` deltaP `24.782` edge `2.4595` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.7474` n `47` status `ready` deltaP `34.242` edge `1.9529` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `10.0797` n `114` status `ready` deltaP `-1.1398` edge `0.872` maxDD `-0.9543`
- `market_context_high->index_24h` score `8.1506` n `47` status `ready` deltaP `37.8878` edge `0.4396` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3946` n `47` status `ready` deltaP `36.9681` edge `0.1436` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3858` n `68` status `ready` deltaP `31.5257` edge `0.1068` maxDD `-1.7857`
- `news_risk_high->crypto_alt_1h` score `2.9523` n `114` status `ready` deltaP `15.4297` edge `0.1941` maxDD `-1.7416`
- `market_context_high->index_4h` score `2.9353` n `47` status `ready` deltaP `33.7215` edge `0.0352` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.4143` n `47` status `ready` deltaP `17.1445` edge `0.1287` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.0432` n `114` status `ready` deltaP `15.343` edge `0.1239` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.2271` n `114` status `ready` deltaP `16.601` edge `0.0201` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.9451` n `47` status `ready` deltaP `14.4604` edge `0.0102` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8899` n `47` status `ready` deltaP `11.167` edge `0.04` maxDD `-1.5564`
- `news_risk_high->fx_4h` score `0.8409` n `102` status `ready` deltaP `15.7909` edge `0.0284` maxDD `-0.421`
- `market_context_high->crypto_alt_4h` score `0.2367` n `47` status `ready` deltaP `6.9441` edge `0.0402` maxDD `-3.3417`
- `news_risk_high->crypto_major_4h` score `0.2327` n `102` status `ready` deltaP `10.5063` edge `0.1625` maxDD `-13.719`
- `market_context_high->fx_1h` score `0.2038` n `47` status `ready` deltaP `7.1155` edge `0.0052` maxDD `-0.1854`
- `news_risk_high->metal_24h` score `0.1124` n `68` status `ready` deltaP `18.3824` edge `0.0367` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
