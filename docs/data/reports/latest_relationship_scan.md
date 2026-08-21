# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T11:36:39.292846+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->equity_1h` score `0.4983` n `115` status `ready` deltaP `9.9779` edge `0.0565` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.4332` n `115` status `ready` deltaP `11.7105` edge `0.0068` maxDD `-0.5685`
- `market_context_high->fx_4h` score `0.1412` n `105` status `ready` deltaP `9.0098` edge `0.0083` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0585` n `115` status `ready` deltaP `3.4926` edge `0.0051` maxDD `-0.2043`
- `market_context_high->equity_4h` score `-0.0686` n `105` status `ready` deltaP `3.978` edge `0.1307` maxDD `-8.3685`
- `market_context_high->metal_4h` score `-0.2554` n `105` status `ready` deltaP `6.5302` edge `-0.0187` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3209` n `105` status `ready` deltaP `5.1234` edge `0.0171` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.4099` n `115` status `ready` deltaP `9.7137` edge `-0.0762` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.4201` n `115` status `ready` deltaP `1.2471` edge `-0.0037` maxDD `-0.503`
- `market_context_high->commodity_24h` score `-0.4595` n `105` status `ready` deltaP `4.4147` edge `0.1156` maxDD `-4.666`
- `market_context_high->commodity_1h` score `-0.6766` n `115` status `ready` deltaP `-4.7474` edge `0.0015` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7828` n `105` status `ready` deltaP `-3.1098` edge `0.0054` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-1.1696` n `115` status `ready` deltaP `-1.5907` edge `-0.0067` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.199` n `115` status `ready` deltaP `-3.0656` edge `-0.0488` maxDD `-2.7581`
- `market_context_high->fx_24h` score `-3.1597` n `105` status `ready` deltaP `-13.8641` edge `-0.0099` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-3.6876` n `105` status `ready` deltaP `-1.8162` edge `-0.1682` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-3.9885` n `105` status `ready` deltaP `-0.1771` edge `-0.2291` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.076` n `105` status `ready` deltaP `-4.2064` edge `-0.0443` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.3865` n `105` status `ready` deltaP `-16.7212` edge `-0.1201` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-4.483` n `105` status `ready` deltaP `9.6826` edge `-0.3875` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
