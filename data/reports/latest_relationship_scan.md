# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T23:07:44.839070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3815`

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

- `news_risk_high->crypto_alt_4h` score `0.0229` n `146` status `ready` deltaP `8.0668` edge `0.2128` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5026` n `146` status `ready` deltaP `2.4813` edge `0.0418` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6809` n `146` status `ready` deltaP `-2.2229` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8628` n `146` status `ready` deltaP `1.6467` edge `-0.0029` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4231` n `146` status `ready` deltaP `-6.8944` edge `-0.0143` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5232` n `146` status `ready` deltaP `-8.689` edge `-0.0122` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.931` n `146` status `ready` deltaP `-0.8353` edge `-0.0119` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1885` n `146` status `ready` deltaP `-8.0285` edge `0.0078` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.4336` n `146` status `ready` deltaP `-8.0106` edge `0.0256` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4589` n `146` status `ready` deltaP `-18.8368` edge `-0.0188` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6383` n `146` status `ready` deltaP `-6.7857` edge `-0.0254` maxDD `-16.4088`
- `news_risk_high->commodity_4h` score `-3.2102` n `146` status `ready` deltaP `-9.8835` edge `0.0338` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.2597` n `146` status `ready` deltaP `-7.1077` edge `-0.0517` maxDD `-9.4709`
- `news_risk_high->metal_24h` score `-4.4757` n `146` status `ready` deltaP `0.1517` edge `-0.0158` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.9883` n `146` status `ready` deltaP `-6.6906` edge `-0.0506` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.2473` n `146` status `ready` deltaP `-11.6397` edge `-0.1244` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-10.4376` n `146` status `ready` deltaP `11.8809` edge `0.2821` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-11.0919` n `146` status `ready` deltaP `-0.378` edge `-0.0857` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.5733` n `146` status `ready` deltaP `-20.6807` edge `-0.0005` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-11.9179` n `146` status `ready` deltaP `11.8809` edge `0.378` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
