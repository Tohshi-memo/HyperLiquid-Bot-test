# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T23:07:30.179417+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11310`

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

- `news_risk_high->unknown_1h` score `1800.081` n `33` status `ready` deltaP `0.9436` edge `150.024` maxDD `-0.8832`
- `risk_on_high->crypto_alt_24h` score `20.1776` n `91` status `ready` deltaP `36.1722` edge `1.4633` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.1776` n `91` status `ready` deltaP `36.1722` edge `1.4633` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.5889` n `201` status `ready` deltaP `27.7364` edge `1.1969` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.9291` n `91` status `ready` deltaP `42.0983` edge `0.5006` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9291` n `91` status `ready` deltaP `42.0983` edge `0.5006` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.6189` n `91` status `ready` deltaP `32.2015` edge `0.5061` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.6189` n `91` status `ready` deltaP `32.2015` edge `0.5061` maxDD `-3.8693`
- `market_context_high->equity_24h` score `7.3814` n `201` status `ready` deltaP `27.2569` edge `0.4334` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.2113` n `91` status `ready` deltaP `25.021` edge `1.1645` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2113` n `91` status `ready` deltaP `25.021` edge `1.1645` maxDD `-24.5429`
- `risk_on_high->equity_24h` score `5.7854` n `91` status `ready` deltaP `27.2569` edge `0.3004` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.7854` n `91` status `ready` deltaP `27.2569` edge `0.3004` maxDD `0.0`
- `risk_on_high->index_24h` score `4.5146` n `91` status `ready` deltaP `43.0575` edge `0.0934` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.5146` n `91` status `ready` deltaP `43.0575` edge `0.0934` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.6429` n `201` status `ready` deltaP `37.399` edge `0.0936` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.3614` n `91` status `ready` deltaP `31.8212` edge `0.0773` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.3614` n `91` status `ready` deltaP `31.8212` edge `0.0773` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.2369` n `201` status `ready` deltaP `24.9818` edge `0.1054` maxDD `-2.843`
- `news_risk_high->commodity_1h` score `1.9362` n `33` status `ready` deltaP `17.9369` edge `0.0584` maxDD `-0.3303`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
