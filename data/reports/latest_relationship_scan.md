# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T06:22:34.434782+00:00`
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

- `market_context_high->unknown_4h` score `48.3382` n `46` status `ready` deltaP `7.3171` edge `3.9794` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `34.5889` n `46` status `ready` deltaP `21.3466` edge `2.7557` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `19.2535` n `46` status `ready` deltaP `20.1389` edge `1.4702` maxDD `0.0`
- `market_context_high->equity_24h` score `17.0305` n `46` status `ready` deltaP `14.5758` edge `1.3321` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `6.8717` n `101` status `ready` deltaP `-4.0086` edge `1.2852` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6292` n `46` status `ready` deltaP `20.1314` edge `0.3436` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `2.8581` n `101` status `ready` deltaP `35.176` edge `0.2625` maxDD `-3.4467`
- `news_risk_high->crypto_alt_24h` score `2.7725` n `101` status `ready` deltaP `-3.6235` edge `0.7433` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `2.6553` n `101` status `ready` deltaP `13.1263` edge `0.2547` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2702` n `101` status `ready` deltaP `13.8362` edge `0.1435` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1342` n `101` status `ready` deltaP `16.1751` edge `0.1958` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9785` n `46` status `ready` deltaP `23.3165` edge `0.0228` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5916` n `101` status `ready` deltaP `15.4829` edge `0.0817` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.151` n `46` status `ready` deltaP `8.2914` edge `0.0713` maxDD `-0.4529`
- `market_context_high->crypto_alt_4h` score `1.0997` n `46` status `ready` deltaP `8.8215` edge `0.0923` maxDD `-2.7574`
- `market_context_high->equity_1h` score `0.9552` n `46` status `ready` deltaP `7.5111` edge `0.0538` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8837` n `101` status `ready` deltaP `15.5004` edge `0.0339` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6591` n `46` status `ready` deltaP `10.3554` edge `0.0112` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5478` n `101` status `ready` deltaP `13.8495` edge `0.0135` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.5038` n `46` status `ready` deltaP `0.9113` edge `0.0882` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
