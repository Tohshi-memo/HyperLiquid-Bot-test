# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T12:52:27.680248+00:00`
- Price records: `672`
- Market context records: `4935`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9400`

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

- `market_context_high->unknown_1h` score `18.1265` n `99` status `ready` deltaP `10.6802` edge `1.4811` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.7411` n `99` status `ready` deltaP `29.2267` edge `0.835` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `7.2302` n `99` status `ready` deltaP `23.2416` edge `0.5828` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `7.1243` n `99` status `ready` deltaP `21.0305` edge `0.5759` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `6.0756` n `86` status `ready` deltaP `26.5141` edge `0.3638` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.8176` n `99` status `ready` deltaP `15.7521` edge `0.1846` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.434` n `99` status `ready` deltaP `10.7` edge `0.1144` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.8809` n `99` status `ready` deltaP `11.5777` edge `0.0424` maxDD `-0.6938`
- `market_context_high->crypto_major_1h` score `0.6773` n `99` status `ready` deltaP `7.0163` edge `0.1439` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4783` n `99` status `ready` deltaP `7.7633` edge `0.1118` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.4776` n `99` status `ready` deltaP `6.7154` edge `0.0738` maxDD `-2.5875`
- `market_context_high->metal_1h` score `0.0317` n `99` status `ready` deltaP `3.874` edge `0.0348` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.3847` n `99` status `ready` deltaP `1.3291` edge `0.0078` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.467` n `99` status `ready` deltaP `0.617` edge `0.0115` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.9781` n `99` status `ready` deltaP `6.0683` edge `-0.0033` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.0217` n `99` status `ready` deltaP `-4.641` edge `-0.003` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.4202` n `99` status `ready` deltaP `-7.8737` edge `-0.0046` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.8024` n `86` status `ready` deltaP `-5.0509` edge `-0.0155` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-5.1228` n `86` status `ready` deltaP `12.9724` edge `-0.0025` maxDD `-27.5371`
- `market_context_high->index_24h` score `-7.5605` n `86` status `ready` deltaP `-9.9281` edge `-0.1553` maxDD `-24.6845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
