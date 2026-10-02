# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T10:52:34.511828+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4842`

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

- `market_context_high->unknown_1h` score `341.1022` n `50` status `ready` deltaP `10.4251` edge `28.3606` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `289.0943` n `50` status `ready` deltaP `10.2134` edge `24.0231` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5514` n `73` status `ready` deltaP `39.795` edge `1.0516` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `10.3789` n `73` status `ready` deltaP `35.878` edge `0.6742` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `10.3769` n `50` status `ready` deltaP `35.125` edge `0.7722` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0477` n `50` status `ready` deltaP `16.5347` edge `0.8147` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9213` n `50` status `ready` deltaP `17.2378` edge `0.5322` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.8791` n `50` status `ready` deltaP `15.122` edge `0.4351` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.448` n `104` status `ready` deltaP `18.1989` edge `0.3837` maxDD `-6.4152`
- `market_context_high->crypto_alt_1h` score `3.0272` n `50` status `ready` deltaP `14.503` edge `0.2219` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.964` n `50` status `ready` deltaP `14.2994` edge `0.1967` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9419` n `50` status `ready` deltaP `32.8415` edge `0.0397` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.5967` n `104` status `ready` deltaP `24.0736` edge `0.1255` maxDD `-2.9013`
- `market_context_high->equity_24h` score `2.5728` n `50` status `ready` deltaP `12.0972` edge `0.4354` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `2.4098` n `73` status `ready` deltaP `9.2894` edge `0.5624` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.452` n `50` status `ready` deltaP `20.3413` edge `0.0118` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2871` n `73` status `ready` deltaP `12.6618` edge `0.208` maxDD `-2.192`
- `market_context_high->index_24h` score `0.9321` n `50` status `ready` deltaP `15.3125` edge `0.0745` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.9007` n `114` status `ready` deltaP `5.5205` edge `0.0945` maxDD `-2.4998`
- `news_risk_high->crypto_major_4h` score `0.8805` n `104` status `ready` deltaP `11.7378` edge `0.2656` maxDD `-10.477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
