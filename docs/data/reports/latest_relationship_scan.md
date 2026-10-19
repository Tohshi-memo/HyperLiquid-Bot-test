# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T03:37:26.474602+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->commodity_24h` score `1.3652` n `81` status `ready` deltaP `14.3875` edge `0.103` maxDD `-1.8119`
- `market_context_high->equity_24h` score `1.1903` n `81` status `ready` deltaP `2.6044` edge `1.0007` maxDD `-55.843`
- `risk_on_high->equity_1h` score `1.0274` n `48` status `ready` deltaP `17.3423` edge `0.0299` maxDD `-2.1255`
- `risk_on_and_context->equity_1h` score `1.0274` n `48` status `ready` deltaP `17.3423` edge `0.0299` maxDD `-2.1255`
- `market_context_high->crypto_major_24h` score `0.8096` n `81` status `ready` deltaP `3.9738` edge `0.687` maxDD `-35.1086`
- `market_context_high->crypto_major_4h` score `0.7888` n `81` status `ready` deltaP `7.7668` edge `0.3898` maxDD `-15.2359`
- `risk_on_high->index_1h` score `0.5892` n `48` status `ready` deltaP `11.8056` edge `0.0014` maxDD `-0.4804`
- `risk_on_and_context->index_1h` score `0.5892` n `48` status `ready` deltaP `11.8056` edge `0.0014` maxDD `-0.4804`
- `market_context_high->crypto_major_1h` score `0.5687` n `82` status `ready` deltaP `5.9698` edge `0.122` maxDD `-3.7781`
- `risk_on_high->fx_1h` score `0.0516` n `48` status `ready` deltaP `5.6494` edge `0.0013` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `0.0516` n `48` status `ready` deltaP `5.6494` edge `0.0013` maxDD `-0.1065`
- `risk_on_high->commodity_24h` score `-0.0251` n `48` status `ready` deltaP `11.5326` edge `0.0008` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.0251` n `48` status `ready` deltaP `11.5326` edge `0.0008` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `-0.2715` n `48` status `ready` deltaP `0.0574` edge `0.0038` maxDD `-0.1446`
- `risk_on_and_context->fx_4h` score `-0.2715` n `48` status `ready` deltaP `0.0574` edge `0.0038` maxDD `-0.1446`
- `risk_on_high->equity_4h` score `-0.4751` n `48` status `ready` deltaP `3.5933` edge `0.0975` maxDD `-6.8836`
- `risk_on_and_context->equity_4h` score `-0.4751` n `48` status `ready` deltaP `3.5933` edge `0.0975` maxDD `-6.8836`
- `market_context_high->fx_1h` score `-0.5084` n `82` status `ready` deltaP `-1.8201` edge `-0.0005` maxDD `-0.537`
- `market_context_high->fx_4h` score `-0.5098` n `81` status `ready` deltaP `-0.9457` edge `0.004` maxDD `-0.7115`
- `market_context_high->crypto_alt_1h` score `-0.5996` n `82` status `ready` deltaP `-0.6864` edge `0.0777` maxDD `-7.3329`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
