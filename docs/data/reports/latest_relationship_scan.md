# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T17:37:31.484229+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `risk_on_high->unknown_4h` score `7.96` n `107` status `ready` deltaP `24.1837` edge `0.5638` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.96` n `107` status `ready` deltaP `24.1837` edge `0.5638` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.4127` n `159` status `ready` deltaP `20.8803` edge `0.4646` maxDD `-2.5526`
- `risk_on_high->crypto_alt_24h` score `4.2992` n `76` status `ready` deltaP `23.9035` edge `0.8803` maxDD `-31.412`
- `risk_on_and_context->crypto_alt_24h` score `4.2992` n `76` status `ready` deltaP `23.9035` edge `0.8803` maxDD `-31.412`
- `risk_on_high->unknown_1h` score `2.5361` n `107` status `ready` deltaP `7.4137` edge `0.2196` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.5361` n `107` status `ready` deltaP `7.4137` edge `0.2196` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `2.3123` n `159` status `ready` deltaP `6.7554` edge `0.2107` maxDD `-2.0436`
- `risk_on_high->fx_24h` score `1.9852` n `76` status `ready` deltaP `50.3198` edge `0.0325` maxDD `-2.076`
- `risk_on_and_context->fx_24h` score `1.9852` n `76` status `ready` deltaP `50.3198` edge `0.0325` maxDD `-2.076`
- `risk_on_high->commodity_24h` score `1.8034` n `76` status `ready` deltaP `12.372` edge `0.1666` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.8034` n `76` status `ready` deltaP `12.372` edge `0.1666` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.6305` n `61` status `ready` deltaP `4.518` edge `0.1404` maxDD `-1.1049`
- `market_context_high->crypto_alt_24h` score `1.0084` n `119` status `ready` deltaP `11.3096` edge `0.5313` maxDD `-33.4801`
- `market_context_high->fx_24h` score `0.9009` n `119` status `ready` deltaP `31.7329` edge `0.0228` maxDD `-2.7423`
- `news_risk_high->commodity_4h` score `0.3071` n `61` status `ready` deltaP `8.2542` edge `0.026` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.2091` n `159` status `ready` deltaP `9.6298` edge `0.0182` maxDD `-1.5315`
- `news_risk_high->commodity_24h` score `0.2004` n `44` status `ready` deltaP `4.9558` edge `0.0242` maxDD `-1.1904`
- `news_risk_high->fx_4h` score `0.1963` n `61` status `ready` deltaP `11.263` edge `0.0006` maxDD `-0.7461`
- `market_context_high->commodity_4h` score `0.1041` n `159` status `ready` deltaP `7.7284` edge `0.0469` maxDD `-2.1795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
