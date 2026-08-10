# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T22:52:31.416037+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `1.0581` n `145` status `ready` deltaP `20.4064` edge `0.0329` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.8061` n `176` status `ready` deltaP `11.225` edge `0.0638` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6152` n `180` status `ready` deltaP `8.4997` edge `0.0289` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.0478` n `176` status `ready` deltaP `7.3032` edge `0.0073` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.0942` n `180` status `ready` deltaP `4.9335` edge `0.0002` maxDD `-0.613`
- `market_context_high->index_1h` score `-0.7386` n `180` status `ready` deltaP `-6.2641` edge `-0.0046` maxDD `-0.8666`
- `market_context_high->index_24h` score `-0.8785` n `145` status `ready` deltaP `-2.9116` edge `0.0607` maxDD `-5.9796`
- `market_context_high->index_4h` score `-1.0513` n `176` status `ready` deltaP `-5.7927` edge `-0.0155` maxDD `-1.4536`
- `market_context_high->metal_24h` score `-1.1874` n `145` status `ready` deltaP `2.5482` edge `0.0165` maxDD `-2.9283`
- `market_context_high->equity_1h` score `-1.1876` n `180` status `ready` deltaP `-4.837` edge `-0.0148` maxDD `-6.0833`
- `market_context_high->metal_1h` score `-1.2215` n `180` status `ready` deltaP `-4.4078` edge `-0.0088` maxDD `-2.0884`
- `market_context_high->crypto_alt_1h` score `-2.8571` n `180` status `ready` deltaP `-11.1377` edge `-0.0441` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-3.0756` n `176` status `ready` deltaP `-6.7212` edge `-0.0351` maxDD `-6.1111`
- `market_context_high->equity_24h` score `-3.7034` n `145` status `ready` deltaP `-2.7562` edge `0.0852` maxDD `-32.9959`
- `market_context_high->crypto_major_1h` score `-3.8096` n `180` status `ready` deltaP `-10.642` edge `-0.0561` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.1273` n `176` status `ready` deltaP `-14.9251` edge `-0.1348` maxDD `-14.5876`
- `market_context_high->crypto_major_24h` score `-4.4382` n `145` status `ready` deltaP `-5.4969` edge `-0.1203` maxDD `-24.9639`
- `market_context_high->commodity_24h` score `-5.9491` n `145` status `ready` deltaP `0.5474` edge `-0.0639` maxDD `-42.1959`
- `market_context_high->crypto_alt_4h` score `-6.9625` n `176` status `ready` deltaP `-14.9667` edge `-0.1554` maxDD `-19.3356`
- `market_context_high->crypto_alt_24h` score `-7.6183` n `145` status `ready` deltaP `-12.8226` edge `-0.2102` maxDD `-20.8005`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
