# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T00:52:31.899430+00:00`
- Price records: `672`
- Market context records: `8569`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5919`

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

- `news_risk_high->unknown_24h` score `5076.2491` n `61` status `ready` deltaP `39.2759` edge `422.801` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9038` n `64` status `ready` deltaP `21.4177` edge `0.4089` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1494` n `64` status `ready` deltaP `18.0259` edge `0.078` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.025` n `62` status `ready` deltaP `14.1227` edge `0.1703` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7349` n `64` status `ready` deltaP `16.2519` edge `0.0839` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.1517` n `64` status `ready` deltaP `8.1174` edge `0.1711` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7253` n `64` status `ready` deltaP `13.7195` edge `0.1407` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4687` n `64` status `ready` deltaP `8.4113` edge `0.0567` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3945` n `64` status `ready` deltaP `7.5131` edge `0.0517` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0994` n `64` status `ready` deltaP `5.436` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.074` n `64` status `ready` deltaP `11.9284` edge `0.0224` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0169` n `64` status `ready` deltaP `3.7706` edge `0.0087` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0341` n `64` status `ready` deltaP `1.7149` edge `0.0318` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.0942` n `62` status `ready` deltaP `8.753` edge `0.0134` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.0964` n `64` status `ready` deltaP `3.7051` edge `0.0076` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2653` n `62` status `ready` deltaP `2.3614` edge `0.0005` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3294` n `62` status `ready` deltaP `3.8584` edge `-0.0054` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5081` n `62` status `ready` deltaP `-2.627` edge `0.0151` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7573` n `62` status `ready` deltaP `0.7968` edge `-0.0155` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9374` n `62` status `ready` deltaP `-2.5449` edge `-0.0117` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
