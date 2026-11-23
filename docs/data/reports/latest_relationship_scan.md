# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T06:22:28.582758+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5240`

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

- `market_context_high->unknown_1h` score `16240.0021` n `83` status `ready` deltaP `2.5016` edge `1353.333` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10752.5557` n `82` status `ready` deltaP `3.5061` edge `896.0368` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1329.1931` n `31` status `ready` deltaP `3.2789` edge `110.7618` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1169.3233` n `31` status `ready` deltaP `3.9388` edge `97.423` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.2073` n `31` status `ready` deltaP `36.31` edge `0.7401` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.62` n `31` status `ready` deltaP `24.1689` edge `0.8109` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.389` n `31` status `ready` deltaP `12.8147` edge `0.8754` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7412` n `31` status `ready` deltaP `18.6401` edge `0.2062` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4614` n `31` status `ready` deltaP `36.31` edge `0.0724` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6375` n `31` status `ready` deltaP `30.9446` edge `0.022` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3652` n `31` status `ready` deltaP `9.1124` edge `0.2886` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9778` n `31` status `ready` deltaP `7.7651` edge `0.2375` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.494` n `31` status `ready` deltaP `28.5348` edge `0.0292` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.46` n `31` status `ready` deltaP `20.1318` edge `0.1087` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8367` n `31` status `ready` deltaP `18.1255` edge `0.0262` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.1333` n `82` status `ready` deltaP `10.9756` edge `0.0129` maxDD `-0.5181`
- `news_risk_high->commodity_1h` score `-0.0705` n `31` status `ready` deltaP `1.2314` edge `0.0121` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.1193` n `83` status `ready` deltaP `3.7389` edge `0.0116` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.1491` n `83` status `ready` deltaP `3.3114` edge `0.0044` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-1.0241` n `82` status `ready` deltaP `6.4025` edge `0.0124` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
