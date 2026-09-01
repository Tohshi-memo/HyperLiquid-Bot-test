# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T00:07:23.773630+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.666` n `107` status `ready` deltaP `23.2691` edge `0.5454` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.666` n `107` status `ready` deltaP `23.2691` edge `0.5454` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.1188` n `159` status `ready` deltaP `19.9657` edge `0.4462` maxDD `-2.5526`
- `risk_on_high->unknown_1h` score `2.0841` n `107` status `ready` deltaP `5.0185` edge `0.1979` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.0841` n `107` status `ready` deltaP `5.0185` edge `0.1979` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `1.8603` n `159` status `ready` deltaP `4.3602` edge `0.189` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `1.6625` n `94` status `ready` deltaP `13.4013` edge `0.148` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.6625` n `94` status `ready` deltaP `13.4013` edge `0.148` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.1785` n `61` status `ready` deltaP `2.1228` edge `0.1187` maxDD `-1.1049`
- `risk_on_high->fx_24h` score `0.6828` n `94` status `ready` deltaP `40.9759` edge `0.0235` maxDD `-3.7307`
- `risk_on_and_context->fx_24h` score `0.6828` n `94` status `ready` deltaP `40.9759` edge `0.0235` maxDD `-3.7307`
- `risk_on_high->crypto_alt_24h` score `0.414` n `94` status `ready` deltaP `12.3523` edge `0.6611` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.414` n `94` status `ready` deltaP `12.3523` edge `0.6611` maxDD `-42.8959`
- `news_risk_high->commodity_4h` score `0.1799` n `61` status `ready` deltaP `6.2725` edge `0.0229` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.1743` n `159` status `ready` deltaP `9.3304` edge `0.0173` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1487` n `61` status `ready` deltaP `10.6533` edge `0.0007` maxDD `-0.7461`
- `risk_on_high->commodity_1h` score `-0.0018` n `107` status `ready` deltaP `5.6215` edge `0.0145` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0018` n `107` status `ready` deltaP `5.6215` edge `0.0145` maxDD `-0.8428`
- `risk_on_high->index_1h` score `-0.0462` n `107` status `ready` deltaP `5.8481` edge `-0.0004` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0462` n `107` status `ready` deltaP `5.8481` edge `-0.0004` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
