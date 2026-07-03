# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T19:22:30.707679+00:00`
- Price records: `672`
- Market context records: `5587`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11423`

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

- `market_context_high->equity_24h` score `3.8875` n `174` status `ready` deltaP `15.0084` edge `0.7318` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.1742` n `202` status `ready` deltaP `11.8042` edge `0.2484` maxDD `-14.0065`
- `market_context_high->fx_24h` score `0.9988` n `174` status `ready` deltaP `19.0075` edge `0.0539` maxDD `-1.457`
- `market_context_high->equity_4h` score `0.5884` n `202` status `ready` deltaP `6.2394` edge `0.1713` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.5296` n `202` status `ready` deltaP `6.8129` edge `0.1628` maxDD `-9.46`
- `market_context_high->crypto_major_24h` score `0.2691` n `174` status `ready` deltaP `12.7575` edge `0.3914` maxDD `-29.6555`
- `market_context_high->equity_1h` score `-0.1692` n `214` status `ready` deltaP `6.3294` edge `0.0368` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.2832` n `214` status `ready` deltaP `2.7814` edge `0.0072` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.2988` n `214` status `ready` deltaP `1.157` edge `0.0008` maxDD `-0.4122`
- `market_context_high->crypto_major_1h` score `-0.4161` n `214` status `ready` deltaP `3.5704` edge `0.0474` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5815` n `214` status `ready` deltaP `-1.0843` edge `0.0002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6371` n `214` status `ready` deltaP `0.5946` edge `0.0391` maxDD `-5.0257`
- `market_context_high->fx_4h` score `-0.6872` n `202` status `ready` deltaP `4.223` edge `0.0088` maxDD `-0.8712`
- `market_context_high->commodity_1h` score `-1.2156` n `214` status `ready` deltaP `-2.468` edge `-0.0083` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5247` n `202` status `ready` deltaP `2.8903` edge `0.0146` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.2072` n `174` status `ready` deltaP `11.4763` edge `0.0392` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0076` n `202` status `ready` deltaP `-13.0992` edge `-0.0599` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1887` n `202` status `ready` deltaP `-5.1754` edge `-0.047` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.9904` n `174` status `ready` deltaP `-8.3273` edge `-0.2328` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-9.831` n `174` status `ready` deltaP `2.5443` edge `0.0335` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
