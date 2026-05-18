# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T00:52:16.247638+00:00`
- Price records: `672`
- Market context records: `1068`
- Flow alert records: `4978`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8669`

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

- `market_context_high->crypto_major_24h` score `15.5934` n `169` status `ready` deltaP `34.5903` edge `1.1152` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.283` n `169` status `ready` deltaP `11.8875` edge `0.4844` maxDD `-9.5387`
- `market_context_high->equity_24h` score `4.545` n `169` status `ready` deltaP `13.6065` edge `0.3377` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.9223` n `169` status `ready` deltaP `14.1244` edge `0.2635` maxDD `-2.1308`
- `market_context_high->metal_24h` score `3.4908` n `169` status `ready` deltaP `-4.1824` edge `0.4855` maxDD `-6.3373`
- `market_context_high->equity_4h` score `0.878` n `171` status `ready` deltaP `5.2194` edge `0.1172` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.3084` n `171` status `ready` deltaP `3.795` edge `0.0687` maxDD `-2.1308`
- `market_context_high->index_1h` score `-0.0394` n `171` status `ready` deltaP `5.369` edge `0.0179` maxDD `-1.8915`
- `market_context_high->fx_1h` score `-0.0538` n `171` status `ready` deltaP `5.7709` edge `0.0002` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.0938` n `171` status `ready` deltaP `8.4235` edge `0.0284` maxDD `-5.3898`
- `market_context_high->crypto_major_4h` score `-0.1479` n `171` status `ready` deltaP `10.2116` edge `0.1226` maxDD `-9.2399`
- `market_context_high->equity_1h` score `-0.1874` n `171` status `ready` deltaP `1.8183` edge `0.0383` maxDD `-3.6162`
- `market_context_high->metal_1h` score `-0.396` n `171` status `ready` deltaP `6.136` edge `-0.0157` maxDD `-3.4119`
- `market_context_high->fx_4h` score `-0.6869` n `171` status `ready` deltaP `1.3622` edge `0.0025` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-0.8181` n `171` status `ready` deltaP `2.6272` edge `0.0229` maxDD `-5.3538`
- `market_context_high->commodity_1h` score `-1.0398` n `171` status `ready` deltaP `-1.5557` edge `0.0045` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.4785` n `171` status `ready` deltaP `3.9643` edge `0.1008` maxDD `-13.0347`
- `market_context_high->metal_4h` score `-2.2562` n `171` status `ready` deltaP `1.9273` edge `-0.1067` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-2.7146` n `171` status `ready` deltaP `-8.1551` edge `0.0231` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.0329` n `169` status `ready` deltaP `5.9093` edge `-0.0206` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
