# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T15:52:26.891002+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11688`

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

- `risk_on_high->unknown_4h` score `8.045` n `107` status `ready` deltaP `24.641` edge `0.5678` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.045` n `107` status `ready` deltaP `24.641` edge `0.5678` maxDD `-2.266`
- `risk_on_high->crypto_alt_24h` score `7.3832` n `69` status `ready` deltaP `30.9783` edge `1.0775` maxDD `-21.6638`
- `risk_on_and_context->crypto_alt_24h` score `7.3832` n `69` status `ready` deltaP `30.9783` edge `1.0775` maxDD `-21.6638`
- `market_context_high->unknown_4h` score `6.499` n `159` status `ready` deltaP `21.3376` edge `0.4687` maxDD `-2.5493`
- `market_context_high->crypto_alt_24h` score `3.7505` n `112` status `ready` deltaP `14.881` edge `0.6323` maxDD `-27.517`
- `risk_on_high->fx_24h` score `2.6622` n `69` status `ready` deltaP `56.4462` edge `0.0402` maxDD `-1.3489`
- `risk_on_and_context->fx_24h` score `2.6622` n `69` status `ready` deltaP `56.4462` edge `0.0402` maxDD `-1.3489`
- `risk_on_high->unknown_1h` score `2.4358` n `107` status `ready` deltaP `6.8149` edge `0.2152` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4358` n `107` status `ready` deltaP `6.8149` edge `0.2152` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.2132` n `159` status `ready` deltaP `6.1566` edge `0.2064` maxDD `-2.041`
- `news_risk_high->unknown_1h` score `1.5323` n `61` status `ready` deltaP `3.9192` edge `0.1362` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.2248` n `112` status `ready` deltaP `33.879` edge `0.0264` maxDD `-2.0153`
- `market_context_high->metal_24h` score `1.1348` n `112` status `ready` deltaP `25.6944` edge `0.1687` maxDD `-7.2277`
- `risk_on_high->commodity_24h` score `0.936` n `69` status `ready` deltaP `10.6506` edge `0.1478` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.936` n `69` status `ready` deltaP `10.6506` edge `0.1478` maxDD `-0.5706`
- `risk_on_high->crypto_major_24h` score `0.3969` n `69` status `ready` deltaP `17.3007` edge `0.4451` maxDD `-33.7642`
- `risk_on_and_context->crypto_major_24h` score `0.3969` n `69` status `ready` deltaP `17.3007` edge `0.4451` maxDD `-33.7642`
- `news_risk_high->commodity_24h` score `0.3798` n `44` status `ready` deltaP `6.1711` edge `0.0391` maxDD `-1.1904`
- `news_risk_high->commodity_4h` score `0.3228` n `61` status `ready` deltaP `8.4066` edge `0.027` maxDD `-1.3325`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
