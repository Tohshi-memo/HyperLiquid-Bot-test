# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T23:52:38.029662+00:00`
- Price records: `672`
- Market context records: `4038`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10624`

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

- `risk_on_high->unknown_4h` score `145.6931` n `40` status `ready` deltaP `-7.2866` edge `12.3713` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.6931` n `40` status `ready` deltaP `-7.2866` edge `12.3713` maxDD `-10.864`
- `market_context_high->unknown_24h` score `46.7086` n `134` status `ready` deltaP `-7.2389` edge `4.3435` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `23.2886` n `155` status `ready` deltaP `2.3102` edge `2.4676` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `4.7366` n `40` status `ready` deltaP `35.7019` edge `0.1567` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.7366` n `40` status `ready` deltaP `35.7019` edge `0.1567` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.2671` n `40` status `ready` deltaP `36.372` edge `0.0345` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.2671` n `40` status `ready` deltaP `36.372` edge `0.0345` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.6376` n `134` status `ready` deltaP `22.6506` edge `0.09` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.6202` n `155` status `ready` deltaP `15.6462` edge `0.1588` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.4223` n `134` status `ready` deltaP `10.8345` edge `0.145` maxDD `-4.8962`
- `market_context_high->equity_1h` score `1.1131` n `159` status `ready` deltaP `8.0434` edge `0.0951` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.9113` n `40` status `ready` deltaP `18.689` edge `0.0179` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9113` n `40` status `ready` deltaP `18.689` edge `0.0179` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.4843` n `40` status `ready` deltaP `2.2964` edge `0.2532` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.4843` n `40` status `ready` deltaP `2.2964` edge `0.2532` maxDD `-12.9187`
- `market_context_high->metal_1h` score `0.4214` n `159` status `ready` deltaP `10.3171` edge `0.0478` maxDD `-3.0049`
- `risk_on_high->equity_1h` score `0.3884` n `40` status `ready` deltaP `10.7635` edge `-0.0003` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.3884` n `40` status `ready` deltaP `10.7635` edge `-0.0003` maxDD `-0.7937`
- `market_context_high->crypto_major_1h` score `0.2766` n `159` status `ready` deltaP `7.0237` edge `0.0484` maxDD `-3.7739`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
