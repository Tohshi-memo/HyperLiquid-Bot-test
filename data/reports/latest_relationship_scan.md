# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T04:07:27.098290+00:00`
- Price records: `672`
- Market context records: `7100`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11488`

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

- `market_context_high->fx_4h` score `0.4056` n `155` status `ready` deltaP `16.2146` edge `0.0139` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.1098` n `155` status `ready` deltaP `0.4365` edge `0.0438` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.1761` n `155` status `ready` deltaP `4.1008` edge `0.0031` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.4373` n `155` status `ready` deltaP `0.565` edge `0.0266` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.5248` n `155` status `ready` deltaP `0.1014` edge `-0.006` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6066` n `155` status `ready` deltaP `3.2953` edge `0.0355` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8755` n `155` status `ready` deltaP `-4.6069` edge `-0.0199` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3818` n `155` status `ready` deltaP `-4.5771` edge `-0.0431` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.5582` n `155` status `ready` deltaP `-7.1345` edge `-0.0055` maxDD `-2.1427`
- `market_context_high->unknown_4h` score `-1.5945` n `155` status `ready` deltaP `-6.9187` edge `0.0019` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.1107` n `155` status `ready` deltaP `2.1866` edge `-0.0429` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.4533` n `155` status `ready` deltaP `-0.1839` edge `-0.0434` maxDD `-12.2591`
- `market_context_high->crypto_major_4h` score `-3.0291` n `155` status `ready` deltaP `4.0057` edge `0.0134` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.1436` n `155` status `ready` deltaP `-0.6874` edge `-0.0199` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.2463` n `155` status `ready` deltaP `-7.1617` edge `-0.0919` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.3387` n `155` status `ready` deltaP `-8.8575` edge `-0.0198` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-4.427` n `155` status `ready` deltaP `-8.9388` edge `-0.011` maxDD `-5.5324`
- `market_context_high->equity_4h` score `-8.5887` n `155` status `ready` deltaP `-0.3718` edge `-0.2116` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.9575` n `155` status `ready` deltaP `-24.4467` edge `-0.0688` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.9634` n `155` status `ready` deltaP `-25.2442` edge `-0.1402` maxDD `-43.0764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
