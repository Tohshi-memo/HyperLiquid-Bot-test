# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T03:52:29.858111+00:00`
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

- `market_context_high->unknown_4h` score `49.2046` n `46` status `ready` deltaP `7.3171` edge `4.0516` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `36.2494` n `46` status `ready` deltaP `23.0828` edge `2.8825` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `20.6248` n `46` status `ready` deltaP `21.875` edge `1.5729` maxDD `0.0`
- `market_context_high->equity_24h` score `17.6014` n `46` status `ready` deltaP `16.3119` edge `1.3681` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `8.5322` n `101` status `ready` deltaP `-2.2724` edge `1.412` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.7163` n `46` status `ready` deltaP `20.305` edge `0.3497` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `4.1438` n `101` status `ready` deltaP `-1.8874` edge `0.846` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `2.7336` n `101` status `ready` deltaP `13.4312` edge `0.2592` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.7257` n `101` status `ready` deltaP `33.4399` edge `0.2571` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.305` n `101` status `ready` deltaP `13.9859` edge `0.1454` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1824` n `101` status `ready` deltaP `16.3276` edge `0.1988` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9749` n `46` status `ready` deltaP `23.3165` edge `0.0225` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.6696` n `101` status `ready` deltaP `15.932` edge `0.0852` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `1.1781` n `46` status `ready` deltaP `9.1264` edge `0.0968` maxDD `-2.7574`
- `market_context_high->equity_4h` score `1.0632` n `46` status `ready` deltaP `8.1389` edge `0.065` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.8605` n `46` status `ready` deltaP `6.9123` edge `0.0499` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.7389` n `101` status `ready` deltaP `13.9761` edge `0.032` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6076` n `46` status `ready` deltaP `9.7566` edge `0.0109` maxDD `-0.0249`
- `market_context_high->crypto_major_1h` score `0.5817` n `46` status `ready` deltaP `1.3604` edge `0.0917` maxDD `-2.1836`
- `news_risk_high->metal_1h` score `0.5574` n `101` status `ready` deltaP `13.9992` edge `0.0133` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
