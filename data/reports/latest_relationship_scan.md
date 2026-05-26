# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T03:22:15.634565+00:00`
- Price records: `672`
- Market context records: `1907`
- Flow alert records: `7388`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `market_context_high->crypto_alt_4h` score `7.6866` n `199` status `ready` deltaP `24.0332` edge `0.5948` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.1179` n `199` status `ready` deltaP `28.6294` edge `0.5269` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.9117` n `199` status `ready` deltaP `17.5006` edge `0.4117` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.5237` n `199` status `ready` deltaP `15.0393` edge `0.2195` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.9415` n `185` status `ready` deltaP `16.9041` edge `0.2917` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.5374` n `185` status `ready` deltaP `13.0292` edge `0.5733` maxDD `-35.8966`
- `market_context_high->index_24h` score `1.2085` n `185` status `ready` deltaP `8.4366` edge `0.1673` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.6957` n `199` status `ready` deltaP `7.543` edge `0.1063` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4983` n `199` status `ready` deltaP `10.398` edge `0.0811` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.4979` n `199` status `ready` deltaP `6.9547` edge `0.1065` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.2034` n `185` status `ready` deltaP `14.4539` edge `0.0255` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0544` n `199` status `ready` deltaP `5.2862` edge `0.0396` maxDD `-2.6836`
- `market_context_high->equity_24h` score `-0.2988` n `185` status `ready` deltaP `8.9611` edge `0.4052` maxDD `-33.1875`
- `market_context_high->metal_1h` score `-0.5445` n `199` status `ready` deltaP `6.1317` edge `0.0229` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6122` n `199` status `ready` deltaP `-2.4539` edge `0.0011` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6493` n `199` status `ready` deltaP `-0.1557` edge `0.0101` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.7036` n `199` status `ready` deltaP `11.9331` edge `0.131` maxDD `-12.5349`
- `market_context_high->crypto_major_24h` score `-0.7379` n `185` status `ready` deltaP `16.9632` edge `0.684` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-0.8407` n `199` status `ready` deltaP `-2.9047` edge `0.0004` maxDD `-1.1056`
- `market_context_high->unknown_1h` score `-0.8683` n `199` status `ready` deltaP `2.2395` edge `0.0079` maxDD `-3.6151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
