# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T02:22:29.077663+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.5786` n `90` status `ready` deltaP `-4.4749` edge `3.2986` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.7783` n `62` status `ready` deltaP `37.6672` edge `0.6674` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.8989` n `62` status `ready` deltaP `22.1725` edge `0.5615` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.0295` n `62` status `ready` deltaP `15.0017` edge `0.4124` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.7547` n `62` status `ready` deltaP `34.4291` edge `0.1667` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.247` n `90` status `ready` deltaP `10.0461` edge `0.7749` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.9299` n `62` status `ready` deltaP `32.1548` edge `0.056` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.424` n `62` status `ready` deltaP `9.8754` edge `0.1717` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.2735` n `90` status `ready` deltaP `15.7317` edge `0.181` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.1032` n `62` status `ready` deltaP `17.3191` edge `0.1196` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9277` n `62` status `ready` deltaP `24.2757` edge `0.0138` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.5249` n `90` status `ready` deltaP `12.5644` edge `0.0862` maxDD `-1.0977`
- `news_risk_high->metal_4h` score `1.4645` n `62` status `ready` deltaP `21.0956` edge `0.0887` maxDD `-0.993`
- `news_risk_high->unknown_4h` score `1.3582` n `62` status `ready` deltaP `-7.4499` edge `0.2874` maxDD `-5.6309`
- `market_context_high->metal_24h` score `1.1992` n `90` status `ready` deltaP `20.9458` edge `0.1626` maxDD `-3.5466`
- `market_context_high->fx_4h` score `1.0767` n `90` status `ready` deltaP `21.8259` edge `0.0189` maxDD `-0.3077`
- `news_risk_high->crypto_alt_1h` score `1.0459` n `62` status `ready` deltaP `2.5594` edge `0.122` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.725` n `90` status `ready` deltaP `12.0958` edge `0.004` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1105` n `90` status `ready` deltaP `9.8037` edge `0.0377` maxDD `-3.7778`
- `market_context_high->crypto_alt_24h` score `0.0991` n `90` status `ready` deltaP `7.1127` edge `0.5591` maxDD `-34.5048`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
