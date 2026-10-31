# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T07:52:28.235038+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7667`

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

- `market_context_high->unknown_24h` score `1673.3063` n `131` status `ready` deltaP `-5.1646` edge `139.5196` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `112.179` n `98` status `ready` deltaP `-5.493` edge `9.4135` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `33.865` n `131` status `ready` deltaP `2.126` edge `2.8212` maxDD `-0.3966`
- `market_context_high->equity_24h` score `8.6657` n `131` status `ready` deltaP `21.7889` edge `0.8526` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `6.4338` n `94` status `ready` deltaP `21.7209` edge `0.4838` maxDD `-5.0629`
- `market_context_high->index_24h` score `4.2406` n `131` status `ready` deltaP `40.3189` edge `0.1029` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.9236` n `98` status `ready` deltaP `8.2457` edge `0.1049` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.5099` n `131` status `ready` deltaP `11.9372` edge `0.015` maxDD `-0.3371`
- `market_context_high->metal_4h` score `0.352` n `131` status `ready` deltaP `15.1822` edge `0.0321` maxDD `-1.7215`
- `market_context_high->commodity_4h` score `0.3423` n `131` status `ready` deltaP `14.1163` edge `0.0563` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.2655` n `131` status `ready` deltaP `4.6476` edge `0.0787` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.1256` n `131` status `ready` deltaP `8.0153` edge `0.0598` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0421` n `131` status `ready` deltaP `1.9107` edge `0.1403` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0743` n `131` status `ready` deltaP `4.0785` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.1994` n `131` status `ready` deltaP `2.9266` edge `0.0153` maxDD `-0.4475`
- `market_context_high->metal_24h` score `-0.4493` n `131` status `ready` deltaP `4.934` edge `0.1742` maxDD `-10.5088`
- `market_context_high->fx_4h` score `-0.4829` n `131` status `ready` deltaP `0.0768` edge `-0.0027` maxDD `-0.4445`
- `market_context_high->index_1h` score `-0.6743` n `131` status `ready` deltaP `-0.2023` edge `0.001` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8636` n `131` status `ready` deltaP `2.762` edge `0.0484` maxDD `-7.536`
- `news_risk_high->index_1h` score `-0.8682` n `98` status `ready` deltaP `1.7139` edge `-0.0038` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
