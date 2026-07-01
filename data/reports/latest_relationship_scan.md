# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T09:52:30.008388+00:00`
- Price records: `672`
- Market context records: `5340`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9524`

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

- `market_context_high->unknown_24h` score `17.9623` n `155` status `ready` deltaP `22.1472` edge `1.3582` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.5932` n `155` status `ready` deltaP `23.6682` edge `0.815` maxDD `-27.2019`
- `market_context_high->equity_24h` score `4.7955` n `155` status `ready` deltaP `17.8517` edge `0.8435` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `3.0295` n `194` status `ready` deltaP `13.3361` edge `0.3928` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9297` n `194` status `ready` deltaP `11.8839` edge `0.329` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.1076` n `194` status `ready` deltaP `11.1594` edge `0.2651` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.7676` n `155` status `ready` deltaP `24.6158` edge `0.0978` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.5446` n `194` status `ready` deltaP `8.462` edge `0.0855` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.249` n `155` status `ready` deltaP `10.5578` edge `0.0399` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.0921` n `194` status `ready` deltaP `6.8168` edge `0.0126` maxDD `-1.0296`
- `market_context_high->crypto_alt_1h` score `0.0314` n `194` status `ready` deltaP `1.9461` edge `0.0858` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.024` n `194` status `ready` deltaP `4.0419` edge `0.0956` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3384` n `194` status `ready` deltaP `0.8643` edge `-0.0002` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.3485` n `194` status `ready` deltaP `6.679` edge `0.0267` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.3708` n `194` status `ready` deltaP `1.7964` edge `0.008` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6312` n `194` status `ready` deltaP `2.7454` edge `0.0037` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2687` n `194` status `ready` deltaP `7.908` edge `-0.0402` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.3784` n `194` status `ready` deltaP `-2.727` edge `-0.0049` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.4351` n `194` status `ready` deltaP `-6.0048` edge `-0.0197` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.5203` n `155` status `ready` deltaP `12.1774` edge `0.3201` maxDD `-53.8745`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
