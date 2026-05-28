# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T18:22:18.099560+00:00`
- Price records: `672`
- Market context records: `2166`
- Flow alert records: `8131`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `market_context_high->crypto_alt_4h` score `13.0145` n `136` status `ready` deltaP `36.7467` edge `0.9332` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8155` n `136` status `ready` deltaP `41.6876` edge `0.7597` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4872` n `136` status `ready` deltaP `22.9017` edge `0.3795` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `3.9279` n `43` status `ready` deltaP `32.3099` edge `0.3553` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.8308` n `136` status `ready` deltaP `24.9282` edge `0.2625` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2654` n `136` status `ready` deltaP `17.5238` edge `0.203` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.0933` n `136` status `ready` deltaP `16.1765` edge `0.2363` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.8771` n `136` status `ready` deltaP `11.7749` edge `0.2841` maxDD `-4.1604`
- `market_context_high->index_4h` score `2.8427` n `136` status `ready` deltaP `22.9734` edge `0.1521` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.6978` n `136` status `ready` deltaP `27.594` edge `0.5729` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `2.4141` n `136` status `ready` deltaP `20.2104` edge `1.024` maxDD `-61.6059`
- `market_context_high->equity_24h` score `2.0792` n `136` status `ready` deltaP `24.0911` edge `0.5025` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `2.0759` n `43` status `ready` deltaP `26.5173` edge `0.0146` maxDD `-0.1382`
- `market_context_high->metal_4h` score `1.6524` n `136` status `ready` deltaP `18.3375` edge `0.1542` maxDD `-4.7664`
- `news_risk_high->unknown_4h` score `1.5441` n `43` status `ready` deltaP `15.8395` edge `0.0954` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.3877` n `43` status `ready` deltaP `-2.2264` edge `0.3135` maxDD `-4.6598`
- `news_risk_high->unknown_1h` score `1.3423` n `43` status `ready` deltaP `21.3445` edge `0.0165` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.8204` n `43` status `ready` deltaP `10.9142` edge `0.1004` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.5535` n `136` status `ready` deltaP `10.2986` edge `0.0563` maxDD `-2.6402`
- `news_risk_high->fx_1h` score `0.4621` n `43` status `ready` deltaP `8.1395` edge `0.0099` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
