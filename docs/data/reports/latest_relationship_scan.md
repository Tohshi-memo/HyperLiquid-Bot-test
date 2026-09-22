# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T02:22:30.604484+00:00`
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

- `market_context_high->unknown_4h` score `48.7306` n `46` status `ready` deltaP `7.3171` edge `4.0121` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `37.2891` n `46` status `ready` deltaP `24.1244` edge `2.9622` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `21.5937` n `46` status `ready` deltaP `22.9167` edge `1.6467` maxDD `0.0`
- `market_context_high->equity_24h` score `18.1156` n `46` status `ready` deltaP `17.3536` edge `1.404` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `9.572` n `101` status `ready` deltaP `-1.2308` edge `1.4917` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.8704` n `46` status `ready` deltaP `21.3466` edge `0.3556` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `5.1127` n `101` status `ready` deltaP `-0.8457` edge `0.9198` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `2.8422` n `101` status `ready` deltaP `13.8885` edge `0.2652` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.6435` n `101` status `ready` deltaP `32.3982` edge `0.2535` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.311` n `101` status `ready` deltaP `13.9859` edge `0.1459` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1476` n `101` status `ready` deltaP `16.3276` edge `0.1959` maxDD `-8.0625`
- `market_context_high->index_4h` score `2.0149` n `46` status `ready` deltaP `23.6214` edge `0.0238` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.6791` n `101` status `ready` deltaP `16.0817` edge `0.085` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `1.2867` n `46` status `ready` deltaP `9.5837` edge `0.1028` maxDD `-2.7574`
- `market_context_high->equity_4h` score `1.2082` n `46` status `ready` deltaP `8.9011` edge `0.072` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.9576` n `46` status `ready` deltaP `7.6608` edge `0.053` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.6418` n `101` status `ready` deltaP `13.0614` edge `0.03` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6256` n `46` status `ready` deltaP `9.9063` edge `0.0114` maxDD `-0.0249`
- `market_context_high->crypto_major_1h` score `0.5913` n `46` status `ready` deltaP `1.5101` edge `0.0915` maxDD `-2.1836`
- `news_risk_high->metal_1h` score `0.5442` n `101` status `ready` deltaP `13.8495` edge `0.0132` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
