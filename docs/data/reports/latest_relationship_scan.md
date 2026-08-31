# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T18:22:32.113219+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `risk_on_high->unknown_4h` score `7.8766` n `107` status `ready` deltaP `23.7264` edge `0.5599` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.8766` n `107` status `ready` deltaP `23.7264` edge `0.5599` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.3293` n `159` status `ready` deltaP `20.423` edge `0.4607` maxDD `-2.5526`
- `risk_on_high->crypto_alt_24h` score `3.3594` n `79` status `ready` deltaP `21.2553` edge `0.825` maxDD `-34.2138`
- `risk_on_and_context->crypto_alt_24h` score `3.3594` n `79` status `ready` deltaP `21.2553` edge `0.825` maxDD `-34.2138`
- `risk_on_high->unknown_1h` score `2.517` n `107` status `ready` deltaP `7.264` edge `0.219` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.517` n `107` status `ready` deltaP `7.264` edge `0.219` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `2.2931` n `159` status `ready` deltaP `6.6057` edge `0.2101` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `1.9133` n `79` status `ready` deltaP `12.9505` edge `0.1719` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.9133` n `79` status `ready` deltaP `12.9505` edge `0.1719` maxDD `-0.5706`
- `risk_on_high->fx_24h` score `1.7241` n `79` status `ready` deltaP `48.0925` edge `0.03` maxDD `-2.3663`
- `risk_on_and_context->fx_24h` score `1.7241` n `79` status `ready` deltaP `48.0925` edge `0.03` maxDD `-2.3663`
- `news_risk_high->unknown_1h` score `1.6113` n `61` status `ready` deltaP `4.3683` edge `0.1398` maxDD `-1.1049`
- `market_context_high->fx_24h` score `0.7812` n `122` status `ready` deltaP `30.9312` edge `0.0218` maxDD `-3.0327`
- `news_risk_high->commodity_4h` score `0.2961` n `61` status `ready` deltaP `8.1018` edge `0.0256` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.221` n `159` status `ready` deltaP `9.7795` edge `0.0182` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1585` n `61` status `ready` deltaP `10.8057` edge `0.0005` maxDD `-0.7461`
- `news_risk_high->commodity_24h` score `0.1273` n `44` status `ready` deltaP `4.435` edge `0.0183` maxDD `-1.1904`
- `market_context_high->commodity_4h` score `0.0872` n `159` status `ready` deltaP `7.576` edge `0.0465` maxDD `-2.1795`
- `risk_on_high->commodity_1h` score `0.0286` n `107` status `ready` deltaP `6.0706` edge `0.0154` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
