# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T15:37:31.522541+00:00`
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

- `risk_on_high->unknown_4h` score `8.0608` n `107` status `ready` deltaP `24.7935` edge `0.5681` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.0608` n `107` status `ready` deltaP `24.7935` edge `0.5681` maxDD `-2.266`
- `risk_on_high->crypto_alt_24h` score `7.7455` n `68` status `ready` deltaP `32.1079` edge `1.1012` maxDD `-20.7791`
- `risk_on_and_context->crypto_alt_24h` score `7.7455` n `68` status `ready` deltaP `32.1079` edge `1.1012` maxDD `-20.7791`
- `market_context_high->unknown_4h` score `6.5148` n `159` status `ready` deltaP `21.4901` edge `0.469` maxDD `-2.5493`
- `market_context_high->crypto_alt_24h` score `3.9215` n `111` status `ready` deltaP `15.428` edge `0.6429` maxDD `-27.517`
- `risk_on_high->fx_24h` score `2.7622` n `68` status `ready` deltaP `57.4449` edge `0.0412` maxDD `-1.2693`
- `risk_on_and_context->fx_24h` score `2.7622` n `68` status `ready` deltaP `57.4449` edge `0.0412` maxDD `-1.2693`
- `risk_on_high->unknown_1h` score `2.4346` n `107` status `ready` deltaP `6.8149` edge `0.2151` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4346` n `107` status `ready` deltaP `6.8149` edge `0.2151` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.212` n `159` status `ready` deltaP `6.1566` edge `0.2063` maxDD `-2.041`
- `news_risk_high->unknown_1h` score `1.5311` n `61` status `ready` deltaP `3.9192` edge `0.1361` maxDD `-1.1043`
- `market_context_high->metal_24h` score `1.2953` n `111` status `ready` deltaP `26.3138` edge `0.1741` maxDD `-6.6766`
- `market_context_high->fx_24h` score `1.2689` n `111` status `ready` deltaP `34.2202` edge `0.0268` maxDD `-1.9356`
- `risk_on_high->commodity_24h` score `0.8973` n `68` status `ready` deltaP `10.3554` edge `0.1448` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8973` n `68` status `ready` deltaP `10.3554` edge `0.1448` maxDD `-0.5706`
- `risk_on_high->crypto_major_24h` score `0.7492` n `68` status `ready` deltaP `18.2598` edge `0.4641` maxDD `-32.5163`
- `risk_on_and_context->crypto_major_24h` score `0.7492` n `68` status `ready` deltaP `18.2598` edge `0.4641` maxDD `-32.5163`
- `news_risk_high->commodity_24h` score `0.4068` n `44` status `ready` deltaP `6.3447` edge `0.0414` maxDD `-1.1904`
- `risk_on_high->metal_24h` score `0.3996` n `68` status `ready` deltaP `24.5915` edge `0.0549` maxDD `-6.0759`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
