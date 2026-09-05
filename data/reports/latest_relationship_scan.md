# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T12:22:26.999173+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11019`

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

- `risk_on_high->unknown_4h` score `22.8863` n `140` status `ready` deltaP `7.0688` edge `1.9219` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.8863` n `140` status `ready` deltaP `7.0688` edge `1.9219` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `10.8414` n `228` status `ready` deltaP `6.956` edge `0.9301` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.5503` n `37` status `ready` deltaP `25.1783` edge `0.4883` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9969` n `37` status `ready` deltaP `21.7014` edge `0.1884` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.639` n `37` status `ready` deltaP `17.1803` edge `0.23` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.2444` n `37` status `ready` deltaP `22.6269` edge `0.0583` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.9812` n `37` status `ready` deltaP `12.3435` edge `0.1029` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5835` n `37` status `ready` deltaP `13.0847` edge `0.0838` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.1963` n `37` status `ready` deltaP `14.2661` edge `0.0239` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.1823` n `37` status `ready` deltaP `6.1661` edge `0.0757` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1503` n `37` status `ready` deltaP `14.4239` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_24h` score `1.0342` n `37` status `ready` deltaP `16.5776` edge `0.2997` maxDD `-18.2098`
- `news_risk_high->crypto_alt_1h` score `0.9093` n `37` status `ready` deltaP `8.8769` edge `0.0431` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.6131` n `37` status `ready` deltaP `6.3983` edge `0.0413` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.4874` n `37` status `ready` deltaP `14.9211` edge `0.0427` maxDD `-3.1244`
- `risk_on_high->crypto_major_24h` score `0.3233` n `122` status `ready` deltaP `21.0525` edge `0.7755` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.3233` n `122` status `ready` deltaP `21.0525` edge `0.7755` maxDD `-56.9519`
- `market_context_high->equity_24h` score `0.2009` n `192` status `ready` deltaP `15.7986` edge `0.355` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.1091` n `152` status `ready` deltaP `12.5591` edge `0.0015` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
