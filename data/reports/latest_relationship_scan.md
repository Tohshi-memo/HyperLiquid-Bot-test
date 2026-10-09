# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T02:22:29.608529+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8896`

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

- `market_context_high->unknown_4h` score `39.8212` n `91` status `ready` deltaP `-3.5965` edge `3.3963` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.278` n `46` status `ready` deltaP `43.4451` edge `0.9002` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.7537` n `46` status `ready` deltaP `44.2802` edge `0.8577` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `11.1029` n `46` status `ready` deltaP `28.7393` edge `0.7436` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.5784` n `90` status `ready` deltaP `21.9122` edge `1.3793` maxDD `-16.7906`
- `market_context_high->equity_24h` score `8.6666` n `90` status `ready` deltaP `28.5461` edge `0.5748` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.8759` n `46` status `ready` deltaP `49.3934` edge `0.2437` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.9101` n `46` status `ready` deltaP `31.7006` edge `0.3017` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5514` n `46` status `ready` deltaP `45.2346` edge `0.0822` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.3373` n `90` status `ready` deltaP `13.6145` edge `0.9309` maxDD `-34.5048`
- `news_risk_high->crypto_major_1h` score `3.0835` n `46` status `ready` deltaP `11.7743` edge `0.214` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.2996` n `46` status `ready` deltaP `28.6384` edge `0.0147` maxDD `-0.1194`
- `news_risk_high->crypto_alt_1h` score `2.1961` n `46` status `ready` deltaP `3.378` edge `0.1922` maxDD `-1.2034`
- `news_risk_high->commodity_24h` score `2.1792` n `46` status `ready` deltaP `28.9278` edge `-0.0028` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.7193` n `91` status `ready` deltaP `17.8588` edge `0.2344` maxDD `-6.9761`
- `news_risk_high->metal_4h` score `1.3485` n `46` status `ready` deltaP `21.3547` edge `0.0721` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.1793` n `90` status `ready` deltaP `20.699` edge `0.1617` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.4492` n `91` status `ready` deltaP `15.0764` edge `0.0116` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4284` n `91` status `ready` deltaP `8.6432` edge `0.0023` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2694` n `91` status `ready` deltaP `10.2932` edge `0.0548` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
