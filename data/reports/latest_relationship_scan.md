# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T11:52:29.099464+00:00`
- Price records: `672`
- Market context records: `7874`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14667`

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

- `market_context_high->equity_24h` score `13.0049` n `116` status `ready` deltaP `29.2984` edge `1.0226` maxDD `-6.0681`
- `market_context_high->metal_24h` score `3.286` n `116` status `ready` deltaP `17.6253` edge `0.2818` maxDD `-1.3707`
- `market_context_high->equity_4h` score `2.7759` n `116` status `ready` deltaP `11.9582` edge `0.3744` maxDD `-5.1923`
- `market_context_high->crypto_major_4h` score `1.6622` n `116` status `ready` deltaP `17.3886` edge `0.1944` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `1.648` n `116` status `ready` deltaP `14.6026` edge `0.1517` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `1.4318` n `116` status `ready` deltaP `21.3242` edge `0.1355` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.1744` n `116` status `ready` deltaP `13.0807` edge `0.0506` maxDD `-1.5286`
- `market_context_high->fx_24h` score `1.122` n `116` status `ready` deltaP `30.5556` edge `0.0489` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7698` n `116` status `ready` deltaP `10.8678` edge `0.108` maxDD `-4.2072`
- `market_context_high->crypto_alt_1h` score `0.3686` n `116` status `ready` deltaP `5.095` edge `0.04` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.3329` n `116` status `ready` deltaP `6.8992` edge `0.0411` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.1983` n `116` status `ready` deltaP `7.6862` edge `0.0172` maxDD `-0.7743`
- `market_context_high->index_4h` score `0.0732` n `116` status `ready` deltaP `12.1111` edge `0.0557` maxDD `-1.1645`
- `market_context_high->commodity_1h` score `-0.0331` n `116` status `ready` deltaP `4.5666` edge `0.0127` maxDD `-0.6722`
- `market_context_high->metal_4h` score `-0.1766` n `116` status `ready` deltaP `6.4444` edge `0.091` maxDD `-1.2276`
- `market_context_high->fx_1h` score `-0.3067` n `116` status `ready` deltaP `1.952` edge `-0.0001` maxDD `-0.4112`
- `market_context_high->index_24h` score `-0.8048` n `116` status `ready` deltaP `-1.8379` edge `0.1096` maxDD `-1.8201`
- `market_context_high->metal_1h` score `-0.8201` n `116` status `ready` deltaP `0.1445` edge `0.0227` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.0613` n `116` status `ready` deltaP `-1.1283` edge `0.0001` maxDD `-1.6246`
- `market_context_high->crypto_alt_24h` score `-1.5743` n `116` status `ready` deltaP `13.4091` edge `0.2383` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
