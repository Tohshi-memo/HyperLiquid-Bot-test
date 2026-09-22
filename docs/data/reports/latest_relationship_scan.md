# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T05:37:28.925021+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10002`

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

- `market_context_high->unknown_4h` score `49.1602` n `46` status `ready` deltaP `7.3171` edge `4.0479` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `35.0757` n `46` status `ready` deltaP `21.8675` edge `2.7928` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `19.6732` n `46` status `ready` deltaP `20.6597` edge `1.5017` maxDD `0.0`
- `market_context_high->equity_24h` score `17.185` n `46` status `ready` deltaP `15.0966` edge `1.3415` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `7.3586` n `101` status `ready` deltaP `-3.4877` edge `1.3223` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6484` n `46` status `ready` deltaP `20.1314` edge `0.3452` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `3.1922` n `101` status `ready` deltaP `-3.1027` edge `0.7748` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.8178` n `101` status `ready` deltaP `34.6552` edge `0.2608` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.6891` n `101` status `ready` deltaP `13.2788` edge `0.2565` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.3217` n `101` status `ready` deltaP `14.1356` edge `0.1458` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1644` n `101` status `ready` deltaP `16.3276` edge `0.1973` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9749` n `46` status `ready` deltaP `23.3165` edge `0.0225` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.6492` n `101` status `ready` deltaP `15.7823` edge `0.0845` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `1.1335` n `46` status `ready` deltaP `8.974` edge `0.0941` maxDD `-2.7574`
- `market_context_high->equity_4h` score `1.0992` n `46` status `ready` deltaP `8.1389` edge `0.068` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.954` n `46` status `ready` deltaP `7.5111` edge `0.0537` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8447` n `101` status `ready` deltaP `15.0431` edge `0.0337` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6603` n `46` status `ready` deltaP `10.3554` edge `0.0113` maxDD `-0.0249`
- `market_context_high->crypto_major_1h` score `0.5613` n `46` status `ready` deltaP `1.2107` edge `0.091` maxDD `-2.1836`
- `news_risk_high->metal_1h` score `0.5454` n `101` status `ready` deltaP `13.8495` edge `0.0133` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
