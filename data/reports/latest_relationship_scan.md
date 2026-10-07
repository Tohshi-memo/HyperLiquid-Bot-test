# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T09:37:28.088030+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_24h` score `366.2096` n `100` status `ready` deltaP `8.4722` edge `30.499` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `35.2648` n `100` status `ready` deltaP `-3.4024` edge `3.0153` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.025` n `62` status `ready` deltaP `35.0757` edge `0.6219` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.7553` n `62` status `ready` deltaP `22.4774` edge `0.5475` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.5309` n `62` status `ready` deltaP `25.5208` edge `0.1241` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.017` n `100` status `ready` deltaP `15.1402` edge `0.2469` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8566` n `62` status `ready` deltaP `32.0024` edge `0.0509` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.5995` n `62` status `ready` deltaP `6.222` edge `0.1851` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.1147` n `62` status `ready` deltaP `7.9293` edge `0.1589` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0079` n `62` status `ready` deltaP `25.3236` edge `0.0135` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.9299` n `62` status `ready` deltaP `17.9288` edge `0.1011` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.4162` n `62` status `ready` deltaP `20.1809` edge `0.0886` maxDD `-0.993`
- `market_context_high->fx_1h` score `1.0295` n `100` status `ready` deltaP `15.6467` edge `0.0057` maxDD `-0.271`
- `news_risk_high->crypto_alt_1h` score `1.0255` n `62` status `ready` deltaP `2.7091` edge `0.1193` maxDD `-2.4854`
- `market_context_high->crypto_major_24h` score `0.927` n `100` status `ready` deltaP `6.3194` edge `0.3741` maxDD `-16.7906`
- `market_context_high->fx_4h` score `0.6734` n `100` status `ready` deltaP `17.4878` edge `0.0152` maxDD `-0.3868`
- `market_context_high->crypto_alt_4h` score `0.6601` n `100` status `ready` deltaP `-2.5549` edge `0.2444` maxDD `-7.1222`
- `news_risk_high->commodity_24h` score `0.4613` n `62` status `ready` deltaP `26.1537` edge `0.0414` maxDD `-8.196`
- `market_context_high->crypto_major_1h` score `0.3697` n `100` status `ready` deltaP `11.4132` edge `0.0602` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `0.3054` n `100` status `ready` deltaP `7.5988` edge `0.0124` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
