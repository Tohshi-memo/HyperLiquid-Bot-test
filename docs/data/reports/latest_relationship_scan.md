# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T08:07:27.895215+00:00`
- Price records: `672`
- Market context records: `4913`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9384`

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

- `market_context_high->unknown_1h` score `15.1349` n `108` status `ready` deltaP `9.4644` edge `1.2399` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.0697` n `108` status `ready` deltaP `24.729` edge `0.7257` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `6.6722` n `108` status `ready` deltaP `21.9061` edge `0.5452` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.4935` n `108` status `ready` deltaP `18.8008` edge `0.5382` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.4089` n `90` status `ready` deltaP `23.7153` edge `0.3269` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.2439` n `108` status `ready` deltaP `9.3439` edge `0.1076` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8785` n `108` status `ready` deltaP `12.0257` edge `0.1706` maxDD `-6.3852`
- `market_context_high->crypto_major_1h` score `0.5407` n `108` status `ready` deltaP `6.8197` edge `0.1277` maxDD `-5.6406`
- `market_context_high->index_4h` score `0.4655` n `108` status `ready` deltaP `9.8464` edge `0.0403` maxDD `-0.7006`
- `market_context_high->crypto_alt_1h` score `0.3936` n `108` status `ready` deltaP `7.3797` edge `0.1035` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.3091` n `108` status `ready` deltaP `5.3781` edge `0.0617` maxDD `-2.6339`
- `market_context_high->commodity_1h` score `-0.1679` n `108` status `ready` deltaP `4.1916` edge `0.0165` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2405` n `108` status `ready` deltaP `0.937` edge `0.0317` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5319` n `108` status `ready` deltaP `-0.5711` edge `0.0111` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.7559` n `108` status `ready` deltaP `7.4356` edge `0.0061` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-0.777` n `108` status `ready` deltaP `-0.9259` edge `0.0036` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-0.8937` n `108` status `ready` deltaP `-7.668` edge `-0.0022` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.6572` n `90` status `ready` deltaP `-4.375` edge `-0.0079` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-4.5724` n `90` status `ready` deltaP `16.5972` edge `0.0192` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.6937` n `90` status `ready` deltaP `-7.3958` edge `-0.1439` maxDD `-24.6845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
