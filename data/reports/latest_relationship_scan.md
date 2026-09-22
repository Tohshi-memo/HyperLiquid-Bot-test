# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T04:07:32.568778+00:00`
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

- `market_context_high->unknown_4h` score `49.2286` n `46` status `ready` deltaP `7.3171` edge `4.0536` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `36.0579` n `46` status `ready` deltaP `22.9091` edge `2.8677` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `20.4729` n `46` status `ready` deltaP `21.7014` edge `1.5614` maxDD `0.0`
- `market_context_high->equity_24h` score `17.5287` n `46` status `ready` deltaP `16.1383` edge `1.3632` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `8.3407` n `101` status `ready` deltaP `-2.4461` edge `1.3972` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6928` n `46` status `ready` deltaP `20.1314` edge `0.3489` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `3.9919` n `101` status `ready` deltaP `-2.061` edge `0.8345` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.7402` n `101` status `ready` deltaP `33.6135` edge `0.2578` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.6975` n `101` status `ready` deltaP `13.2788` edge `0.2572` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2798` n `101` status `ready` deltaP `13.8362` edge `0.1443` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.162` n `101` status `ready` deltaP `16.3276` edge `0.1971` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9725` n `46` status `ready` deltaP `23.3165` edge `0.0223` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.6336` n `101` status `ready` deltaP `15.7823` edge `0.0832` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `1.1419` n `46` status `ready` deltaP `8.974` edge `0.0948` maxDD `-2.7574`
- `market_context_high->equity_4h` score `1.056` n `46` status `ready` deltaP `8.1389` edge `0.0644` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.8569` n `46` status `ready` deltaP `6.9123` edge `0.0496` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.7547` n `101` status `ready` deltaP `14.1285` edge `0.0323` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6064` n `46` status `ready` deltaP `9.7566` edge `0.0108` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5574` n `101` status `ready` deltaP `13.9992` edge `0.0133` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.5457` n `46` status `ready` deltaP `1.2107` edge `0.0897` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
