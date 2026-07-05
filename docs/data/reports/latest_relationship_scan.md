# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T04:07:26.564509+00:00`
- Price records: `672`
- Market context records: `5734`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8882`

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

- `market_context_high->equity_24h` score `0.8887` n `218` status `ready` deltaP `15.5294` edge `0.5183` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1357` n `284` status `ready` deltaP `7.5554` edge `0.1248` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2061` n `285` status `ready` deltaP `3.0854` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.43` n `285` status `ready` deltaP `1.9346` edge `-0.0005` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6094` n `285` status `ready` deltaP `0.737` edge `0.0038` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6513` n `285` status `ready` deltaP `2.9126` edge `0.027` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.801` n `285` status `ready` deltaP `-2.3369` edge `-0.0064` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.8332` n `285` status `ready` deltaP `2.931` edge `0.0345` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-0.9024` n `285` status `ready` deltaP `1.7849` edge `0.0333` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.0902` n `218` status `ready` deltaP `11.3819` edge `0.0427` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1711` n `284` status `ready` deltaP `1.2131` edge `0.0105` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.244` n `284` status `ready` deltaP `2.9007` edge `0.0057` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6458` n `284` status `ready` deltaP `-7.8366` edge `-0.0494` maxDD `-11.6719`
- `market_context_high->crypto_major_4h` score `-2.7783` n `284` status `ready` deltaP `6.9049` edge `0.1413` maxDD `-24.5086`
- `market_context_high->index_24h` score `-2.9966` n `218` status `ready` deltaP `0.3584` edge `0.0279` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7201` n `284` status `ready` deltaP `-2.2737` edge `-0.0273` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.9031` n `284` status `ready` deltaP `5.0863` edge `0.0969` maxDD `-25.4852`
- `market_context_high->crypto_major_24h` score `-4.1572` n `218` status `ready` deltaP `8.0642` edge `0.0455` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.6844` n `218` status `ready` deltaP `-7.9495` edge `-0.2437` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.6072` n `218` status `ready` deltaP `-11.4424` edge `-0.077` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
