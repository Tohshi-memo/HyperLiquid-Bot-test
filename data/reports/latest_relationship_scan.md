# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T19:52:29.244522+00:00`
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

- `risk_on_high->unknown_4h` score `7.8586` n `107` status `ready` deltaP `23.7264` edge `0.5584` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.8586` n `107` status `ready` deltaP `23.7264` edge `0.5584` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.3114` n `159` status `ready` deltaP `20.423` edge `0.4592` maxDD `-2.5526`
- `risk_on_high->unknown_1h` score `2.4043` n `107` status `ready` deltaP `6.5155` edge `0.2146` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.4043` n `107` status `ready` deltaP `6.5155` edge `0.2146` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `2.1804` n `159` status `ready` deltaP `5.8572` edge `0.2057` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `2.0412` n `85` status `ready` deltaP `13.8745` edge `0.1764` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `2.0412` n `85` status `ready` deltaP `13.8745` edge `0.1764` maxDD `-0.5706`
- `risk_on_high->crypto_alt_24h` score `1.5267` n `85` status `ready` deltaP `16.5196` edge `0.7255` maxDD `-40.5249`
- `risk_on_and_context->crypto_alt_24h` score `1.5267` n `85` status `ready` deltaP `16.5196` edge `0.7255` maxDD `-40.5249`
- `news_risk_high->unknown_1h` score `1.4986` n `61` status `ready` deltaP `3.6198` edge `0.1354` maxDD `-1.1049`
- `risk_on_high->fx_24h` score `1.2425` n `85` status `ready` deltaP `44.2198` edge `0.026` maxDD `-2.9199`
- `risk_on_and_context->fx_24h` score `1.2425` n `85` status `ready` deltaP `44.2198` edge `0.026` maxDD `-2.9199`
- `market_context_high->fx_24h` score `0.4632` n `128` status `ready` deltaP `29.5139` edge `0.02` maxDD `-3.5863`
- `news_risk_high->commodity_4h` score `0.2384` n `61` status `ready` deltaP `7.1871` edge `0.0243` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.2354` n `159` status `ready` deltaP `9.9292` edge `0.0184` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1585` n `61` status `ready` deltaP `10.8057` edge `0.0005` maxDD `-0.7461`
- `risk_on_high->commodity_1h` score `0.038` n `107` status `ready` deltaP `6.2203` edge `0.0156` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `0.038` n `107` status `ready` deltaP `6.2203` edge `0.0156` maxDD `-0.8428`
- `market_context_high->commodity_4h` score `-0.0016` n `159` status `ready` deltaP `6.6613` edge `0.0452` maxDD `-2.1795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
