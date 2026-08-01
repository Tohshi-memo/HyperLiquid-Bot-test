# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T10:07:28.400347+00:00`
- Price records: `672`
- Market context records: `8610`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `4856.342` n `63` status `ready` deltaP `34.552` edge `404.5069` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.8104` n `37` status `ready` deltaP `51.2343` edge `1.2657` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `5.8539` n `63` status `ready` deltaP `19.9391` edge `0.4146` maxDD `-3.4427`
- `market_context_high->fx_24h` score `3.2004` n `37` status `ready` deltaP `32.3154` edge `0.0851` maxDD `-0.3737`
- `market_context_high->crypto_major_24h` score `2.7502` n `37` status `ready` deltaP `10.2394` edge `0.5975` maxDD `-20.0534`
- `news_risk_high->index_4h` score `2.3704` n `63` status `ready` deltaP `20.548` edge `0.0796` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7348` n `63` status `ready` deltaP `15.98` edge `0.0857` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.6832` n `62` status `ready` deltaP `12.3705` edge `0.1535` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `1.0936` n `63` status `ready` deltaP `7.6756` edge `0.1666` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.4261` n `63` status `ready` deltaP `11.3721` edge `0.118` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.3723` n `63` status `ready` deltaP `7.2926` edge `0.0518` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3339` n `63` status `ready` deltaP `6.6938` edge `0.0494` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1438` n `63` status `ready` deltaP `6.3041` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0956` n `63` status `ready` deltaP `12.1984` edge `0.0224` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.071` n `63` status `ready` deltaP `3.6313` edge `0.0325` maxDD `-0.8085`
- `market_context_high->metal_24h` score `0.0513` n `37` status `ready` deltaP `3.307` edge `0.0719` maxDD `-1.9898`
- `news_risk_high->index_1h` score `0.0155` n `63` status `ready` deltaP `3.6998` edge `0.009` maxDD `-0.5338`
- `news_risk_high->metal_1h` score `-0.0369` n `63` status `ready` deltaP `4.4483` edge `0.0076` maxDD `-0.5599`
- `market_context_high->index_24h` score `-0.0543` n `37` status `ready` deltaP `14.5722` edge `0.0154` maxDD `-4.5603`
- `market_context_high->fx_4h` score `-0.1441` n `62` status `ready` deltaP `8.2045` edge `0.0129` maxDD `-1.3685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
