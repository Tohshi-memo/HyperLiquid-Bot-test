# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T10:52:31.895914+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `47.1286` n `46` status `ready` deltaP `7.3171` edge `3.8786` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `32.2593` n `46` status `ready` deltaP `18.2216` edge `2.5824` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `17.1987` n `46` status `ready` deltaP `17.0139` edge `1.3198` maxDD `0.0`
- `market_context_high->equity_24h` score `16.6124` n `46` status `ready` deltaP `13.5341` edge `1.3042` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.586` n `46` status `ready` deltaP `20.1314` edge `0.34` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.5421` n `101` status `ready` deltaP `-7.1336` edge `1.1119` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.0792` n `101` status `ready` deltaP `37.4329` edge `0.2758` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.4549` n `101` status `ready` deltaP `12.2117` edge `0.2441` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.233` n `101` status `ready` deltaP `13.8362` edge `0.1404` maxDD `-2.058`
- `market_context_high->index_4h` score `2.1473` n `46` status `ready` deltaP `24.8409` edge `0.0267` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `2.0378` n `101` status `ready` deltaP `15.8702` edge `0.1898` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.558` n `101` status `ready` deltaP `15.4829` edge `0.0789` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.4597` n `46` status `ready` deltaP `9.5109` edge `0.0889` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.9648` n `46` status `ready` deltaP `7.6608` edge `0.0536` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.9493` n `101` status `ready` deltaP `16.1102` edge `0.0353` maxDD `-0.421`
- `market_context_high->crypto_alt_4h` score `0.8993` n `46` status `ready` deltaP `7.9069` edge `0.0817` maxDD `-2.7574`
- `news_risk_high->crypto_alt_24h` score `0.7177` n `101` status `ready` deltaP `-6.7485` edge `0.5929` maxDD `-32.7147`
- `market_context_high->index_1h` score `0.6854` n `46` status `ready` deltaP `10.6548` edge `0.0114` maxDD `-0.0249`
- `market_context_high->metal_24h` score `0.642` n `46` status `ready` deltaP `19.6634` edge `-0.0542` maxDD `-0.2042`
- `news_risk_high->metal_1h` score `0.5694` n `101` status `ready` deltaP `14.1489` edge `0.0133` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
