# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T08:07:28.342314+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7346`

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

- `news_risk_high->unknown_24h` score `2612.9076` n `139` status `ready` deltaP `1.2153` edge `217.7342` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.2562` n `139` status `ready` deltaP `32.9349` edge `1.5303` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.0408` n `139` status `ready` deltaP `33.4007` edge `0.8697` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `9.1245` n `139` status `ready` deltaP `27.498` edge `1.0205` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.1591` n `139` status `ready` deltaP `37.8173` edge `0.164` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.8528` n `139` status `ready` deltaP `31.2388` edge `0.2983` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4871` n `139` status `ready` deltaP `27.4785` edge `0.185` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.9167` n `139` status `ready` deltaP `8.4982` edge `0.2857` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.8796` n `142` status `ready` deltaP `7.5694` edge `0.1139` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6469` n `142` status `ready` deltaP `8.4507` edge `0.0637` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4586` n `142` status `ready` deltaP `8.6004` edge `0.0099` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0855` n `139` status `ready` deltaP `7.7251` edge `0.0267` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4367` n `142` status `ready` deltaP `1.3916` edge `0.063` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.511` n `142` status `ready` deltaP `1.3135` edge `0.0116` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.3319` n `139` status `ready` deltaP `8.61` edge `-0.0068` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4388` n `139` status `ready` deltaP `-9.0037` edge `0.025` maxDD `-3.6214`
- `news_risk_high->fx_1h` score `-1.8936` n `142` status `ready` deltaP `-9.8929` edge `-0.0038` maxDD `-1.0436`
- `news_risk_high->crypto_major_4h` score `-1.9051` n `139` status `ready` deltaP `-5.2433` edge `0.0622` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0668` n `142` status `ready` deltaP `-12.2986` edge `-0.0155` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-4.0265` n `139` status `ready` deltaP `-12.2368` edge `-0.0121` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
