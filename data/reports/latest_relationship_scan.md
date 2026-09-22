# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T03:22:32.482136+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9972`

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

- `market_context_high->unknown_4h` score `48.8554` n `46` status `ready` deltaP `7.3171` edge `4.0225` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `36.5939` n `46` status `ready` deltaP `23.43` edge `2.9089` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `20.9262` n `46` status `ready` deltaP `22.2222` edge `1.5957` maxDD `0.0`
- `market_context_high->equity_24h` score `17.7624` n `46` status `ready` deltaP `16.6591` edge `1.3792` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `8.8768` n `101` status `ready` deltaP `-1.9252` edge `1.4384` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.7669` n `46` status `ready` deltaP `20.6522` edge `0.3516` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `4.4452` n `101` status `ready` deltaP `-1.5402` edge `0.8688` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `2.7758` n `101` status `ready` deltaP `13.5837` edge `0.2617` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.6975` n `101` status `ready` deltaP `33.0927` edge `0.2558` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.305` n `101` status `ready` deltaP `13.9859` edge `0.1454` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.186` n `101` status `ready` deltaP `16.3276` edge `0.1991` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9919` n `46` status `ready` deltaP `23.4689` edge `0.0229` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.6731` n `101` status `ready` deltaP `15.932` edge `0.0855` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `1.2203` n `46` status `ready` deltaP `9.2789` edge `0.0993` maxDD `-2.7574`
- `market_context_high->equity_4h` score `1.0994` n `46` status `ready` deltaP `8.2914` edge `0.067` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.8881` n `46` status `ready` deltaP `7.062` edge `0.0512` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.7049` n `101` status `ready` deltaP `13.6712` edge `0.0312` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6232` n `46` status `ready` deltaP `9.9063` edge `0.0112` maxDD `-0.0249`
- `market_context_high->crypto_major_1h` score `0.5853` n `46` status `ready` deltaP `1.3604` edge `0.092` maxDD `-2.1836`
- `news_risk_high->metal_1h` score `0.5574` n `101` status `ready` deltaP `13.9992` edge `0.0133` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
