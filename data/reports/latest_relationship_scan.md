# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T01:52:30.444707+00:00`
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

- `market_context_high->unknown_4h` score `38.6016` n `90` status `ready` deltaP `-4.3224` edge `3.2995` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.7867` n `62` status `ready` deltaP `37.6672` edge `0.6681` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.8941` n `62` status `ready` deltaP `22.1725` edge `0.5611` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.9394` n `62` status `ready` deltaP `14.6557` edge `0.4072` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.715` n `62` status `ready` deltaP `34.083` edge `0.1657` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.2213` n `90` status `ready` deltaP `10.0461` edge `0.7716` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8984` n `62` status `ready` deltaP `31.8499` edge `0.0554` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4168` n `62` status `ready` deltaP `9.8754` edge `0.1711` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.2819` n `90` status `ready` deltaP `15.7317` edge `0.1817` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0706` n `62` status `ready` deltaP `17.1666` edge `0.1179` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9409` n `62` status `ready` deltaP `24.4254` edge `0.0139` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4708` n `62` status `ready` deltaP `21.0956` edge `0.0895` maxDD `-0.993`
- `market_context_high->equity_24h` score `1.4348` n `90` status `ready` deltaP `12.2184` edge `0.081` maxDD `-1.0977`
- `news_risk_high->unknown_4h` score `1.3812` n `62` status `ready` deltaP `-7.2974` edge `0.2883` maxDD `-5.6309`
- `market_context_high->metal_24h` score `1.1757` n `90` status `ready` deltaP `20.5997` edge `0.1619` maxDD `-3.5466`
- `market_context_high->fx_4h` score `1.0487` n `90` status `ready` deltaP `21.521` edge `0.0186` maxDD `-0.3077`
- `news_risk_high->crypto_alt_1h` score `1.004` n `62` status `ready` deltaP `2.26` edge `0.1205` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7226` n `90` status `ready` deltaP `12.0958` edge `0.0038` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1058` n `90` status `ready` deltaP `9.8037` edge `0.0371` maxDD `-3.7778`
- `market_context_high->crypto_alt_24h` score `0.1022` n `90` status `ready` deltaP `7.1127` edge `0.5595` maxDD `-34.5048`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
