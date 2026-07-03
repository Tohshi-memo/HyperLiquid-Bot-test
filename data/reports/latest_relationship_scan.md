# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T16:22:29.781155+00:00`
- Price records: `672`
- Market context records: `5574`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11396`

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

- `market_context_high->equity_24h` score `4.3471` n `174` status `ready` deltaP `15.0084` edge `0.7701` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.2515` n `190` status `ready` deltaP `11.1361` edge `0.2593` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `0.9212` n `174` status `ready` deltaP `13.7991` edge `0.4388` maxDD `-29.6555`
- `market_context_high->fx_24h` score `0.801` n `174` status `ready` deltaP `16.9241` edge `0.0513` maxDD `-1.457`
- `market_context_high->equity_4h` score `0.6985` n `190` status `ready` deltaP `6.1457` edge `0.1811` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.644` n `190` status `ready` deltaP `6.5774` edge `0.1739` maxDD `-9.46`
- `market_context_high->index_1h` score `-0.2281` n `202` status `ready` deltaP `3.3497` edge `0.008` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-0.2604` n `190` status `ready` deltaP `6.2981` edge `0.0097` maxDD `-0.8712`
- `market_context_high->equity_1h` score `-0.2894` n `202` status `ready` deltaP `5.5019` edge `0.0399` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.4356` n `202` status `ready` deltaP `1.4273` edge `0.001` maxDD `-0.4122`
- `market_context_high->metal_1h` score `-0.5197` n `202` status `ready` deltaP `-0.0459` edge `0.0012` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6338` n `202` status `ready` deltaP `0.621` edge `0.0392` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7483` n `202` status `ready` deltaP `2.533` edge `0.0453` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.2665` n `202` status `ready` deltaP `-3.074` edge `-0.0085` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5274` n `190` status `ready` deltaP `2.4358` edge `0.0174` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.9764` n `174` status `ready` deltaP `13.5596` edge `0.0549` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0648` n `190` status `ready` deltaP `-13.9746` edge `-0.0614` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.4952` n `190` status `ready` deltaP `-7.837` edge `-0.0548` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.8446` n `174` status `ready` deltaP `-7.4593` edge `-0.2199` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-9.0822` n `174` status `ready` deltaP `3.7596` edge `0.0878` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
