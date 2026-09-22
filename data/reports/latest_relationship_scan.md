# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T12:22:34.200629+00:00`
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

- `market_context_high->unknown_4h` score `46.9738` n `46` status `ready` deltaP `7.3171` edge `3.8657` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `31.7307` n `46` status `ready` deltaP `17.18` edge `2.5453` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `16.8372` n `46` status `ready` deltaP `16.3194` edge `1.2943` maxDD `0.0`
- `market_context_high->equity_24h` score `16.4447` n `46` status `ready` deltaP `13.0133` edge `1.2937` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.5656` n `46` status `ready` deltaP `20.1314` edge `0.3383` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.0136` n `101` status `ready` deltaP `-8.1752` edge `1.0748` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.1895` n `101` status `ready` deltaP `38.4746` edge `0.283` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.4105` n `101` status `ready` deltaP `12.2117` edge `0.2404` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2666` n `101` status `ready` deltaP `13.8362` edge `0.1432` maxDD `-2.058`
- `market_context_high->index_4h` score `2.0489` n `46` status `ready` deltaP `23.9263` edge `0.0246` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.8101` n `101` status `ready` deltaP `15.108` edge `0.1759` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.5796` n `101` status `ready` deltaP `15.4829` edge `0.0807` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.2426` n `46` status `ready` deltaP `8.5963` edge `0.0769` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.0404` n `101` status `ready` deltaP `17.0248` edge `0.0368` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.9996` n `46` status `ready` deltaP `7.9602` edge `0.0545` maxDD `-0.2751`
- `market_context_high->crypto_alt_4h` score `0.8549` n `46` status `ready` deltaP `7.9069` edge `0.078` maxDD `-2.7574`
- `market_context_high->metal_24h` score `0.8118` n `46` status `ready` deltaP `20.7051` edge `-0.047` maxDD `-0.2042`
- `market_context_high->index_1h` score `0.7489` n `46` status `ready` deltaP `11.4033` edge `0.0117` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6113` n `101` status `ready` deltaP `14.598` edge `0.0138` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.4918` n `46` status `ready` deltaP `0.9113` edge `0.0872` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
