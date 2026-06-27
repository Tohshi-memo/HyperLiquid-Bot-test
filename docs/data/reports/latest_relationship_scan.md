# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T16:07:27.238010+00:00`
- Price records: `672`
- Market context records: `4949`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9472`

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

- `market_context_high->unknown_1h` score `19.0951` n `96` status `ready` deltaP `9.5122` edge `1.5696` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.2063` n `93` status `ready` deltaP `27.9013` edge `0.8826` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.2415` n `93` status `ready` deltaP `20.9513` edge `0.5862` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.0143` n `93` status `ready` deltaP `21.5775` edge `0.5759` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.775` n `92` status `ready` deltaP `27.1966` edge `0.3342` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7838` n `93` status `ready` deltaP `14.685` edge `0.1889` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.664` n `93` status `ready` deltaP `12.6294` edge `0.1207` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.9917` n `93` status `ready` deltaP `12.6623` edge `0.0444` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.8642` n `96` status `ready` deltaP `7.8842` edge `0.0768` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8458` n `96` status `ready` deltaP `8.6514` edge `0.1546` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.6658` n `96` status `ready` deltaP `9.5247` edge `0.1241` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.0858` n `96` status `ready` deltaP `4.3413` edge `0.0362` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.3639` n `96` status `ready` deltaP `1.8026` edge `0.0073` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4136` n `96` status `ready` deltaP `1.4783` edge `0.0126` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.9473` n `93` status `ready` deltaP `6.6188` edge `-0.0044` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.1646` n `93` status `ready` deltaP `-7.1499` edge `-0.0046` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.3287` n `92` status `ready` deltaP `0.0906` edge `-0.0103` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.6085` n `96` status `ready` deltaP `-10.0923` edge `-0.0055` maxDD `-0.5675`
- `market_context_high->commodity_24h` score `-3.902` n `92` status `ready` deltaP `20.2219` edge `0.0509` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.898` n `92` status `ready` deltaP `-9.2618` edge `0.0324` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
