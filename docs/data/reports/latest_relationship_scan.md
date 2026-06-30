# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T10:07:29.102002+00:00`
- Price records: `672`
- Market context records: `5238`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5602`

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

- `market_context_high->unknown_24h` score `23.4154` n `128` status `ready` deltaP `31.9444` edge `1.7573` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.1289` n `128` status `ready` deltaP `33.6806` edge `1.2357` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `6.6938` n `128` status `ready` deltaP `21.9618` edge `0.7626` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.1569` n `155` status `ready` deltaP `13.9989` edge `0.413` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.0204` n `155` status `ready` deltaP `14.8318` edge `0.4654` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.2288` n `155` status `ready` deltaP `17.2875` edge `0.1727` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8058` n `155` status `ready` deltaP `8.0896` edge `0.1607` maxDD `-2.7986`
- `market_context_high->equity_24h` score `1.3062` n `128` status `ready` deltaP `17.7952` edge `0.5531` maxDD `-40.0306`
- `market_context_high->fx_24h` score `0.5969` n `128` status `ready` deltaP `13.5417` edge `0.049` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.458` n `155` status `ready` deltaP `4.6533` edge `0.1033` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4097` n `155` status `ready` deltaP `6.553` edge `0.115` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.1651` n `155` status `ready` deltaP `6.483` edge `0.1344` maxDD `-7.4425`
- `market_context_high->index_24h` score `-0.1334` n `128` status `ready` deltaP `17.5347` edge `0.0295` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.1767` n `155` status `ready` deltaP `5.3699` edge `0.046` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1784` n `155` status `ready` deltaP `3.812` edge `0.0109` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.2314` n `155` status `ready` deltaP `3.3881` edge `0.0085` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.311` n `155` status `ready` deltaP `0.9108` edge `-0.0007` maxDD `-0.6194`
- `market_context_high->commodity_1h` score `-0.6655` n `155` status `ready` deltaP `-0.3226` edge `-0.0023` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.7568` n `155` status `ready` deltaP `0.595` edge `0.0024` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8813` n `155` status `ready` deltaP `3.3143` edge `0.0162` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
