# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T01:07:28.031758+00:00`
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

- `market_context_high->unknown_24h` score `45.9992` n `77` status `ready` deltaP `-37.8179` edge `6.4178` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `4.4958` n `77` status `ready` deltaP `34.145` edge `0.1819` maxDD `-0.4576`
- `market_context_high->commodity_4h` score `0.9318` n `106` status `ready` deltaP `10.9497` edge `0.0517` maxDD `-0.7636`
- `market_context_high->index_24h` score `0.5269` n `77` status `ready` deltaP `14.9509` edge `-0.0329` maxDD `-0.1624`
- `market_context_high->metal_4h` score `-0.1506` n `106` status `ready` deltaP `16.915` edge `0.0154` maxDD `-4.5909`
- `market_context_high->crypto_major_24h` score `-0.2235` n `77` status `ready` deltaP `-1.4273` edge `0.1796` maxDD `-10.5655`
- `market_context_high->metal_1h` score `-0.4107` n `112` status `ready` deltaP `5.0471` edge `0.0037` maxDD `-1.7257`
- `market_context_high->fx_1h` score `-0.4176` n `112` status `ready` deltaP `-2.2348` edge `-0.0016` maxDD `-0.2968`
- `market_context_high->fx_4h` score `-0.4977` n `106` status `ready` deltaP `0.1438` edge `-0.0043` maxDD `-0.504`
- `market_context_high->commodity_1h` score `-0.5064` n `112` status `ready` deltaP `-1.0532` edge `0.0094` maxDD `-0.8998`
- `market_context_high->index_1h` score `-0.7006` n `112` status `ready` deltaP `-5.3945` edge `-0.0017` maxDD `-0.5064`
- `market_context_high->index_4h` score `-1.2597` n `106` status `ready` deltaP `-11.2517` edge `-0.0056` maxDD `-0.8045`
- `market_context_high->crypto_major_4h` score `-1.4177` n `106` status `ready` deltaP `1.5532` edge `-0.0077` maxDD `-4.6638`
- `market_context_high->crypto_alt_1h` score `-1.9263` n `112` status `ready` deltaP `-5.6565` edge `-0.0176` maxDD `-4.7507`
- `market_context_high->crypto_major_1h` score `-1.9635` n `112` status `ready` deltaP `-6.25` edge `-0.0209` maxDD `-4.0845`
- `market_context_high->equity_1h` score `-2.164` n `112` status `ready` deltaP `-8.3832` edge `-0.0377` maxDD `-3.606`
- `market_context_high->metal_24h` score `-2.7368` n `77` status `ready` deltaP `-16.8719` edge `0.0128` maxDD `-7.0954`
- `market_context_high->fx_24h` score `-2.7716` n `77` status `ready` deltaP `-24.6573` edge `-0.0302` maxDD `-1.8596`
- `market_context_high->equity_24h` score `-3.0618` n `77` status `ready` deltaP `8.7279` edge `-0.1342` maxDD `-10.6642`
- `market_context_high->crypto_alt_4h` score `-5.7669` n `106` status `ready` deltaP `-8.853` edge `-0.0534` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
