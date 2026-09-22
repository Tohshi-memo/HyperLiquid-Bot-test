# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T15:22:35.607884+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9930`

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

- `market_context_high->unknown_4h` score `46.5594` n `46` status `ready` deltaP `7.0122` edge `3.8332` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `30.5993` n `46` status `ready` deltaP `15.0966` edge `2.4649` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2236` n `46` status `ready` deltaP `12.3189` edge `1.2799` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.8127` n `46` status `ready` deltaP `14.5833` edge `1.2205` maxDD `0.0`
- `market_context_high->index_24h` score `5.5428` n `46` status `ready` deltaP `20.1314` edge `0.3364` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `3.1938` n `101` status `ready` deltaP `38.301` edge `0.2847` maxDD `-3.4467`
- `news_risk_high->crypto_major_24h` score `2.8821` n `101` status `ready` deltaP `-10.2586` edge `0.9944` maxDD `-46.1999`
- `news_risk_high->crypto_alt_1h` score `2.1011` n `101` status `ready` deltaP `13.0877` edge `0.1344` maxDD `-2.058`
- `news_risk_high->crypto_alt_4h` score `2.0899` n `101` status `ready` deltaP `11.1446` edge `0.2208` maxDD `-7.675`
- `market_context_high->index_4h` score `1.9032` n `46` status `ready` deltaP `22.5543` edge `0.0216` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.4099` n `101` status `ready` deltaP `13.7361` edge `0.1517` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.3746` n `101` status `ready` deltaP `14.435` edge `0.0706` maxDD `-2.8494`
- `news_risk_high->fx_4h` score `1.0928` n `101` status `ready` deltaP `17.6346` edge `0.0371` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.0563` n `46` status `ready` deltaP `22.4412` edge `-0.0382` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.8454` n `46` status `ready` deltaP `6.767` edge `0.056` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.84` n `46` status `ready` deltaP `7.3614` edge `0.0452` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6579` n `46` status `ready` deltaP `10.5051` edge `0.0101` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6005` n `101` status `ready` deltaP `14.598` edge `0.0129` maxDD `-0.8144`
- `market_context_high->crypto_alt_4h` score `0.5344` n `46` status `ready` deltaP `6.8398` edge `0.0584` maxDD `-2.7574`
- `news_risk_high->metal_24h` score `0.4874` n `101` status `ready` deltaP `18.6314` edge `0.0227` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
