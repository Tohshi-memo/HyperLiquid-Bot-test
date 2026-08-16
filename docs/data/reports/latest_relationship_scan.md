# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T16:52:25.039653+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11814`

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

- `market_context_high->unknown_24h` score `219.7582` n `88` status `ready` deltaP `-21.512` edge `28.5859` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.8721` n `88` status `ready` deltaP `41.3037` edge `0.3864` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.4402` n `125` status `ready` deltaP `14.0744` edge `0.0733` maxDD `-0.7687`
- `market_context_high->fx_1h` score `-0.1168` n `125` status `ready` deltaP `1.7521` edge `0.0015` maxDD `-0.2527`
- `market_context_high->commodity_1h` score `-0.119` n `125` status `ready` deltaP `1.7569` edge `0.0195` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.3024` n `125` status `ready` deltaP `4.3598` edge `0.0062` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.5027` n `125` status `ready` deltaP `1.9533` edge `-0.0059` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.7695` n `125` status `ready` deltaP `-6.5377` edge `-0.0029` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.8808` n `125` status `ready` deltaP `8.5902` edge `-0.0128` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.3877` n `88` status `ready` deltaP `-7.1497` edge `0.0305` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.672` n `125` status `ready` deltaP `-9.7329` edge `-0.0455` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.8625` n `88` status `ready` deltaP `-8.7437` edge `0.0707` maxDD `-7.0954`
- `market_context_high->crypto_alt_1h` score `-1.9124` n `125` status `ready` deltaP `-1.097` edge `-0.0181` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-1.9857` n `125` status `ready` deltaP `-4.5497` edge `-0.0298` maxDD `-5.4277`
- `market_context_high->index_4h` score `-2.085` n `125` status `ready` deltaP `-12.4805` edge `-0.0093` maxDD `-0.8328`
- `market_context_high->index_24h` score `-2.0937` n `88` status `ready` deltaP `-6.7551` edge `-0.0694` maxDD `-2.3194`
- `market_context_high->crypto_major_4h` score `-3.6414` n `125` status `ready` deltaP `-0.7805` edge `-0.0625` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-4.9326` n `88` status `ready` deltaP `-5.6976` edge `-0.0087` maxDD `-35.189`
- `market_context_high->unknown_1h` score `-7.1521` n `125` status `ready` deltaP `0.1521` edge `-0.5513` maxDD `-1.3246`
- `market_context_high->crypto_alt_4h` score `-7.9995` n `125` status `ready` deltaP `-11.7524` edge `-0.1004` maxDD `-26.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
