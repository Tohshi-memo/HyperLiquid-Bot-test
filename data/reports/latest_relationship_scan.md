# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T08:37:31.057003+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4814`

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

- `market_context_high->unknown_1h` score `340.7783` n `50` status `ready` deltaP `10.1257` edge `28.3356` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.3873` n `50` status `ready` deltaP `8.8415` edge `23.89` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.4314` n `66` status `ready` deltaP `39.5044` edge `0.9602` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.8959` n `50` status `ready` deltaP `36.1667` edge `0.8085` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `9.7681` n `66` status `ready` deltaP `36.5688` edge `0.6187` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `8.9673` n `50` status `ready` deltaP `16.5347` edge `0.808` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9469` n `50` status `ready` deltaP `17.5427` edge `0.5323` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9289` n `50` status `ready` deltaP `15.5793` edge `0.4362` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.325` n `95` status `ready` deltaP `16.1056` edge `0.3874` maxDD `-6.4152`
- `market_context_high->fx_4h` score `2.9323` n `50` status `ready` deltaP `32.8415` edge `0.0389` maxDD `-0.0791`
- `market_context_high->equity_24h` score `2.9068` n `50` status `ready` deltaP `13.6597` edge `0.4678` maxDD `-11.8957`
- `market_context_high->crypto_alt_1h` score `2.9025` n `50` status `ready` deltaP `13.9042` edge `0.2155` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.8668` n `50` status `ready` deltaP `14.0` edge `0.1906` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `2.3204` n `95` status `ready` deltaP `23.3505` edge `0.1073` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.4651` n `50` status `ready` deltaP `20.491` edge `0.0119` maxDD `-0.113`
- `market_context_high->index_24h` score `1.0037` n `50` status `ready` deltaP `16.1806` edge `0.0779` maxDD `-1.2338`
- `news_risk_high->crypto_major_24h` score `0.9664` n `66` status `ready` deltaP `5.6819` edge `0.4014` maxDD `-15.8971`
- `news_risk_high->crypto_alt_1h` score `0.9509` n `107` status `ready` deltaP `5.8481` edge `0.0965` maxDD `-2.4998`
- `news_risk_high->metal_24h` score `0.8537` n `66` status `ready` deltaP `6.8182` edge `0.1914` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.6477` n `95` status `ready` deltaP `8.4901` edge `0.2574` maxDD `-10.477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
