# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T15:22:37.444797+00:00`
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

- `risk_on_high->crypto_alt_24h` score `12.5711` n `67` status `ready` deltaP `33.2712` edge `1.1296` maxDD `-19.6389`
- `risk_on_and_context->crypto_alt_24h` score `12.5711` n `67` status `ready` deltaP `33.2712` edge `1.1296` maxDD `-19.6389`
- `risk_on_high->unknown_4h` score `8.0644` n `107` status `ready` deltaP `24.7935` edge `0.5684` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.0644` n `107` status `ready` deltaP `24.7935` edge `0.5684` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5184` n `159` status `ready` deltaP `21.4901` edge `0.4693` maxDD `-2.5493`
- `market_context_high->crypto_alt_24h` score `4.1256` n `110` status `ready` deltaP `15.9849` edge `0.6562` maxDD `-27.517`
- `risk_on_high->fx_24h` score `2.8621` n `67` status `ready` deltaP `58.4785` edge `0.0421` maxDD `-1.2014`
- `risk_on_and_context->fx_24h` score `2.8621` n `67` status `ready` deltaP `58.4785` edge `0.0421` maxDD `-1.2014`
- `risk_on_high->unknown_1h` score `2.4346` n `107` status `ready` deltaP `6.8149` edge `0.2151` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4346` n `107` status `ready` deltaP `6.8149` edge `0.2151` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.212` n `159` status `ready` deltaP `6.1566` edge `0.2063` maxDD `-2.041`
- `news_risk_high->unknown_1h` score `1.5311` n `61` status `ready` deltaP `3.9192` edge `0.1361` maxDD `-1.1043`
- `market_context_high->metal_24h` score `1.4549` n `110` status `ready` deltaP `26.9444` edge `0.1796` maxDD `-6.1494`
- `market_context_high->fx_24h` score `1.3119` n `110` status `ready` deltaP `34.5707` edge `0.0272` maxDD `-1.8678`
- `risk_on_high->crypto_major_24h` score `1.1596` n `67` status `ready` deltaP `19.2475` edge `0.4877` maxDD `-31.0549`
- `risk_on_and_context->crypto_major_24h` score `1.1596` n `67` status `ready` deltaP `19.2475` edge `0.4877` maxDD `-31.0549`
- `risk_on_high->commodity_24h` score `0.857` n `67` status `ready` deltaP `10.0461` edge `0.1417` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.857` n `67` status `ready` deltaP `10.0461` edge `0.1417` maxDD `-0.5706`
- `risk_on_high->metal_24h` score `0.5929` n `67` status `ready` deltaP `25.6011` edge `0.0622` maxDD `-5.5487`
- `risk_on_and_context->metal_24h` score `0.5929` n `67` status `ready` deltaP `25.6011` edge `0.0622` maxDD `-5.5487`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
