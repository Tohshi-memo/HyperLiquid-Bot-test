# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T11:22:35.461646+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.2227` n `84` status `ready` deltaP `7.8918` edge `0.2534` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.5164` n `84` status `ready` deltaP `16.6254` edge `0.2669` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.0389` n `96` status `ready` deltaP `9.3127` edge `0.0549` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.8051` n `96` status `ready` deltaP `15.0406` edge `0.0244` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.7704` n `96` status `ready` deltaP `9.629` edge `0.1021` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.6599` n `96` status `ready` deltaP `12.9179` edge `0.0076` maxDD `-0.0982`
- `market_context_high->crypto_alt_4h` score `0.6034` n `96` status `ready` deltaP `10.9756` edge `0.1041` maxDD `-5.4926`
- `market_context_high->unknown_1h` score `0.5712` n `96` status `ready` deltaP `9.6557` edge `0.0059` maxDD `-0.4807`
- `market_context_high->unknown_24h` score `-0.0055` n `84` status `ready` deltaP `14.3105` edge `-0.0781` maxDD `-0.0875`
- `market_context_high->metal_1h` score `-0.0405` n `96` status `ready` deltaP `4.0232` edge `0.0085` maxDD `-0.4291`
- `market_context_high->equity_4h` score `-0.0501` n `96` status `ready` deltaP `2.0071` edge `0.0729` maxDD `-2.5696`
- `market_context_high->fx_4h` score `-0.2416` n `96` status `ready` deltaP `2.9217` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->crypto_alt_1h` score `-0.3441` n `96` status `ready` deltaP `2.5262` edge `0.0192` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.3757` n `96` status `ready` deltaP `4.0905` edge `0.0096` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4631` n `96` status `ready` deltaP `-3.7176` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4671` n `96` status `ready` deltaP `1.4845` edge `0.0147` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.5677` n `96` status `ready` deltaP `1.0924` edge `0.0109` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8557` n `96` status `ready` deltaP `-7.142` edge `-0.0055` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.9611` n `84` status `ready` deltaP `-6.8086` edge `0.0186` maxDD `-6.9709`
- `market_context_high->index_24h` score `-4.4013` n `84` status `ready` deltaP `-14.653` edge `-0.1783` maxDD `-12.0629`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
