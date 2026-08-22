# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T12:22:26.560824+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `market_context_high->unknown_1h` score `0.9932` n `145` status `ready` deltaP `7.4975` edge `0.0555` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.2279` n `136` status `ready` deltaP `18.5258` edge `-0.0606` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.082` n `136` status `ready` deltaP `7.6309` edge `0.0099` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0241` n `145` status `ready` deltaP `7.7225` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0147` n `145` status `ready` deltaP `4.3651` edge `0.0049` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2761` n `136` status `ready` deltaP `6.5549` edge `-0.0175` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.314` n `145` status `ready` deltaP `0.9756` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->equity_1h` score `-0.3546` n `145` status `ready` deltaP `4.3382` edge `0.0326` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.5284` n `136` status `ready` deltaP `3.6765` edge `0.0113` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.7164` n `136` status `ready` deltaP `-1.623` edge `0.004` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9068` n `145` status `ready` deltaP `-6.8191` edge `-0.0017` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.6877` n `136` status `ready` deltaP `-0.7442` edge `0.0691` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-1.7812` n `136` status `ready` deltaP `4.7614` edge `-0.0522` maxDD `-5.5715`
- `market_context_high->fx_24h` score `-1.8523` n `122` status `ready` deltaP `-0.296` edge `0.0086` maxDD `-2.2121`
- `market_context_high->commodity_24h` score `-1.9803` n `122` status `ready` deltaP `-5.5499` edge `0.0553` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.4044` n `145` status `ready` deltaP `-2.3983` edge `-0.0349` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.4282` n `145` status `ready` deltaP `-4.7718` edge `-0.108` maxDD `-7.6697`
- `market_context_high->index_24h` score `-4.4704` n `122` status `ready` deltaP `-8.1967` edge `-0.0456` maxDD `-20.4972`
- `market_context_high->metal_24h` score `-5.4358` n `122` status `ready` deltaP `-24.2856` edge `-0.2042` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.516` n `136` status `ready` deltaP `-1.3988` edge `-0.3207` maxDD `-5.3711`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
