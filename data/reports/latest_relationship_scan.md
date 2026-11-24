# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T02:37:26.868795+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `32382.3001` n `45` status `ready` deltaP `2.3153` edge `2698.519` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22235.4784` n `45` status `ready` deltaP `3.33` edge `1852.9482` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1172.7708` n `31` status `ready` deltaP `2.5304` edge `97.7316` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1000.1252` n `31` status `ready` deltaP `4.5486` edge `83.3191` maxDD `-0.119`
- `news_risk_high->equity_24h` score `37.0072` n `31` status `ready` deltaP `43.0556` edge `2.7969` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.8737` n `31` status `ready` deltaP `45.4861` edge `2.6029` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.804` n `31` status `ready` deltaP `45.6597` edge `2.2626` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.95` n `31` status `ready` deltaP `42.798` edge `0.738` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.6592` n `31` status `ready` deltaP `23.864` edge `0.8162` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6491` n `31` status `ready` deltaP `30.8222` edge `0.5635` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6267` n `31` status `ready` deltaP `56.4684` edge `0.1886` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.5584` n `31` status `ready` deltaP `13.8818` edge `0.89` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.7028` n `31` status `ready` deltaP `40.625` edge `0.2044` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2852` n `31` status `ready` deltaP `18.191` edge `0.1712` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.2356` n `45` status `ready` deltaP `38.6246` edge `0.0406` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8166` n `31` status `ready` deltaP `31.2795` edge `0.0522` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5021` n `31` status `ready` deltaP `29.8967` edge `0.0177` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4968` n `31` status `ready` deltaP `10.9088` edge `0.2935` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.114` n `31` status `ready` deltaP `10.1603` edge `0.239` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5874` n `31` status `ready` deltaP `30.4809` edge `0.0282` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
