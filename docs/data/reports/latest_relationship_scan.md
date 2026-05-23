# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T06:22:18.557651+00:00`
- Price records: `672`
- Market context records: `1603`
- Flow alert records: `6528`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `14.2043` n `183` status `ready` deltaP `31.1162` edge `1.0763` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `13.0465` n `183` status `ready` deltaP `27.5017` edge `1.1055` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.0834` n `183` status `ready` deltaP `27.2712` edge `0.855` maxDD `-8.0553`
- `market_context_high->equity_24h` score `5.5034` n `183` status `ready` deltaP `21.7356` edge `0.5464` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.3333` n `183` status `ready` deltaP `23.2269` edge `0.3149` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.2055` n `199` status `ready` deltaP `10.4264` edge `0.1404` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.1471` n `199` status `ready` deltaP `12.7972` edge `0.2655` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0432` n `199` status `ready` deltaP `8.9747` edge `0.2166` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.1761` n `183` status `ready` deltaP `7.7442` edge `0.0386` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3768` n `199` status `ready` deltaP `0.3686` edge `0.0516` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5455` n `199` status `ready` deltaP `0.9133` edge `0.0293` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.6024` n `199` status `ready` deltaP `-1.5451` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6805` n `199` status `ready` deltaP `0.4747` edge `0.0033` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7321` n `199` status `ready` deltaP `5.1478` edge `0.0054` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7788` n `199` status `ready` deltaP `-1.096` edge `-0.0004` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.9067` n `199` status `ready` deltaP `-0.8929` edge `0.0254` maxDD `-6.1883`
- `market_context_high->index_4h` score `-0.9521` n `199` status `ready` deltaP `-0.1716` edge `0.0307` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3835` n `199` status `ready` deltaP `9.4489` edge `0.0909` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.4124` n `199` status `ready` deltaP `-11.007` edge `-0.0148` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.1763` n `199` status `ready` deltaP `-13.9379` edge `-0.108` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
