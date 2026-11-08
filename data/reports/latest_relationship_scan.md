# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T09:22:25.846105+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5181`

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

- `market_context_high->unknown_4h` score `125.2186` n `37` status `ready` deltaP `-3.9387` edge `10.5059` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.2856` n `37` status `ready` deltaP `10.6571` edge `0.2487` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1583` n `37` status `ready` deltaP `34.0763` edge `0.045` maxDD `-0.0521`
- `market_context_high->index_4h` score `2.0426` n `37` status `ready` deltaP `26.6604` edge `0.0395` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.3624` n `43` status `ready` deltaP `6.6053` edge `0.0916` maxDD `-0.1014`
- `news_risk_high->fx_4h` score `1.2222` n `45` status `ready` deltaP `17.2595` edge `0.0125` maxDD `-0.0571`
- `market_context_high->crypto_major_1h` score `0.8286` n `37` status `ready` deltaP `10.0502` edge `0.0606` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.5488` n `37` status `ready` deltaP `12.146` edge `0.0709` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.3978` n `37` status `ready` deltaP `6.773` edge `0.0151` maxDD `-0.1681`
- `news_risk_high->equity_4h` score `0.357` n `45` status `ready` deltaP `1.4804` edge `0.1098` maxDD `-4.2454`
- `market_context_high->index_1h` score `0.3344` n `37` status `ready` deltaP `2.3993` edge `0.0389` maxDD `-0.1621`
- `news_risk_high->fx_1h` score `0.153` n `46` status `ready` deltaP `5.4804` edge `0.0047` maxDD `-0.0625`
- `market_context_high->commodity_1h` score `0.1335` n `37` status `ready` deltaP `9.3179` edge `0.0096` maxDD `-1.7019`
- `news_risk_high->index_4h` score `0.0766` n `45` status `ready` deltaP `5.5793` edge `0.0204` maxDD `-0.4888`
- `market_context_high->commodity_4h` score `-0.0156` n `37` status `ready` deltaP `2.987` edge `0.0235` maxDD `-1.633`
- `news_risk_high->index_1h` score `-0.0535` n `46` status `ready` deltaP `5.3957` edge `0.0025` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0637` n `37` status `ready` deltaP `1.2017` edge `0.0166` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.314` n `46` status `ready` deltaP `-3.1502` edge `0.0357` maxDD `-1.396`
- `news_risk_high->index_24h` score `-0.4875` n `43` status `ready` deltaP `-0.8519` edge `0.11` maxDD `-6.6786`
- `market_context_high->equity_4h` score `-0.637` n `37` status `ready` deltaP `22.8618` edge `0.0939` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
