# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T22:37:25.294996+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `12819`

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

- `market_context_high->equity_4h` score `0.62` n `105` status `ready` deltaP `7.6365` edge `0.1637` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.5498` n `105` status `ready` deltaP `10.2167` edge `0.0592` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.4065` n `105` status `ready` deltaP `11.306` edge `0.0072` maxDD `-0.5622`
- `market_context_high->fx_4h` score `-0.0066` n `105` status `ready` deltaP `6.5708` edge `0.0056` maxDD `-0.3539`
- `market_context_high->metal_4h` score `-0.1065` n `105` status `ready` deltaP `8.3595` edge `-0.0118` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.1191` n `96` status `ready` deltaP `4.6875` edge `0.1368` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.1788` n `105` status `ready` deltaP `1.3744` edge `0.0038` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.1811` n `105` status `ready` deltaP `7.2576` edge `0.0208` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.1898` n `105` status `ready` deltaP `3.3875` edge `0.0003` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.3787` n `105` status `ready` deltaP `8.0796` edge `-0.0627` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5259` n `105` status `ready` deltaP `1.2504` edge `0.0044` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6726` n `105` status `ready` deltaP `1.6866` edge `-0.013` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7892` n `105` status `ready` deltaP `-3.2622` edge `0.0056` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8195` n `105` status `ready` deltaP `-6.9261` edge `-0.0023` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.4296` n `105` status `ready` deltaP `5.3484` edge `-0.0278` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.7958` n `105` status `ready` deltaP `7.5973` edge `-0.0982` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-3.5` n `96` status `ready` deltaP `15.625` edge `-0.3452` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.6069` n `96` status `ready` deltaP `1.0416` edge `-0.0526` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8546` n `96` status `ready` deltaP `-21.1805` edge `-0.0217` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9518` n `96` status `ready` deltaP `-21.0069` edge `-0.164` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
