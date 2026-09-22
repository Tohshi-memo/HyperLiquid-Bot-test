# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T10:22:35.559524+00:00`
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

- `market_context_high->unknown_4h` score `47.1922` n `46` status `ready` deltaP `7.3171` edge `3.8839` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `32.4743` n `46` status `ready` deltaP `18.5689` edge `2.598` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `17.3585` n `46` status `ready` deltaP `17.3611` edge `1.3308` maxDD `0.0`
- `market_context_high->equity_24h` score `16.693` n `46` status `ready` deltaP `13.8814` edge `1.3086` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.5932` n `46` status `ready` deltaP `20.1314` edge `0.3406` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.7571` n `101` status `ready` deltaP `-6.7863` edge `1.1275` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.0409` n `101` status `ready` deltaP `37.0857` edge `0.2732` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.4825` n `101` status `ready` deltaP `12.2117` edge `0.2464` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2246` n `101` status `ready` deltaP `13.8362` edge `0.1397` maxDD `-2.058`
- `market_context_high->index_4h` score `2.1777` n `46` status `ready` deltaP `25.1458` edge `0.0272` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `2.0942` n `101` status `ready` deltaP `15.8702` edge `0.1945` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.5568` n `101` status `ready` deltaP `15.4829` edge `0.0788` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.5297` n `46` status `ready` deltaP `9.8158` edge `0.0927` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.972` n `46` status `ready` deltaP `7.6608` edge `0.0542` maxDD `-0.2751`
- `market_context_high->crypto_alt_4h` score `0.9269` n `46` status `ready` deltaP `7.9069` edge `0.084` maxDD `-2.7574`
- `news_risk_high->fx_4h` score `0.9189` n `101` status `ready` deltaP `15.8053` edge `0.0348` maxDD `-0.421`
- `news_risk_high->crypto_alt_24h` score `0.8775` n `101` status `ready` deltaP `-6.4013` edge `0.6039` maxDD `-32.7147`
- `market_context_high->index_1h` score `0.6854` n `46` status `ready` deltaP `10.6548` edge `0.0114` maxDD `-0.0249`
- `market_context_high->metal_24h` score `0.5915` n `46` status `ready` deltaP `19.3162` edge `-0.0561` maxDD `-0.2042`
- `news_risk_high->metal_1h` score `0.5706` n `101` status `ready` deltaP `14.1489` edge `0.0134` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
