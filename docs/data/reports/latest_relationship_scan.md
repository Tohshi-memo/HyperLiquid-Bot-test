# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T01:37:27.178512+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `29.3548` n `75` status `ready` deltaP `-39.7222` edge `4.2966` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `4.3474` n `75` status `ready` deltaP `34.1806` edge `0.1693` maxDD `-0.4576`
- `market_context_high->commodity_4h` score `0.9783` n `105` status `ready` deltaP `11.5607` edge `0.0516` maxDD `-0.7718`
- `market_context_high->index_24h` score `0.8546` n `75` status `ready` deltaP `17.0625` edge `-0.0294` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `0.0929` n `75` status `ready` deltaP `-0.4931` edge `0.1974` maxDD `-9.2432`
- `market_context_high->metal_4h` score `-0.1532` n `105` status `ready` deltaP `16.6275` edge `0.0171` maxDD `-4.5909`
- `market_context_high->metal_1h` score `-0.3371` n `110` status `ready` deltaP `5.7866` edge `0.0049` maxDD `-1.7257`
- `market_context_high->fx_4h` score `-0.5632` n `105` status `ready` deltaP `-0.935` edge `-0.0055` maxDD `-0.504`
- `market_context_high->commodity_1h` score `-0.5695` n `110` status `ready` deltaP `-1.7964` edge `0.0091` maxDD `-0.8998`
- `market_context_high->fx_1h` score `-0.7011` n `110` status `ready` deltaP `-2.877` edge `-0.0022` maxDD `-0.2968`
- `market_context_high->index_1h` score `-0.7354` n `110` status `ready` deltaP `-5.988` edge `-0.0022` maxDD `-0.5064`
- `market_context_high->crypto_major_4h` score `-1.3875` n `105` status `ready` deltaP `1.8859` edge `-0.0074` maxDD `-4.6638`
- `market_context_high->equity_24h` score `-1.7802` n `75` status `ready` deltaP `10.5625` edge `-0.0845` maxDD `-7.7412`
- `market_context_high->index_4h` score `-1.9078` n `105` status `ready` deltaP `-10.919` edge `-0.0053` maxDD `-0.8045`
- `market_context_high->crypto_major_1h` score `-2.0613` n `110` status `ready` deltaP `-6.5133` edge `-0.0273` maxDD `-4.0845`
- `market_context_high->crypto_alt_1h` score `-2.0704` n `110` status `ready` deltaP `-6.663` edge `-0.0229` maxDD `-4.7507`
- `market_context_high->equity_1h` score `-2.1783` n `110` status `ready` deltaP `-8.5329` edge `-0.0379` maxDD `-3.606`
- `market_context_high->fx_24h` score `-2.8716` n `75` status `ready` deltaP `-26.0417` edge `-0.0338` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-2.9099` n `75` status `ready` deltaP `-18.3264` edge `0.0003` maxDD `-7.0954`
- `market_context_high->equity_4h` score `-5.6643` n `105` status `ready` deltaP `-20.0625` edge `-0.1517` maxDD `-8.5929`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
