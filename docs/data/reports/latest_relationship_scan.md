# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T12:52:44.598134+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9968`

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

- `market_context_high->unknown_1h` score `99.5251` n `47` status `ready` deltaP `10.116` edge `8.2334` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.8291` n `46` status `ready` deltaP `31.0689` edge `3.4609` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `29.7469` n `46` status `ready` deltaP `26.0417` edge `2.3053` maxDD `0.0`
- `market_context_high->equity_24h` score `25.2312` n `46` status `ready` deltaP `28.4647` edge `1.9229` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `10.0879` n `103` status `ready` deltaP `3.3779` edge `1.7224` maxDD `-63.6743`
- `market_context_high->index_24h` score `8.2376` n `46` status `ready` deltaP `36.9716` edge `0.4487` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `7.4848` n `103` status `ready` deltaP `0.799` edge `1.3197` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.6445` n `46` status `ready` deltaP `31.4689` edge `0.1173` maxDD `-0.2042`
- `market_context_high->index_4h` score `3.076` n `47` status `ready` deltaP `34.941` edge `0.0388` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.6865` n `47` status `ready` deltaP `17.9067` edge `0.1463` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.3091` n `118` status `ready` deltaP `12.5038` edge `0.1581` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.9946` n `118` status `ready` deltaP `14.7493` edge `0.1114` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.6717` n `114` status `ready` deltaP `24.5561` edge `0.0392` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.347` n `103` status `ready` deltaP `30.7056` edge `0.1311` maxDD `-1.7159`
- `news_risk_high->commodity_24h` score `1.322` n `103` status `ready` deltaP `17.4976` edge `0.1114` maxDD `-2.431`
- `news_risk_high->metal_24h` score `1.0357` n `103` status `ready` deltaP `23.3431` edge `0.122` maxDD `-7.2536`
- `market_context_high->index_1h` score `1.017` n `47` status `ready` deltaP `15.2089` edge `0.0112` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9691` n `47` status `ready` deltaP `11.3167` edge `0.0456` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.8836` n `114` status `ready` deltaP `13.2435` edge `0.1985` maxDD `-13.719`
- `news_risk_high->metal_1h` score `0.764` n `118` status `ready` deltaP `16.0053` edge `0.0163` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
