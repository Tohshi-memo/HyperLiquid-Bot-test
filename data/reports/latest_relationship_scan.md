# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T02:07:27.274270+00:00`
- Price records: `672`
- Market context records: `5834`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10076`

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

- `market_context_high->equity_4h` score `0.6029` n `269` status `ready` deltaP `7.5783` edge `0.1455` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.2964` n `269` status `ready` deltaP `1.5955` edge `-0.0001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.4289` n `269` status `ready` deltaP `4.1477` edge `0.0373` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.5191` n `269` status `ready` deltaP `-0.6873` edge `-0.0017` maxDD `-2.1545`
- `market_context_high->equity_24h` score `-0.5362` n `241` status `ready` deltaP `15.5414` edge `0.3596` maxDD `-31.6316`
- `market_context_high->index_1h` score `-0.5586` n `269` status `ready` deltaP `1.2087` edge `0.0051` maxDD `-0.7819`
- `market_context_high->metal_1h` score `-0.6202` n `269` status `ready` deltaP `2.2516` edge `0.0004` maxDD `-2.0339`
- `market_context_high->crypto_major_1h` score `-0.9817` n `269` status `ready` deltaP `2.6234` edge `0.0328` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1349` n `269` status `ready` deltaP `1.1364` edge `0.0313` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1721` n `269` status `ready` deltaP `0.6086` edge `0.0144` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.614` n `241` status `ready` deltaP `7.9313` edge `0.022` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.6222` n `269` status `ready` deltaP `-1.7958` edge `-0.0011` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.2039` n `269` status `ready` deltaP `-5.12` edge `-0.0453` maxDD `-8.9164`
- `market_context_high->commodity_4h` score `-2.5383` n `269` status `ready` deltaP `-0.7344` edge `-0.0143` maxDD `-8.0531`
- `market_context_high->index_24h` score `-2.8918` n `241` status `ready` deltaP `2.9125` edge `0.0243` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.1279` n `269` status `ready` deltaP `6.2517` edge `0.1349` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.8765` n `269` status `ready` deltaP `3.8206` edge `0.069` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-5.5416` n `241` status `ready` deltaP `-0.4848` edge `-0.2108` maxDD `-10.8216`
- `market_context_high->commodity_24h` score `-5.6853` n `241` status `ready` deltaP `-11.2545` edge `-0.0579` maxDD `-30.3426`
- `market_context_high->crypto_alt_24h` score `-12.7613` n `241` status `ready` deltaP `-11.6363` edge `-0.5278` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
