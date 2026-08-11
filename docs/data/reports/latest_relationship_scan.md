# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T07:07:28.327803+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `46.9918` n `127` status `ready` deltaP `-18.7803` edge `4.2866` maxDD `-9.6329`
- `market_context_high->commodity_24h` score `2.6889` n `127` status `ready` deltaP `14.7246` edge `0.2146` maxDD `-3.0953`
- `risk_on_high->commodity_1h` score `1.099` n `31` status `ready` deltaP `11.7539` edge `0.0365` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.099` n `31` status `ready` deltaP `11.7539` edge `0.0365` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.7618` n `180` status `ready` deltaP `10.1231` edge `0.0297` maxDD `-0.6965`
- `market_context_high->commodity_4h` score `0.661` n `169` status `ready` deltaP `10.3267` edge `0.0577` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.4947` n `127` status `ready` deltaP `16.8875` edge `0.0316` maxDD `-1.4613`
- `risk_on_high->index_1h` score `0.3857` n `31` status `ready` deltaP `11.073` edge `0.0085` maxDD `-0.2966`
- `risk_on_and_context->index_1h` score `0.3857` n `31` status `ready` deltaP `11.073` edge `0.0085` maxDD `-0.2966`
- `risk_on_high->fx_1h` score `-0.0453` n `31` status `ready` deltaP `2.5932` edge `0.0017` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `-0.0453` n `31` status `ready` deltaP `2.5932` edge `0.0017` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.1574` n `180` status `ready` deltaP `3.3101` edge `0.0001` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.2705` n `169` status `ready` deltaP `3.3288` edge `0.0036` maxDD `-0.504`
- `risk_on_high->equity_1h` score `-0.6634` n `31` status `ready` deltaP `-3.3948` edge `-0.0142` maxDD `-1.5242`
- `risk_on_and_context->equity_1h` score `-0.6634` n `31` status `ready` deltaP `-3.3948` edge `-0.0142` maxDD `-1.5242`
- `market_context_high->index_1h` score `-0.8905` n `180` status `ready` deltaP `-7.8875` edge `-0.0039` maxDD `-0.948`
- `market_context_high->metal_1h` score `-1.1051` n `180` status `ready` deltaP `-8.0605` edge `-0.016` maxDD `-2.0884`
- `risk_on_high->crypto_major_1h` score `-1.2202` n `31` status `ready` deltaP `2.7429` edge `-0.0618` maxDD `-2.6536`
- `risk_on_and_context->crypto_major_1h` score `-1.2202` n `31` status `ready` deltaP `2.7429` edge `-0.0618` maxDD `-2.6536`
- `market_context_high->index_4h` score `-1.4117` n `169` status `ready` deltaP `-3.0622` edge `-0.0078` maxDD `-1.4875`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
