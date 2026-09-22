# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T15:37:30.739132+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9834`

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

- `market_context_high->unknown_4h` score `46.4778` n `46` status `ready` deltaP `7.0122` edge `3.8264` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `30.517` n `46` status `ready` deltaP `14.923` edge `2.4592` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2332` n `46` status `ready` deltaP `12.3189` edge `1.2807` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.7112` n `46` status `ready` deltaP `14.4097` edge `1.2132` maxDD `0.0`
- `market_context_high->index_24h` score `5.5452` n `46` status `ready` deltaP `20.1314` edge `0.3366` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `3.1762` n `101` status `ready` deltaP `38.1274` edge `0.2836` maxDD `-3.4467`
- `news_risk_high->crypto_major_24h` score `2.7998` n `101` status `ready` deltaP `-10.4322` edge `0.9887` maxDD `-46.1999`
- `news_risk_high->crypto_alt_1h` score `2.0687` n `101` status `ready` deltaP `12.938` edge `0.1327` maxDD `-2.058`
- `news_risk_high->crypto_alt_4h` score `2.0369` n `101` status `ready` deltaP `10.9922` edge `0.2174` maxDD `-7.675`
- `market_context_high->index_4h` score `1.8886` n `46` status `ready` deltaP `22.4019` edge `0.0214` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.3593` n `101` status `ready` deltaP `13.5837` edge `0.1485` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.347` n `101` status `ready` deltaP `14.2853` edge `0.0693` maxDD `-2.8494`
- `news_risk_high->fx_4h` score `1.0928` n `101` status `ready` deltaP `17.6346` edge `0.0371` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.0822` n `46` status `ready` deltaP `22.6148` edge `-0.0372` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.8448` n `46` status `ready` deltaP `7.3614` edge `0.0456` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.8152` n `46` status `ready` deltaP `6.6146` edge `0.0545` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6591` n `46` status `ready` deltaP `10.5051` edge `0.0102` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6149` n `101` status `ready` deltaP `14.7477` edge `0.0131` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.5042` n `101` status `ready` deltaP `18.805` edge `0.0237` maxDD `-2.4203`
- `market_context_high->crypto_alt_4h` score `0.4814` n `46` status `ready` deltaP `6.6874` edge `0.055` maxDD `-2.7574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
