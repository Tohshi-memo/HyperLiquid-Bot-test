# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T13:22:28.151310+00:00`
- Price records: `672`
- Market context records: `7032`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `market_context_high->fx_1h` score `-0.2559` n `213` status `ready` deltaP `2.0108` edge `0.0012` maxDD `-0.4598`
- `market_context_high->crypto_alt_1h` score `-0.3089` n `213` status `ready` deltaP `2.1942` edge `0.0322` maxDD `-4.5815`
- `market_context_high->fx_4h` score `-0.4069` n `213` status `ready` deltaP `12.2467` edge `0.0086` maxDD `-1.3932`
- `market_context_high->metal_1h` score `-0.6644` n `213` status `ready` deltaP `-1.4998` edge `0.0016` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.6759` n `213` status `ready` deltaP `0.6093` edge `0.0004` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.9635` n `213` status `ready` deltaP `3.7116` edge `0.0302` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-1.099` n `213` status `ready` deltaP `-2.5751` edge `0.0045` maxDD `-2.6467`
- `market_context_high->unknown_24h` score `-1.2171` n `201` status `ready` deltaP `-7.8022` edge `0.3561` maxDD `-19.1435`
- `market_context_high->commodity_1h` score `-1.2587` n `213` status `ready` deltaP `-3.7594` edge `-0.0182` maxDD `-1.9306`
- `market_context_high->index_4h` score `-1.9144` n `213` status `ready` deltaP `6.0396` edge `-0.0158` maxDD `-12.2591`
- `market_context_high->unknown_4h` score `-1.9831` n `213` status `ready` deltaP `-6.0446` edge `0.0847` maxDD `-8.1064`
- `market_context_high->metal_4h` score `-2.0008` n `213` status `ready` deltaP `4.9367` edge `0.0089` maxDD `-5.5324`
- `market_context_high->commodity_4h` score `-2.0907` n `213` status `ready` deltaP `-3.8082` edge `-0.0328` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.4665` n `201` status `ready` deltaP `-1.6895` edge `-0.0634` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.6589` n `213` status `ready` deltaP `1.5824` edge `0.0271` maxDD `-22.2831`
- `market_context_high->equity_1h` score `-2.8156` n `213` status `ready` deltaP `3.5963` edge `-0.0138` maxDD `-14.9179`
- `market_context_high->crypto_major_4h` score `-2.9849` n `213` status `ready` deltaP `2.7103` edge `0.0277` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.7329` n `201` status `ready` deltaP `-2.84` edge `-0.0122` maxDD `-3.7285`
- `market_context_high->equity_4h` score `-7.2609` n `213` status `ready` deltaP `4.5824` edge `-0.0744` maxDD `-63.963`
- `market_context_high->metal_24h` score `-13.79` n `201` status `ready` deltaP `-12.6114` edge `-0.0592` maxDD `-40.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
