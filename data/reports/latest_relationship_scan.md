# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T17:22:31.885891+00:00`
- Price records: `672`
- Market context records: `5372`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11526`

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

- `market_context_high->unknown_24h` score `9.2311` n `177` status `ready` deltaP `17.0521` edge `0.6686` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.1409` n `177` status `ready` deltaP `21.875` edge `0.7366` maxDD `-29.6555`
- `market_context_high->equity_24h` score `3.0054` n `177` status `ready` deltaP `14.0449` edge `0.7197` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.9123` n `204` status `ready` deltaP `13.9855` edge `0.3787` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.2694` n `204` status `ready` deltaP `10.5003` edge `0.2832` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.4015` n `204` status `ready` deltaP `8.979` edge `0.2208` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.3419` n `177` status `ready` deltaP `17.3287` edge `0.0975` maxDD `-9.0959`
- `market_context_high->equity_1h` score `0.0495` n `205` status `ready` deltaP `5.9632` edge `0.0609` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.0062` n `177` status `ready` deltaP `8.5276` edge `0.0332` maxDD `-0.8294`
- `market_context_high->index_1h` score `-0.1158` n `205` status `ready` deltaP `4.2289` edge `0.0115` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.2041` n `205` status `ready` deltaP `3.576` edge `0.0837` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.2554` n `205` status `ready` deltaP `1.3305` edge `0.066` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4322` n `205` status `ready` deltaP `-0.804` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.6161` n `205` status `ready` deltaP `0.8814` edge `0.0103` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-1.153` n `204` status `ready` deltaP `0.8309` edge `0.0013` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.1988` n `204` status `ready` deltaP `8.0015` edge `-0.0348` maxDD `-6.1421`
- `market_context_high->index_4h` score `-1.2707` n `204` status `ready` deltaP `4.074` edge `0.0229` maxDD `-2.8094`
- `market_context_high->commodity_1h` score `-1.519` n `205` status `ready` deltaP `-3.7695` edge `-0.007` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.6466` n `204` status `ready` deltaP `-7.4187` edge `-0.0374` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.4976` n `177` status `ready` deltaP `12.5706` edge `0.3375` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
