# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T22:22:28.394746+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `12819`

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

- `market_context_high->equity_4h` score `0.6526` n `105` status `ready` deltaP `7.7889` edge `0.1654` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.5366` n `105` status `ready` deltaP `10.067` edge `0.0591` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.4065` n `105` status `ready` deltaP `11.306` edge `0.0072` maxDD `-0.5622`
- `market_context_high->fx_4h` score `-0.0066` n `105` status `ready` deltaP `6.5708` edge `0.0056` maxDD `-0.3539`
- `market_context_high->metal_4h` score `-0.0946` n `105` status `ready` deltaP `8.5119` edge `-0.0113` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.1176` n `96` status `ready` deltaP `4.6875` edge `0.137` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.1716` n `105` status `ready` deltaP `7.41` edge `0.021` maxDD `-1.7252`
- `market_context_high->fx_1h` score `-0.1788` n `105` status `ready` deltaP `1.3744` edge `0.0038` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.1886` n `105` status `ready` deltaP `3.3875` edge `0.0004` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.3811` n `105` status `ready` deltaP `8.0796` edge `-0.0629` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5158` n `105` status `ready` deltaP `1.4001` edge `0.0047` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6765` n `105` status `ready` deltaP `1.6866` edge `-0.0135` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7979` n `105` status `ready` deltaP `-3.4146` edge `0.0055` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8117` n `105` status `ready` deltaP `-6.7764` edge `-0.0023` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.4152` n `105` status `ready` deltaP `5.3484` edge `-0.0266` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.7886` n `105` status `ready` deltaP `7.5973` edge `-0.0976` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-3.4309` n `96` status `ready` deltaP `15.7986` edge `-0.3406` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.6069` n `96` status `ready` deltaP `1.0416` edge `-0.0526` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8522` n `96` status `ready` deltaP `-21.1805` edge `-0.0215` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9533` n `96` status `ready` deltaP `-21.0069` edge `-0.1642` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
