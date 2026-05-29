# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T12:22:20.577974+00:00`
- Price records: `672`
- Market context records: `2244`
- Flow alert records: `8352`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9203`

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

- `news_risk_high->crypto_alt_24h` score `25.3971` n `39` status `ready` deltaP `55.2885` edge `1.8067` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.1536` n `39` status `ready` deltaP `45.179` edge `1.0889` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.1782` n `39` status `ready` deltaP `36.1512` edge `1.0553` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.2142` n `131` status `ready` deltaP `32.8931` edge `0.8922` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.0563` n `131` status `ready` deltaP `39.1583` edge `0.7133` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.8385` n `39` status `ready` deltaP `36.1912` edge `0.6012` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `8.6715` n `39` status `ready` deltaP `23.2639` edge `1.0147` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `8.6008` n `119` status `ready` deltaP `29.5547` edge `0.6325` maxDD `-7.3572`
- `market_context_high->crypto_major_24h` score `6.2365` n `119` status `ready` deltaP `17.9417` edge `1.0692` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.9239` n `131` status `ready` deltaP `22.6715` edge `0.3879` maxDD `-1.6306`
- `market_context_high->index_4h` score `4.1569` n `131` status `ready` deltaP `31.5409` edge `0.1735` maxDD `-0.3228`
- `news_risk_high->commodity_4h` score `3.9045` n `43` status `ready` deltaP `33.2246` edge `0.3462` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.8594` n `131` status `ready` deltaP `23.1486` edge `0.2419` maxDD `-2.635`
- `news_risk_high->fx_24h` score `3.467` n `39` status `ready` deltaP `35.0828` edge `0.0735` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.2892` n `119` status `ready` deltaP `13.568` edge `0.2354` maxDD `-1.4737`
- `news_risk_high->index_24h` score `3.2698` n `39` status `ready` deltaP `12.3398` edge `0.2321` maxDD `-1.3507`
- `market_context_high->equity_24h` score `2.9154` n `119` status `ready` deltaP `21.0682` edge `0.2552` maxDD `-6.8828`
- `market_context_high->crypto_alt_1h` score `2.6227` n `143` status `ready` deltaP `15.1847` edge `0.2037` maxDD `-4.9097`
- `market_context_high->crypto_major_1h` score `2.3663` n `143` status `ready` deltaP `14.0855` edge `0.1734` maxDD `-2.6086`
- `news_risk_high->fx_4h` score `2.15` n `43` status `ready` deltaP `27.2794` edge `0.0157` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
