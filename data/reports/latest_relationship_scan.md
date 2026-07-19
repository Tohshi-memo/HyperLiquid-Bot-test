# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T20:07:30.896913+00:00`
- Price records: `672`
- Market context records: `7286`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13807`

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

- `market_context_high->fx_1h` score `-0.1973` n `130` status `ready` deltaP `3.3957` edge `0.001` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.7231` n `130` status `ready` deltaP `-2.2523` edge `-0.0156` maxDD `-1.9668`
- `market_context_high->fx_4h` score `-0.8103` n `128` status `ready` deltaP `6.2691` edge `0.0143` maxDD `-1.4649`
- `market_context_high->crypto_alt_1h` score `-0.8363` n `130` status `ready` deltaP `-2.029` edge `0.0102` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.9232` n `130` status `ready` deltaP `1.8586` edge `0.0103` maxDD `-7.6171`
- `market_context_high->fx_24h` score `-0.9815` n `125` status `ready` deltaP `-0.5913` edge `0.0009` maxDD `-2.1564`
- `market_context_high->unknown_1h` score `-1.1742` n `130` status `ready` deltaP `0.707` edge `-0.0929` maxDD `-1.3212`
- `market_context_high->commodity_4h` score `-1.242` n `128` status `ready` deltaP `1.1014` edge `-0.014` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-1.2684` n `128` status `ready` deltaP `6.7454` edge `0.0852` maxDD `-6.2026`
- `market_context_high->index_1h` score `-1.5255` n `130` status `ready` deltaP `-7.3897` edge `-0.0106` maxDD `-2.3805`
- `market_context_high->metal_1h` score `-2.3259` n `130` status `ready` deltaP `-10.5735` edge `-0.0075` maxDD `-1.9332`
- `market_context_high->metal_4h` score `-2.6037` n `128` status `ready` deltaP `-11.3186` edge `-0.0128` maxDD `-4.6441`
- `market_context_high->commodity_24h` score `-2.9329` n `125` status `ready` deltaP `-5.4957` edge `-0.128` maxDD `-2.3815`
- `market_context_high->crypto_alt_4h` score `-4.0879` n `128` status `ready` deltaP `-1.1243` edge `-0.0284` maxDD `-17.7144`
- `market_context_high->equity_1h` score `-4.7997` n `130` status `ready` deltaP `-11.0857` edge `-0.0734` maxDD `-15.5469`
- `market_context_high->crypto_major_4h` score `-5.163` n `128` status `ready` deltaP `-1.1433` edge `-0.0332` maxDD `-23.4879`
- `market_context_high->index_4h` score `-5.4227` n `128` status `ready` deltaP `-15.6728` edge `-0.066` maxDD `-12.1795`
- `market_context_high->unknown_24h` score `-5.8592` n `126` status `ready` deltaP `-10.8383` edge `-0.0551` maxDD `-16.8727`
- `market_context_high->metal_24h` score `-11.7831` n `126` status `ready` deltaP `-29.8115` edge `-0.1381` maxDD `-24.9399`
- `market_context_high->index_24h` score `-14.1964` n `125` status `ready` deltaP `-29.6` edge `-0.1766` maxDD `-38.3944`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
