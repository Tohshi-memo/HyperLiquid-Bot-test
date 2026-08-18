# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T07:37:28.085249+00:00`
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

- `market_context_high->crypto_major_24h` score `2.2696` n `76` status `ready` deltaP `6.2734` edge `0.2681` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.1634` n `76` status `ready` deltaP `13.9765` edge `0.2393` maxDD `-4.666`
- `market_context_high->equity_1h` score `0.926` n `97` status `ready` deltaP `8.5762` edge `0.0504` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.6601` n `95` status `ready` deltaP `13.7532` edge `0.0209` maxDD `-1.273`
- `market_context_high->index_1h` score `0.5823` n `97` status `ready` deltaP `12.0532` edge `0.0069` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5148` n `97` status `ready` deltaP `9.3108` edge `0.0035` maxDD `-0.4807`
- `market_context_high->crypto_major_4h` score `0.4225` n `95` status `ready` deltaP `8.9185` edge `0.0968` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `0.3835` n `95` status `ready` deltaP `11.0526` edge `0.1072` maxDD `-5.5373`
- `market_context_high->unknown_24h` score `0.1041` n `76` status `ready` deltaP `14.7131` edge `-0.0706` maxDD `-0.1719`
- `market_context_high->metal_1h` score `-0.1157` n `97` status `ready` deltaP `3.3088` edge `0.007` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.2309` n `95` status `ready` deltaP `3.06` edge `0.0005` maxDD `-0.3734`
- `market_context_high->equity_4h` score `-0.2334` n `95` status `ready` deltaP `1.4859` edge `0.0611` maxDD `-2.5696`
- `market_context_high->commodity_4h` score `-0.2957` n `95` status `ready` deltaP `4.9984` edge `0.0138` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.3159` n `97` status `ready` deltaP `2.71` edge `0.0216` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4533` n `97` status `ready` deltaP `-3.4416` edge `0.001` maxDD `-0.2273`
- `market_context_high->crypto_major_1h` score `-0.499` n `97` status `ready` deltaP `1.0803` edge `0.0133` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.5954` n `95` status `ready` deltaP `0.5055` edge `0.0093` maxDD `-0.3165`
- `market_context_high->commodity_1h` score `-0.9198` n `97` status `ready` deltaP `-7.4326` edge `-0.0071` maxDD `-1.5684`
- `market_context_high->metal_24h` score `-1.0126` n `76` status `ready` deltaP `-2.0774` edge `0.0416` maxDD `-4.6062`
- `market_context_high->index_24h` score `-3.1161` n `76` status `ready` deltaP `-9.6711` edge `-0.1427` maxDD `-7.3861`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
