# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T18:07:30.893683+00:00`
- Price records: `672`
- Market context records: `7589`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14550`

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

- `market_context_high->commodity_4h` score `0.0741` n `154` status `ready` deltaP `8.8169` edge `0.0234` maxDD `-2.4139`
- `market_context_high->commodity_24h` score `0.0572` n `146` status `ready` deltaP `13.6223` edge `0.0723` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.0212` n `154` status `ready` deltaP `5.9495` edge `0.0119` maxDD `-0.9072`
- `market_context_high->unknown_24h` score `-0.1292` n `147` status `ready` deltaP `10.5513` edge `0.0983` maxDD `-7.4832`
- `market_context_high->commodity_1h` score `-0.23` n `154` status `ready` deltaP `5.2884` edge `0.0028` maxDD `-1.5775`
- `market_context_high->fx_24h` score `-0.4121` n `146` status `ready` deltaP `8.9686` edge `0.0167` maxDD `-3.2001`
- `market_context_high->crypto_alt_1h` score `-0.4484` n `154` status `ready` deltaP `0.6494` edge `0.0128` maxDD `-3.6359`
- `market_context_high->crypto_major_1h` score `-0.4648` n `154` status `ready` deltaP `6.3944` edge `0.013` maxDD `-5.5504`
- `market_context_high->equity_1h` score `-0.617` n `154` status `ready` deltaP `5.7506` edge `0.0521` maxDD `-8.8965`
- `market_context_high->index_4h` score `-0.6286` n `154` status `ready` deltaP `9.3213` edge `0.0299` maxDD `-3.4775`
- `market_context_high->fx_1h` score `-0.6475` n `154` status `ready` deltaP `-0.3939` edge `-0.0014` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.9006` n `154` status `ready` deltaP `1.845` edge `0.0172` maxDD `-1.0307`
- `market_context_high->unknown_1h` score `-0.9744` n `154` status `ready` deltaP `-0.1011` edge `-0.0619` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.2046` n `154` status `ready` deltaP `1.4908` edge `0.0454` maxDD `-10.1158`
- `market_context_high->crypto_major_4h` score `-1.6281` n `154` status `ready` deltaP `6.3411` edge `0.0527` maxDD `-16.63`
- `market_context_high->metal_4h` score `-1.6685` n `154` status `ready` deltaP `-1.6095` edge `0.045` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.753` n `154` status `ready` deltaP `2.1407` edge `0.1977` maxDD `-21.9375`
- `market_context_high->fx_4h` score `-2.3259` n `154` status `ready` deltaP `-3.354` edge `-0.003` maxDD `-2.1439`
- `market_context_high->equity_24h` score `-2.3664` n `146` status `ready` deltaP `16.4575` edge `0.4558` maxDD `-62.5118`
- `market_context_high->unknown_4h` score `-2.6871` n `154` status `ready` deltaP `10.7955` edge `-0.1919` maxDD `-5.2989`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
