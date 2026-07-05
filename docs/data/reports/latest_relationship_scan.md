# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T19:39:57.561150+00:00`
- Price records: `672`
- Market context records: `5805`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9058`

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

- `market_context_high->equity_24h` score `0.3461` n `248` status `ready` deltaP `15.3954` edge `0.4341` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.1105` n `295` status `ready` deltaP `5.6335` edge `0.1171` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2215` n `295` status `ready` deltaP `2.8418` edge `0.0012` maxDD `-0.5499`
- `market_context_high->metal_1h` score `-0.6377` n `295` status `ready` deltaP `2.2912` edge `-0.0009` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.644` n `295` status `ready` deltaP `0.1162` edge `0.0035` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6533` n `295` status `ready` deltaP `2.9331` edge `0.0267` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7408` n `295` status `ready` deltaP `-1.9522` edge `-0.0049` maxDD `-3.4978`
- `market_context_high->crypto_major_1h` score `-0.9337` n `295` status `ready` deltaP `2.9692` edge `0.0345` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1343` n `295` status `ready` deltaP `1.2037` edge `0.0309` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2495` n `295` status `ready` deltaP `-0.1152` edge `0.0093` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.3006` n `248` status `ready` deltaP `11.5087` edge `0.0341` maxDD `-5.2054`
- `market_context_high->fx_4h` score `-1.4257` n `295` status `ready` deltaP `1.2046` edge `0.0041` maxDD `-2.2593`
- `market_context_high->commodity_4h` score `-2.0542` n `295` status `ready` deltaP `-2.6168` edge `-0.0214` maxDD `-10.628`
- `market_context_high->metal_4h` score `-2.3508` n `295` status `ready` deltaP `-4.6403` edge `-0.046` maxDD `-10.6231`
- `market_context_high->crypto_major_4h` score `-2.8009` n `295` status `ready` deltaP `7.9702` edge `0.1507` maxDD `-25.6458`
- `market_context_high->index_24h` score `-2.8042` n `248` status `ready` deltaP `3.7131` edge `0.0302` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.4345` n `295` status `ready` deltaP `5.7157` edge `0.0932` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-6.1098` n `248` status `ready` deltaP `-5.6843` edge `-0.2424` maxDD `-22.5746`
- `market_context_high->commodity_24h` score `-9.7935` n `248` status `ready` deltaP `-13.1496` edge `-0.0721` maxDD `-35.1754`
- `market_context_high->crypto_major_24h` score `-10.2905` n `248` status `ready` deltaP `-1.3049` edge `-0.224` maxDD `-33.6539`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
