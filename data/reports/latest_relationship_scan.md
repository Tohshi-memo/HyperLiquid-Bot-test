# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T21:20:58.677265+00:00`
- Price records: `672`
- Market context records: `5596`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11433`

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

- `market_context_high->equity_24h` score `3.6631` n `174` status `ready` deltaP `15.0084` edge `0.7131` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.3619` n `210` status `ready` deltaP `12.4564` edge `0.2597` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.1189` n `174` status `ready` deltaP `20.2227` edge `0.0558` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.6619` n `210` status `ready` deltaP `7.5217` edge `0.1691` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.5704` n `210` status `ready` deltaP `6.6449` edge `0.1671` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.3136` n `222` status `ready` deltaP `0.9036` edge `0.0011` maxDD `-0.453`
- `market_context_high->equity_1h` score `-0.3436` n `222` status `ready` deltaP `5.574` edge `0.0349` maxDD `-5.0555`
- `market_context_high->crypto_major_24h` score `-0.4689` n `174` status `ready` deltaP `11.5422` edge `0.338` maxDD `-29.6555`
- `market_context_high->crypto_major_1h` score `-0.5149` n `222` status `ready` deltaP `4.6556` edge `0.0506` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.5276` n `222` status `ready` deltaP `1.5132` edge `0.0421` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.5445` n `222` status `ready` deltaP `1.5092` edge `0.0064` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.5775` n `222` status `ready` deltaP `-1.052` edge `0.0005` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-1.2021` n `210` status `ready` deltaP `3.027` edge `0.0085` maxDD `-0.9751`
- `market_context_high->commodity_1h` score `-1.2392` n `222` status `ready` deltaP `-2.8524` edge `-0.0077` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5304` n `210` status `ready` deltaP `2.8934` edge `0.0141` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.2783` n `174` status `ready` deltaP `11.1291` edge `0.0324` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9265` n `210` status `ready` deltaP `-11.9613` edge `-0.0571` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1538` n `210` status `ready` deltaP `-5.1597` edge `-0.0442` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.0556` n `174` status `ready` deltaP `-8.501` edge `-0.24` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-10.5546` n `174` status `ready` deltaP `1.329` edge `-0.0187` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
