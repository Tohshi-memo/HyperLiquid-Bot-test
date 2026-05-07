# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T13:52:20.117320+00:00`
- Price records: `555`
- Market context records: `651`
- Flow alert records: `1848`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `795`

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

- `market_context_high->crypto_major_24h` score `7.4547` n `146` status `ready` deltaP `19.6675` edge `0.5235` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.067` n `146` status `ready` deltaP `8.6833` edge `0.4525` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1585` n `146` status `ready` deltaP `7.9388` edge `0.0139` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.362` n `146` status `ready` deltaP `1.2734` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4174` n `146` status `ready` deltaP `2.4242` edge `0.0465` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6402` n `146` status `ready` deltaP `0.447` edge `0.0003` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.2396` n `146` status `ready` deltaP `-1.9296` edge `-0.0094` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2423` n `146` status `ready` deltaP `-4.7684` edge `-0.0114` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.244` n `146` status `ready` deltaP `5.3999` edge `-0.0082` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.6715` n `146` status `ready` deltaP `5.687` edge `-0.0049` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1042` n `146` status `ready` deltaP `3.8287` edge `0.0561` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.1376` n `146` status `ready` deltaP `0.3956` edge `-0.0285` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.3133` n `146` status `ready` deltaP `14.4039` edge `0.0818` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9226` n `146` status `ready` deltaP `-8.9613` edge `0.0157` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.133` n `146` status `ready` deltaP `-4.2581` edge `0.1174` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.3459` n `146` status `ready` deltaP `-3.9035` edge `-0.0376` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4511` n `146` status `ready` deltaP `-5.155` edge `-0.0573` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.5306` n `146` status `ready` deltaP `-5.7384` edge `-0.0254` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6878` n `146` status `ready` deltaP `-11.4707` edge `-0.0537` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.9336` n `146` status `ready` deltaP `0.4333` edge `-0.2262` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
