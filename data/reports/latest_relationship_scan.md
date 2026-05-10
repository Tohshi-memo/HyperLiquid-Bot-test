# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T10:41:43.577871+00:00`
- Price records: `672`
- Market context records: `967`
- Flow alert records: `2709`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `15.0111` n `150` status `ready` deltaP `33.9931` edge `1.0577` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.4356` n `150` status `ready` deltaP `10.5903` edge `0.7157` maxDD `0.0`
- `market_context_high->equity_24h` score `1.3523` n `150` status `ready` deltaP `1.0` edge `0.3665` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.6541` n `150` status `ready` deltaP `-0.5972` edge `0.258` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2933` n `204` status `ready` deltaP `2.721` edge `0.0382` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3742` n `204` status `ready` deltaP `1.3503` edge `0.0011` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6405` n `204` status `ready` deltaP `1.1389` edge `0.0159` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.674` n `192` status `ready` deltaP `1.7149` edge `0.0018` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7243` n `204` status `ready` deltaP `2.8942` edge `0.0057` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-0.7893` n `204` status `ready` deltaP `-1.5792` edge `-0.0135` maxDD `-3.5069`
- `market_context_high->equity_4h` score `-1.3252` n `192` status `ready` deltaP `1.9309` edge `0.0919` maxDD `-10.5498`
- `market_context_high->crypto_major_1h` score `-1.6278` n `204` status `ready` deltaP `6.4283` edge `-0.0062` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.6358` n `192` status `ready` deltaP `-1.5371` edge `0.0262` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8962` n `204` status `ready` deltaP `-2.5155` edge `-0.0304` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-1.9685` n `204` status `ready` deltaP `0.8894` edge `-0.026` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.4845` n `192` status `ready` deltaP `8.9939` edge `0.1036` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-2.7411` n `192` status `ready` deltaP `-0.7749` edge `0.081` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.1761` n `192` status `ready` deltaP `7.7617` edge `-0.1286` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.2141` n `192` status `ready` deltaP `-1.8801` edge `0.0225` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-3.9713` n `150` status `ready` deltaP `5.3611` edge `0.0057` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
