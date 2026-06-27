# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T18:22:31.284069+00:00`
- Price records: `672`
- Market context records: `4959`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9520`

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

- `market_context_high->unknown_1h` score `19.4242` n `95` status `ready` deltaP `9.1113` edge `1.5997` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.1153` n `94` status `ready` deltaP `28.7137` edge `0.8696` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.1973` n `94` status `ready` deltaP `21.283` edge `0.5803` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `6.9536` n `94` status `ready` deltaP `21.7339` edge `0.5698` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.7684` n `91` status `ready` deltaP `26.7991` edge `0.3363` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.6621` n `94` status `ready` deltaP `13.6741` edge `0.1855` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.4973` n `94` status `ready` deltaP `11.8708` edge `0.1202` maxDD `-1.9651`
- `market_context_high->equity_1h` score `1.0347` n `95` status `ready` deltaP `9.5509` edge `0.0799` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.9587` n `95` status `ready` deltaP `9.3823` edge `0.1642` maxDD `-5.6406`
- `market_context_high->index_4h` score `0.896` n `94` status `ready` deltaP `11.5562` edge `0.0438` maxDD `-0.6938`
- `market_context_high->crypto_alt_1h` score `0.7427` n `95` status `ready` deltaP `10.1497` edge `0.1298` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.2517` n `95` status `ready` deltaP `6.2196` edge `0.0375` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.3088` n `95` status `ready` deltaP `3.3895` edge `0.0133` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.3646` n `95` status `ready` deltaP `1.7145` edge `0.0078` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-1.0451` n `94` status `ready` deltaP `6.5613` edge `-0.0063` maxDD `-4.9624`
- `market_context_high->fx_4h` score `-1.1239` n `94` status `ready` deltaP `-6.383` edge `-0.0045` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.4733` n `91` status `ready` deltaP `-1.4766` edge `-0.0119` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.5006` n `95` status `ready` deltaP `-9.116` edge `-0.0043` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-3.9983` n `91` status `ready` deltaP `19.6485` edge `0.0467` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.9108` n `91` status `ready` deltaP `-9.1671` edge `0.0307` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
