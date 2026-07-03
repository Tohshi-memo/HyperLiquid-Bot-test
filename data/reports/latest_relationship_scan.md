# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T23:39:24.785222+00:00`
- Price records: `672`
- Market context records: `5607`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11433`

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

- `market_context_high->equity_24h` score `3.3919` n `174` status `ready` deltaP `15.0084` edge `0.6905` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.4716` n `219` status `ready` deltaP `13.4668` edge `0.2621` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.219` n `174` status `ready` deltaP `21.2644` edge `0.0572` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.8425` n `219` status `ready` deltaP `8.7434` edge `0.176` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.4471` n `219` status `ready` deltaP `6.0029` edge `0.1611` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.3126` n `231` status `ready` deltaP `6.0665` edge `0.0342` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.3564` n `231` status `ready` deltaP `0.1841` edge `0.0007` maxDD `-0.4764`
- `market_context_high->metal_1h` score `-0.516` n `231` status `ready` deltaP `0.0991` edge `0.0007` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.6351` n `231` status `ready` deltaP `3.9791` edge `0.0451` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.6383` n `231` status `ready` deltaP `0.8192` edge `0.0375` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.8755` n `231` status `ready` deltaP `1.1672` edge `0.0061` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.1978` n `231` status `ready` deltaP `-2.5145` edge `-0.0065` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1987` n `219` status `ready` deltaP `1.136` edge `0.0073` maxDD `-1.1505`
- `market_context_high->crypto_major_24h` score `-1.3823` n `174` status `ready` deltaP `9.9797` edge `0.2723` maxDD `-29.6555`
- `market_context_high->index_4h` score `-1.6293` n `219` status `ready` deltaP `1.8974` edge `0.0125` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.3847` n `174` status `ready` deltaP `10.0874` edge `0.0257` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8713` n `219` status `ready` deltaP `-11.1837` edge `-0.0552` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.2092` n `219` status `ready` deltaP `-6.0022` edge `-0.0432` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.1964` n `174` status `ready` deltaP `-9.8898` edge `-0.2488` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-11.4044` n `174` status `ready` deltaP `-0.2335` edge `-0.0791` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
