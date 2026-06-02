# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T12:07:22.047209+00:00`
- Price records: `672`
- Market context records: `2661`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `market_context_high->unknown_24h` score `8.065` n `117` status `ready` deltaP `17.281` edge `0.5897` maxDD `-1.626`
- `market_context_high->crypto_alt_24h` score `8.022` n `117` status `ready` deltaP `13.929` edge `0.925` maxDD `-19.9486`
- `market_context_high->crypto_alt_4h` score `4.7638` n `121` status `ready` deltaP `23.8019` edge `0.5062` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.2385` n `121` status `ready` deltaP `13.2269` edge `0.3627` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.4558` n `121` status `ready` deltaP `7.3939` edge `0.177` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.9399` n `133` status `ready` deltaP `9.0991` edge `0.1364` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.4565` n `133` status `ready` deltaP `7.449` edge `0.1078` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.2959` n `117` status `ready` deltaP `9.0946` edge `0.0621` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.0871` n `121` status `ready` deltaP `7.4985` edge `0.0269` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1129` n `133` status `ready` deltaP `2.9445` edge `0.0289` maxDD `-1.9684`
- `market_context_high->commodity_1h` score `-0.2877` n `133` status `ready` deltaP `4.132` edge `0.0109` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.3057` n `117` status `ready` deltaP `8.9877` edge `0.0018` maxDD `-0.6418`
- `market_context_high->index_1h` score `-0.3091` n `133` status `ready` deltaP `2.0463` edge `0.01` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.3644` n `121` status `ready` deltaP `4.2242` edge `0.0231` maxDD `-2.5301`
- `market_context_high->metal_1h` score `-0.5548` n `133` status `ready` deltaP `-0.6787` edge `0.0028` maxDD `-1.8854`
- `market_context_high->fx_1h` score `-0.6053` n `133` status `ready` deltaP `-1.4205` edge `0.0034` maxDD `-0.2164`
- `market_context_high->fx_4h` score `-0.6959` n `121` status `ready` deltaP `-0.6778` edge `0.0119` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.0527` n `121` status `ready` deltaP `5.348` edge `0.0214` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.2243` n `133` status `ready` deltaP `-4.3908` edge `0.0111` maxDD `-2.7085`
- `market_context_high->equity_24h` score `-1.5564` n `117` status `ready` deltaP `6.2634` edge `-0.0737` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
