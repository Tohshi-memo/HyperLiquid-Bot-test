# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T22:07:24.477701+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10805`

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

- `risk_on_high->unknown_4h` score `20.8284` n `133` status `ready` deltaP `-2.1066` edge `1.9503` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `20.8284` n `133` status `ready` deltaP `-2.1066` edge `1.9503` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.2478` n `228` status `ready` deltaP `2.0913` edge `0.9202` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `6.5039` n `37` status `ready` deltaP `25.1783` edge `0.4011` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8815` n `37` status `ready` deltaP `20.1389` edge `0.1892` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2249` n `37` status `ready` deltaP `16.1132` edge `0.2026` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3259` n `37` status `ready` deltaP `23.5416` edge `0.059` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6039` n `37` status `ready` deltaP `13.2344` edge `0.0845` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5904` n `37` status `ready` deltaP `7.9227` edge `0.0998` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.2957` n `37` status `ready` deltaP `15.4637` edge `0.0242` maxDD `-0.2118`
- `market_context_high->equity_24h` score `1.1703` n `160` status `ready` deltaP `12.9167` edge `0.4403` maxDD `-20.6443`
- `news_risk_high->index_1h` score `1.1503` n `37` status `ready` deltaP `14.4239` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.0971` n `37` status `ready` deltaP `5.717` edge `0.0716` maxDD `-0.4628`
- `news_risk_high->fx_24h` score `0.9051` n `37` status `ready` deltaP `19.7822` edge `0.0451` maxDD `-3.1244`
- `news_risk_high->crypto_alt_1h` score `0.8314` n `37` status `ready` deltaP `8.2781` edge `0.0406` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.3247` n `37` status `ready` deltaP `16.0567` edge `0.2122` maxDD `-18.2098`
- `news_risk_high->crypto_alt_4h` score `0.2247` n `37` status `ready` deltaP `3.9593` edge `0.0252` maxDD `-1.296`
- `risk_on_high->index_1h` score `-0.0499` n `145` status `ready` deltaP `6.1666` edge `-0.0028` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0499` n `145` status `ready` deltaP `6.1666` edge `-0.0028` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0519` n `37` status `ready` deltaP `5.276` edge `0.0028` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
