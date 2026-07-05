# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T02:22:28.660237+00:00`
- Price records: `672`
- Market context records: `5727`
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

- `market_context_high->equity_24h` score `0.9314` n `218` status `ready` deltaP `16.0503` edge `0.5203` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1439` n `277` status `ready` deltaP `7.2235` edge `0.1277` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2381` n `285` status `ready` deltaP `2.4866` edge `0.001` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4471` n `285` status `ready` deltaP `1.6352` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.625` n `285` status `ready` deltaP `3.212` edge `0.0272` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.625` n `285` status `ready` deltaP `0.4376` edge `0.0038` maxDD `-0.9472`
- `market_context_high->crypto_major_4h` score `-0.6389` n `277` status `ready` deltaP `8.2829` edge `0.1693` maxDD `-15.5543`
- `market_context_high->commodity_1h` score `-0.7699` n `285` status `ready` deltaP `-1.8878` edge `-0.0054` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.8596` n `285` status `ready` deltaP `2.7813` edge `0.0333` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-1.0043` n `285` status `ready` deltaP `1.0364` edge `0.0298` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.1302` n `218` status `ready` deltaP `10.6875` edge `0.0422` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1382` n `277` status `ready` deltaP `1.8007` edge `0.0108` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2553` n `277` status `ready` deltaP `2.6833` edge `0.0057` maxDD `-1.4288`
- `market_context_high->crypto_alt_4h` score `-2.0699` n `277` status `ready` deltaP `6.1328` edge `0.1184` maxDD `-17.8757`
- `market_context_high->metal_4h` score `-2.6003` n `277` status `ready` deltaP `-6.9759` edge `-0.0493` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.9264` n `218` status `ready` deltaP `1.5737` edge `0.0288` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8266` n `277` status `ready` deltaP `-3.3647` edge `-0.0289` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.3869` n `218` status `ready` deltaP `7.0225` edge `0.0333` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.6115` n `218` status `ready` deltaP `-6.9078` edge `-0.2413` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.4512` n `218` status `ready` deltaP `-10.2271` edge `-0.0721` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
