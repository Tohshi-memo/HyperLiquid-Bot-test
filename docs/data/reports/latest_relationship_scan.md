# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T18:07:30.444336+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4096`

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

- `news_risk_high->equity_4h` score `2.516` n `98` status `ready` deltaP `17.1945` edge `0.2985` maxDD `-4.2454`
- `news_risk_high->index_4h` score `1.0977` n `98` status `ready` deltaP `16.538` edge `0.029` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.549` n `98` status `ready` deltaP `5.5236` edge `0.0921` maxDD `-1.6827`
- `news_risk_high->equity_24h` score `0.5154` n `98` status `ready` deltaP `29.583` edge `1.0275` maxDD `-86.0244`
- `news_risk_high->index_1h` score `0.2883` n `98` status `ready` deltaP `11.2795` edge `0.0071` maxDD `-0.2931`
- `news_risk_high->index_24h` score `-0.1745` n `98` status `ready` deltaP `3.4556` edge `0.1459` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.2699` n `98` status `ready` deltaP `0.7607` edge `0.0003` maxDD `-0.1984`
- `news_risk_high->metal_1h` score `-0.2958` n `98` status `ready` deltaP `0.2719` edge `-0.004` maxDD `-0.5256`
- `news_risk_high->crypto_major_4h` score `-0.2983` n `98` status `ready` deltaP `2.439` edge `0.1141` maxDD `-9.1553`
- `news_risk_high->crypto_alt_4h` score `-0.5574` n `98` status `ready` deltaP `1.8417` edge `0.1799` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6397` n `98` status `ready` deltaP `2.2455` edge `0.0258` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.7793` n `98` status `ready` deltaP `-2.3675` edge `-0.0032` maxDD `-0.4745`
- `news_risk_high->metal_4h` score `-0.8041` n `98` status `ready` deltaP `1.9133` edge `-0.0253` maxDD `-1.5773`
- `news_risk_high->crypto_major_1h` score `-0.8411` n `98` status `ready` deltaP `-2.5571` edge `0.0031` maxDD `-4.1772`
- `news_risk_high->fx_24h` score `-1.5622` n `98` status `ready` deltaP `-11.7586` edge `0.0105` maxDD `-0.3169`
- `news_risk_high->metal_24h` score `-2.8002` n `98` status `ready` deltaP `5.0119` edge `-0.2028` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.3445` n `98` status `ready` deltaP `-19.2381` edge `-0.015` maxDD `-3.1699`
- `news_risk_high->commodity_4h` score `-4.8967` n `98` status `ready` deltaP `-27.2585` edge `-0.0207` maxDD `-7.7841`
- `news_risk_high->crypto_major_24h` score `-6.0384` n `98` status `ready` deltaP `-14.314` edge `0.1716` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.7704` n `98` status `ready` deltaP `-24.7462` edge `-0.0138` maxDD `-33.501`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
