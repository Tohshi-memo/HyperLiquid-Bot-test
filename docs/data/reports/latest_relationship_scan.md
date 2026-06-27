# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T11:07:32.881676+00:00`
- Price records: `672`
- Market context records: `4927`
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

- `market_context_high->unknown_1h` score `16.8128` n `103` status `ready` deltaP `10.6389` edge `1.3719` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.1785` n `103` status `ready` deltaP `28.8095` edge `0.7909` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `7.1049` n `103` status `ready` deltaP `23.7301` edge `0.5691` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.6537` n `103` status `ready` deltaP `18.7633` edge `0.5518` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `6.0166` n `85` status `ready` deltaP `26.391` edge `0.3597` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3201` n `103` status `ready` deltaP `9.8005` edge `0.1109` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.9993` n `103` status `ready` deltaP `13.3155` edge `0.1775` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.6644` n `103` status `ready` deltaP `9.1109` edge `0.0408` maxDD `-0.6938`
- `market_context_high->crypto_major_1h` score `0.4331` n `103` status `ready` deltaP `5.2758` edge `0.1242` maxDD `-5.6406`
- `market_context_high->equity_1h` score `0.3483` n `103` status `ready` deltaP `5.4895` edge `0.0654` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.2579` n `103` status `ready` deltaP `6.0156` edge `0.0952` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.0497` n `103` status `ready` deltaP `3.1117` edge `0.0331` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2089` n `103` status `ready` deltaP `3.4794` edge `0.016` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.533` n `103` status `ready` deltaP `-0.5625` edge `0.0109` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.7122` n `103` status `ready` deltaP `8.1474` edge `0.005` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-0.9167` n `103` status `ready` deltaP `-2.7883` edge `-0.0019` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.5203` n `103` status `ready` deltaP `-9.0649` edge `-0.005` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-2.0348` n `85` status `ready` deltaP `-7.6859` edge `-0.0173` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.9999` n `85` status `ready` deltaP `-10.5985` edge `-0.1618` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.0767` n `85` status `ready` deltaP `13.2639` edge `-0.0006` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
