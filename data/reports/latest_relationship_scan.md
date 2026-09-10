# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T22:52:29.704326+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11296`

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

- `news_risk_high->unknown_1h` score `1877.6168` n `32` status `ready` deltaP `3.4057` edge `156.4689` maxDD `-0.8832`
- `risk_on_high->crypto_alt_24h` score `20.1584` n `91` status `ready` deltaP `36.1722` edge `1.4617` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.1584` n `91` status `ready` deltaP `36.1722` edge `1.4617` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.5697` n `201` status `ready` deltaP `27.7364` edge `1.1953` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.9001` n `91` status `ready` deltaP `41.9459` edge `0.4992` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9001` n `91` status `ready` deltaP `41.9459` edge `0.4992` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.5911` n `91` status `ready` deltaP `32.0491` edge `0.5048` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.5911` n `91` status `ready` deltaP `32.0491` edge `0.5048` maxDD `-3.8693`
- `market_context_high->equity_24h` score `7.2883` n `201` status `ready` deltaP `27.0833` edge `0.4268` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.2105` n `91` status `ready` deltaP `25.021` edge `1.1644` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2105` n `91` status `ready` deltaP `25.021` edge `1.1644` maxDD `-24.5429`
- `risk_on_high->equity_24h` score `5.6923` n `91` status `ready` deltaP `27.0833` edge `0.2938` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.6923` n `91` status `ready` deltaP `27.0833` edge `0.2938` maxDD `0.0`
- `risk_on_high->index_24h` score `4.4899` n `91` status `ready` deltaP `42.8839` edge `0.0925` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.4899` n `91` status `ready` deltaP `42.8839` edge `0.0925` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.6182` n `201` status `ready` deltaP `37.2254` edge `0.0927` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.3349` n `91` status `ready` deltaP `31.6688` edge `0.0761` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.3349` n `91` status `ready` deltaP `31.6688` edge `0.0761` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.2103` n `201` status `ready` deltaP `24.8294` edge `0.1042` maxDD `-2.843`
- `news_risk_high->commodity_1h` score `2.177` n `32` status `ready` deltaP `20.2096` edge `0.0625` maxDD `-0.2651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
