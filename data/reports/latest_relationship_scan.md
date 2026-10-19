# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T04:37:27.556816+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8757`

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

- `risk_on_high->equity_24h` score `2.9216` n `44` status `ready` deltaP `-15.9644` edge `0.8823` maxDD `-30.2591`
- `risk_on_and_context->equity_24h` score `2.9216` n `44` status `ready` deltaP `-15.9644` edge `0.8823` maxDD `-30.2591`
- `market_context_high->equity_24h` score `2.6845` n `77` status `ready` deltaP `3.1914` edge `1.1213` maxDD `-55.843`
- `market_context_high->crypto_major_24h` score `1.5622` n `77` status `ready` deltaP `4.9468` edge `0.777` maxDD `-35.1086`
- `market_context_high->commodity_24h` score `1.1997` n `77` status `ready` deltaP `13.6082` edge `0.0944` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.638` n `44` status `ready` deltaP `13.8548` edge `0.0207` maxDD `-2.1255`
- `risk_on_and_context->equity_1h` score `0.638` n `44` status `ready` deltaP `13.8548` edge `0.0207` maxDD `-2.1255`
- `market_context_high->crypto_major_4h` score `0.5686` n `77` status `ready` deltaP `5.1373` edge `0.3791` maxDD `-15.2359`
- `risk_on_high->index_1h` score `0.4549` n `44` status `ready` deltaP `10.2512` edge `0.0005` maxDD `-0.4746`
- `risk_on_and_context->index_1h` score `0.4549` n `44` status `ready` deltaP `10.2512` edge `0.0005` maxDD `-0.4746`
- `market_context_high->crypto_major_1h` score `0.2918` n `78` status `ready` deltaP `4.3797` edge `0.0971` maxDD `-3.7781`
- `risk_on_high->equity_4h` score `0.0793` n `44` status `ready` deltaP `6.7695` edge `0.1057` maxDD `-5.5375`
- `risk_on_and_context->equity_4h` score `0.0793` n `44` status `ready` deltaP `6.7695` edge `0.1057` maxDD `-5.5375`
- `risk_on_high->fx_4h` score `-0.07` n `44` status `ready` deltaP `2.1407` edge `0.0063` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.07` n `44` status `ready` deltaP `2.1407` edge `0.0063` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.1842` n `44` status `ready` deltaP `1.6721` edge `-0.0001` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.1842` n `44` status `ready` deltaP `1.6721` edge `-0.0001` maxDD `-0.1065`
- `risk_on_high->index_4h` score `-0.3708` n `44` status `ready` deltaP `7.2074` edge `0.009` maxDD `-1.0362`
- `risk_on_and_context->index_4h` score `-0.3708` n `44` status `ready` deltaP `7.2074` edge `0.009` maxDD `-1.0362`
- `market_context_high->fx_4h` score `-0.4397` n `77` status `ready` deltaP `0.1926` edge `0.0054` maxDD `-0.7115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
