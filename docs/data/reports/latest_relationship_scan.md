# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T21:07:25.190241+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10602`

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

- `risk_on_high->unknown_4h` score `19.7867` n `133` status `ready` deltaP `8.3887` edge `1.6548` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.7867` n `133` status `ready` deltaP `8.3887` edge `1.6548` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `10.9785` n `133` status `ready` deltaP `-1.8021` edge `0.9846` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `10.9785` n `133` status `ready` deltaP `-1.8021` edge `0.9846` maxDD `-1.95`
- `market_context_high->unknown_4h` score `9.7803` n `215` status `ready` deltaP `9.5498` edge `0.8209` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.2` n `217` status `ready` deltaP `-0.8562` edge `0.7521` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `4.143` n `46` status `ready` deltaP `20.1917` edge `0.2376` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.2771` n `46` status `ready` deltaP `9.882` edge `0.1722` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `2.0114` n `46` status `ready` deltaP `11.8659` edge `0.1057` maxDD `-0.042`
- `news_risk_high->metal_4h` score `1.6789` n `46` status `ready` deltaP `17.6232` edge `0.0487` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6339` n `46` status `ready` deltaP `15.8292` edge `0.0697` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.4657` n `46` status `ready` deltaP `10.114` edge `0.0748` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.1193` n `46` status `ready` deltaP `14.3973` edge `0.0107` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.7268` n `46` status `ready` deltaP `9.3726` edge `0.0174` maxDD `-0.2118`
- `news_risk_high->fx_4h` score `0.2933` n `46` status `ready` deltaP `10.4056` edge `0.0003` maxDD `-0.9514`
- `news_risk_high->commodity_1h` score `0.2376` n `46` status `ready` deltaP `9.0797` edge `0.0039` maxDD `-0.9036`
- `news_risk_high->crypto_alt_1h` score `0.1699` n `46` status `ready` deltaP `3.9053` edge `0.0184` maxDD `-1.0885`
- `risk_on_high->metal_1h` score `0.0968` n `133` status `ready` deltaP `12.4128` edge `0.0009` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0968` n `133` status `ready` deltaP `12.4128` edge `0.0009` maxDD `-1.699`
- `news_risk_high->crypto_major_1h` score `0.0671` n `46` status `ready` deltaP `-0.371` edge `0.0403` maxDD `-1.0047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
