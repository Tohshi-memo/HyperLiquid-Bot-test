# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T11:07:27.060846+00:00`
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

- `market_context_high->unknown_4h` score `47.0866` n `46` status `ready` deltaP `7.3171` edge `3.8751` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `32.165` n `46` status `ready` deltaP `18.048` edge `2.5757` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `17.1471` n `46` status `ready` deltaP `17.0139` edge `1.3155` maxDD `0.0`
- `market_context_high->equity_24h` score `16.5709` n `46` status `ready` deltaP `13.3605` edge `1.3019` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.5824` n `46` status `ready` deltaP `20.1314` edge `0.3397` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.4478` n `101` status `ready` deltaP `-7.3072` edge `1.1052` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.0991` n `101` status `ready` deltaP `37.6065` edge `0.2772` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.4501` n `101` status `ready` deltaP `12.2117` edge `0.2437` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2378` n `101` status `ready` deltaP `13.8362` edge `0.1408` maxDD `-2.058`
- `market_context_high->index_4h` score `2.1315` n `46` status `ready` deltaP `24.6884` edge `0.0264` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `2.0138` n `101` status `ready` deltaP `15.8702` edge `0.1878` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.5592` n `101` status `ready` deltaP `15.4829` edge `0.079` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.4211` n `46` status `ready` deltaP `9.3585` edge `0.0867` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.9648` n `46` status `ready` deltaP `7.6608` edge `0.0536` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.9639` n `101` status `ready` deltaP `16.2626` edge `0.0355` maxDD `-0.421`
- `market_context_high->crypto_alt_4h` score `0.8945` n `46` status `ready` deltaP `7.9069` edge `0.0813` maxDD `-2.7574`
- `market_context_high->index_1h` score `0.6986` n `46` status `ready` deltaP `10.8045` edge `0.0115` maxDD `-0.0249`
- `market_context_high->metal_24h` score `0.6679` n `46` status `ready` deltaP `19.837` edge `-0.0532` maxDD `-0.2042`
- `news_risk_high->crypto_alt_24h` score `0.6661` n `101` status `ready` deltaP `-6.7485` edge `0.5886` maxDD `-32.7147`
- `news_risk_high->metal_1h` score `0.5825` n `101` status `ready` deltaP `14.2986` edge `0.0134` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
