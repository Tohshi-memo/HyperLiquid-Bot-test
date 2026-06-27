# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T17:37:24.767667+00:00`
- Price records: `672`
- Market context records: `4956`
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

- `market_context_high->unknown_1h` score `19.9054` n `94` status `ready` deltaP `9.9217` edge `1.6344` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.425` n `92` status `ready` deltaP `28.6254` edge `0.896` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.4153` n `92` status `ready` deltaP `22.329` edge `0.5915` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.1814` n `92` status `ready` deltaP `22.8261` edge `0.5815` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8389` n `91` status `ready` deltaP `27.3199` edge `0.3387` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7972` n `92` status `ready` deltaP `14.6275` edge `0.1904` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.6998` n `92` status `ready` deltaP `12.7916` edge `0.1226` maxDD `-1.9651`
- `market_context_high->equity_1h` score `1.0067` n `94` status `ready` deltaP `9.1254` edge `0.0804` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `1.0052` n `94` status `ready` deltaP `9.8261` edge `0.1672` maxDD `-5.6406`
- `market_context_high->index_4h` score `0.986` n `92` status `ready` deltaP `12.5464` edge `0.0447` maxDD `-0.6938`
- `market_context_high->crypto_alt_1h` score `0.7861` n `94` status `ready` deltaP `10.6383` edge `0.1321` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.1866` n `94` status `ready` deltaP `5.4051` edge `0.0375` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.3338` n `94` status `ready` deltaP `2.908` edge `0.0133` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.3456` n `94` status `ready` deltaP `2.0799` edge `0.0078` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.8907` n `92` status `ready` deltaP `7.4496` edge `-0.0039` maxDD `-4.5989`
- `market_context_high->fx_4h` score `-1.1726` n `92` status `ready` deltaP `-7.3038` edge `-0.0046` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.4232` n `91` status `ready` deltaP `-0.9558` edge `-0.0112` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.5196` n `94` status `ready` deltaP `-9.3388` edge `-0.0044` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-3.9959` n `91` status `ready` deltaP `19.6485` edge `0.0469` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.8909` n `91` status `ready` deltaP `-8.9935` edge `0.0312` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
