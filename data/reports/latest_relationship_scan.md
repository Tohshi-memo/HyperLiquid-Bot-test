# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T20:52:28.989020+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10656`

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

- `news_risk_high->crypto_major_24h` score `24.2276` n `98` status `ready` deltaP `12.2697` edge `2.623` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.4106` n `98` status `ready` deltaP `15.2671` edge `2.0872` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `10.2136` n `44` status `ready` deltaP `-0.4158` edge `0.8689` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `4.721` n `101` status `ready` deltaP `21.0532` edge `0.374` maxDD `-7.675`
- `market_context_high->commodity_4h` score `3.7784` n `44` status `ready` deltaP `36.0587` edge `0.0878` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `3.7681` n `101` status `ready` deltaP `20.4434` edge `0.3035` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.8877` n `101` status `ready` deltaP `16.6805` edge `0.176` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2055` n `101` status `ready` deltaP `18.7763` edge `0.1109` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.2029` n `44` status `ready` deltaP `18.0017` edge `0.0069` maxDD `-0.1333`
- `news_risk_high->commodity_24h` score `1.0261` n `98` status `ready` deltaP `22.775` edge `0.1103` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.8757` n `55` status `ready` deltaP `12.9314` edge `0.0047` maxDD `-0.1012`
- `market_context_high->commodity_1h` score `0.6874` n `55` status `ready` deltaP `11.9897` edge `0.0357` maxDD `-0.1998`
- `news_risk_high->metal_1h` score `0.6425` n `101` status `ready` deltaP `14.7477` edge `0.0154` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.6252` n `101` status `ready` deltaP `17.2512` edge `0.0425` maxDD `-2.0994`
- `news_risk_high->equity_24h` score `0.4774` n `98` status `ready` deltaP `16.3974` edge `0.0714` maxDD `-4.941`
- `news_risk_high->equity_1h` score `0.2328` n `101` status `ready` deltaP `5.364` edge `0.0242` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `0.2017` n `101` status `ready` deltaP `8.6407` edge `0.0228` maxDD `-0.421`
- `news_risk_high->metal_24h` score `0.1098` n `98` status `ready` deltaP `14.9837` edge `-0.0014` maxDD `-2.4203`
- `market_context_high->metal_1h` score `-0.0299` n `55` status `ready` deltaP `3.9467` edge `0.0047` maxDD `-0.4538`
- `news_risk_high->fx_1h` score `-0.2915` n `101` status `ready` deltaP `2.0943` edge `0.0061` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
