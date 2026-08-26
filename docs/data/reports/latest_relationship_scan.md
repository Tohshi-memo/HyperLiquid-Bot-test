# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T19:17:01.440712+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `48.0401` n `50` status `ready` deltaP `11.5717` edge `3.9262` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.4601` n `50` status `ready` deltaP `26.8767` edge `0.8691` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `11.893` n `50` status `ready` deltaP `35.5509` edge `0.7982` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.8523` n `50` status `ready` deltaP `34.0864` edge `0.5202` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.1082` n `50` status `ready` deltaP `40.8497` edge `0.0852` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.4761` n `50` status `ready` deltaP `41.0107` edge `0.0253` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.3203` n `137` status `ready` deltaP `25.5774` edge `0.147` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.6695` n `50` status `ready` deltaP `15.479` edge `0.1548` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.18` n `50` status `ready` deltaP `32.3696` edge `-0.0299` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.5173` n `50` status `ready` deltaP `19.379` edge `0.0743` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.3479` n `50` status `ready` deltaP `18.4072` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.3006` n `137` status `ready` deltaP `12.8513` edge `0.0676` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `1.2831` n `50` status `ready` deltaP `16.8144` edge `0.0229` maxDD `-0.2455`
- `news_risk_high->commodity_1h` score `0.5004` n `50` status `ready` deltaP `14.0` edge `0.0021` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1116` n `50` status `ready` deltaP `6.9102` edge `0.0022` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.1037` n `50` status `ready` deltaP `6.4018` edge `0.0057` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.0781` n `50` status `ready` deltaP `5.1018` edge `-0.0014` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0408` n `50` status `ready` deltaP `8.1613` edge `-0.0047` maxDD `-0.249`
- `market_context_high->unknown_24h` score `-0.3754` n `133` status `ready` deltaP `5.5567` edge `0.0044` maxDD `-3.1513`
- `market_context_high->fx_1h` score `-0.4029` n `137` status `ready` deltaP `3.3415` edge `-0.0007` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
