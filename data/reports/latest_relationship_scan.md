# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T15:07:56.657075+00:00`
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

- `market_context_high->unknown_4h` score `46.6134` n `46` status `ready` deltaP `7.0122` edge `3.8377` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `30.678` n `46` status `ready` deltaP `15.2703` edge `2.4703` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2128` n `46` status `ready` deltaP `12.3189` edge `1.279` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.9058` n `46` status `ready` deltaP `14.7569` edge `1.2271` maxDD `0.0`
- `market_context_high->index_24h` score `5.5392` n `46` status `ready` deltaP `20.1314` edge `0.3361` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `3.2121` n `101` status `ready` deltaP `38.4746` edge `0.2859` maxDD `-3.4467`
- `news_risk_high->crypto_major_24h` score `2.9608` n `101` status `ready` deltaP `-10.0849` edge `0.9998` maxDD `-46.1999`
- `news_risk_high->crypto_alt_4h` score `2.1321` n `101` status `ready` deltaP `11.2971` edge `0.2233` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.1023` n `101` status `ready` deltaP `13.0877` edge `0.1345` maxDD `-2.058`
- `market_context_high->index_4h` score `1.9044` n `46` status `ready` deltaP `22.5543` edge `0.0217` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.4533` n `101` status `ready` deltaP `13.8885` edge `0.1543` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.3746` n `101` status `ready` deltaP `14.435` edge `0.0706` maxDD `-2.8494`
- `news_risk_high->fx_4h` score `1.0928` n `101` status `ready` deltaP `17.6346` edge `0.0371` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.0455` n `46` status `ready` deltaP `22.4412` edge `-0.0391` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.872` n `46` status `ready` deltaP `6.9194` edge `0.0572` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.8209` n `46` status `ready` deltaP `7.2117` edge `0.0446` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6447` n `46` status `ready` deltaP `10.3554` edge `0.01` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5861` n `101` status `ready` deltaP `14.4483` edge `0.0127` maxDD `-0.8144`
- `market_context_high->crypto_alt_4h` score `0.5766` n `46` status `ready` deltaP `6.9923` edge `0.0609` maxDD `-2.7574`
- `news_risk_high->metal_24h` score `0.4804` n `101` status `ready` deltaP `18.6314` edge `0.0218` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
