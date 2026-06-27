# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T11:37:27.973100+00:00`
- Price records: `672`
- Market context records: `4929`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9400`

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

- `market_context_high->unknown_1h` score `16.8164` n `103` status `ready` deltaP `10.6389` edge `1.3722` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.2375` n `103` status `ready` deltaP `28.9619` edge `0.7948` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `7.1629` n `103` status `ready` deltaP `24.035` edge `0.5719` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.7057` n `103` status `ready` deltaP `19.0682` edge `0.5541` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `6.0346` n `85` status `ready` deltaP `26.391` edge `0.3612` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3469` n `103` status `ready` deltaP `10.1054` edge `0.1111` maxDD `-1.9651`
- `market_context_high->equity_4h` score `1.0001` n `103` status `ready` deltaP `13.3155` edge `0.1776` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.6778` n `103` status `ready` deltaP `9.2633` edge `0.0409` maxDD `-0.6938`
- `market_context_high->crypto_major_1h` score `0.4479` n `103` status `ready` deltaP `5.4255` edge `0.1251` maxDD `-5.6406`
- `market_context_high->equity_1h` score `0.3654` n `103` status `ready` deltaP `5.7889` edge `0.0656` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.2711` n `103` status `ready` deltaP `6.1653` edge `0.0959` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.0377` n `103` status `ready` deltaP `3.2614` edge `0.0331` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2089` n `103` status `ready` deltaP `3.4794` edge `0.016` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5167` n `103` status `ready` deltaP `-0.2631` edge `0.011` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.7074` n `103` status `ready` deltaP `8.1474` edge `0.0054` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-0.908` n `103` status `ready` deltaP `-2.6359` edge `-0.0018` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.5203` n `103` status `ready` deltaP `-9.0649` edge `-0.005` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-2.0348` n `85` status `ready` deltaP `-7.6859` edge `-0.0173` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.9999` n `85` status `ready` deltaP `-10.5985` edge `-0.1618` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.0743` n `85` status `ready` deltaP `13.2639` edge `-0.0004` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
