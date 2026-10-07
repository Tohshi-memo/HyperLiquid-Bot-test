# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T05:22:27.759166+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `1164.0492` n `113` status `ready` deltaP `10.7731` edge `96.9703` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `30.5305` n `113` status `ready` deltaP `-0.8714` edge `2.6039` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.8976` n `62` status `ready` deltaP `34.9233` edge `0.6123` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.4085` n `62` status `ready` deltaP `21.5628` edge `0.5247` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.6381` n `113` status `ready` deltaP `17.3241` edge `0.2841` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.1796` n `62` status `ready` deltaP `22.5694` edge `0.1145` maxDD `0.0`
- `news_risk_high->index_4h` score `2.758` n `62` status `ready` deltaP `30.9353` edge `0.0498` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.1135` n `62` status `ready` deltaP `7.7796` edge `0.1598` maxDD `-1.5096`
- `news_risk_high->equity_24h` score `1.959` n `62` status `ready` deltaP `3.2706` edge `0.1514` maxDD `-0.1298`
- `news_risk_high->index_1h` score `1.9385` n `62` status `ready` deltaP `24.5751` edge `0.0127` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.77` n `62` status `ready` deltaP `16.7093` edge `0.0959` maxDD `-2.7837`
- `market_context_high->crypto_alt_4h` score `1.5935` n `113` status `ready` deltaP `1.8225` edge `0.293` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `1.499` n `113` status `ready` deltaP `7.3946` edge `0.373` maxDD `-16.7906`
- `news_risk_high->metal_4h` score `1.2995` n `62` status `ready` deltaP `18.6565` edge `0.0838` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `0.9955` n `62` status `ready` deltaP `2.7091` edge `0.1168` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.8566` n `113` status `ready` deltaP `19.268` edge `0.0186` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.829` n `62` status `ready` deltaP `28.4107` edge `0.0735` maxDD `-8.196`
- `market_context_high->fx_1h` score `0.7589` n `113` status `ready` deltaP `12.9948` edge `0.005` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.4318` n `113` status `ready` deltaP `11.3075` edge `0.0306` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `0.2849` n `113` status `ready` deltaP `9.6352` edge `0.0484` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
