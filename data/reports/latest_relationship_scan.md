# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T16:37:28.492169+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4038`

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

- `news_risk_high->equity_4h` score `2.437` n `104` status `ready` deltaP `16.5455` edge `0.2927` maxDD `-4.2454`
- `news_risk_high->equity_24h` score `1.0045` n `104` status `ready` deltaP `30.9023` edge `1.0814` maxDD `-86.0244`
- `news_risk_high->index_4h` score `0.9986` n `104` status `ready` deltaP `15.4784` edge `0.0278` maxDD `-0.4888`
- `news_risk_high->index_1h` score `0.0642` n `104` status `ready` deltaP `8.1644` edge `0.0035` maxDD `-0.6421`
- `news_risk_high->index_24h` score `-0.1682` n `104` status `ready` deltaP `2.8081` edge `0.1432` maxDD `-6.6786`
- `news_risk_high->equity_1h` score `-0.2351` n `104` status `ready` deltaP `2.7349` edge `0.0583` maxDD `-5.2009`
- `news_risk_high->fx_1h` score `-0.3899` n `104` status `ready` deltaP `-1.4567` edge `-0.0003` maxDD `-0.1984`
- `news_risk_high->crypto_major_4h` score `-0.5453` n `104` status `ready` deltaP `0.1642` edge `0.0976` maxDD `-9.1553`
- `news_risk_high->crypto_alt_4h` score `-0.5595` n `104` status `ready` deltaP `2.6267` edge `0.1744` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.7279` n `104` status `ready` deltaP `1.4337` edge `0.0199` maxDD `-5.8225`
- `news_risk_high->metal_1h` score `-0.7784` n `104` status `ready` deltaP `-1.5603` edge `-0.0078` maxDD `-0.733`
- `news_risk_high->fx_4h` score `-0.8113` n `104` status `ready` deltaP `-2.9667` edge `-0.0033` maxDD `-0.4745`
- `news_risk_high->metal_4h` score `-0.9734` n `104` status `ready` deltaP `-0.8325` edge `-0.0287` maxDD `-1.5773`
- `news_risk_high->fx_24h` score `-1.2118` n `104` status `ready` deltaP `-14.433` edge `0.0043` maxDD `-0.4086`
- `news_risk_high->crypto_major_1h` score `-1.4927` n `104` status `ready` deltaP `-3.8865` edge `-0.0046` maxDD `-4.1772`
- `news_risk_high->metal_24h` score `-2.8969` n `104` status `ready` deltaP `3.2573` edge `-0.2035` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.0712` n `104` status `ready` deltaP `-16.3462` edge `-0.0103` maxDD `-3.2657`
- `news_risk_high->commodity_4h` score `-5.3528` n `104` status `ready` deltaP `-28.3771` edge `-0.0311` maxDD `-9.3965`
- `news_risk_high->crypto_major_24h` score `-6.0069` n `104` status `ready` deltaP `-15.9436` edge `0.1865` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.1227` n `104` status `ready` deltaP `-24.5841` edge `-0.0136` maxDD `-35.9515`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
