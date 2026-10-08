# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T10:52:34.775644+00:00`
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

- `market_context_high->unknown_4h` score `40.6027` n `90` status `ready` deltaP `-2.7981` edge `3.4561` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.1195` n `57` status `ready` deltaP `38.3318` edge `0.6914` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `8.6936` n `57` status `ready` deltaP `28.6478` edge `0.6271` maxDD `-4.823`
- `news_risk_high->equity_24h` score `7.5214` n `57` status `ready` deltaP `19.9255` edge `0.5039` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `5.7755` n `90` status `ready` deltaP `15.3195` edge `0.9357` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.3612` n `57` status `ready` deltaP `38.8601` edge `0.1877` maxDD `0.0`
- `market_context_high->equity_24h` score `3.4389` n `90` status `ready` deltaP `18.0541` edge `0.2091` maxDD `-1.0977`
- `news_risk_high->index_4h` score `3.2752` n `57` status `ready` deltaP `35.5103` edge `0.0624` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.9023` n `57` status `ready` deltaP `20.1085` edge `0.1676` maxDD `-2.7837`
- `news_risk_high->crypto_major_1h` score `2.7184` n `57` status `ready` deltaP `10.8704` edge `0.1896` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.5728` n `90` status `ready` deltaP `17.1037` edge `0.1968` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.4072` n `57` status `ready` deltaP `29.3545` edge `0.0189` maxDD `-0.1194`
- `news_risk_high->metal_4h` score `1.3919` n `57` status `ready` deltaP `20.6301` edge `0.0825` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.3523` n `57` status `ready` deltaP `3.2961` edge `0.1409` maxDD `-2.3482`
- `market_context_high->metal_24h` score `1.3279` n `90` status `ready` deltaP `22.4007` edge `0.1694` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.8308` n `90` status `ready` deltaP `19.082` edge `0.0167` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5729` n `90` status `ready` deltaP `10.2994` edge `0.0033` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.5166` n `90` status `ready` deltaP `9.0962` edge `0.5994` maxDD `-34.5048`
- `news_risk_high->equity_1h` score `0.3348` n `57` status `ready` deltaP `4.5593` edge `0.0565` maxDD `-0.7197`
- `news_risk_high->metal_1h` score `0.3345` n `57` status `ready` deltaP `10.2479` edge `0.0164` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
