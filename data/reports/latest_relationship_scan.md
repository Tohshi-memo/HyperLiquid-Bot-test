# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T01:07:30.856841+00:00`
- Price records: `672`
- Market context records: `7514`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14782`

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

- `risk_on_high->crypto_major_4h` score `7.4792` n `36` status `ready` deltaP `40.2947` edge `0.3739` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.4792` n `36` status `ready` deltaP `40.2947` edge `0.3739` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.3083` n `32` status `ready` deltaP `16.7732` edge `0.516` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `6.3083` n `32` status `ready` deltaP `16.7732` edge `0.516` maxDD `-5.8371`
- `risk_on_high->crypto_alt_4h` score `5.0999` n `36` status `ready` deltaP `31.0129` edge `0.2426` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.0999` n `36` status `ready` deltaP `31.0129` edge `0.2426` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.4393` n `36` status `ready` deltaP `14.5833` edge `0.3157` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.4393` n `36` status `ready` deltaP `14.5833` edge `0.3157` maxDD `-0.4384`
- `risk_on_high->crypto_alt_24h` score `2.0876` n `32` status `ready` deltaP `16.5728` edge `0.25` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.0876` n `32` status `ready` deltaP `16.5728` edge `0.25` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.6046` n `36` status `ready` deltaP `23.8024` edge `0.0715` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.6046` n `36` status `ready` deltaP `23.8024` edge `0.0715` maxDD `-0.957`
- `risk_on_high->fx_24h` score `0.5638` n `31` status `ready` deltaP `16.4993` edge `0.0079` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.5638` n `31` status `ready` deltaP `16.4993` edge `0.0079` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.5129` n `36` status `ready` deltaP `6.2312` edge `0.0293` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.5129` n `36` status `ready` deltaP `6.2312` edge `0.0293` maxDD `-0.2479`
- `risk_on_high->equity_1h` score `0.4099` n `36` status `ready` deltaP `7.8079` edge `0.0382` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.4099` n `36` status `ready` deltaP `7.8079` edge `0.0382` maxDD `-1.3497`
- `risk_on_high->metal_4h` score `0.312` n `36` status `ready` deltaP `4.2683` edge `0.0799` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.312` n `36` status `ready` deltaP `4.2683` edge `0.0799` maxDD `-0.5882`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
