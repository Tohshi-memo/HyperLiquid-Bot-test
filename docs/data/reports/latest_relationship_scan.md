# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T08:52:37.786297+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4873`

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

- `market_context_high->unknown_4h` score `806.6225` n `32` status `ready` deltaP `8.8415` edge `67.1596` maxDD `0.0`
- `market_context_high->unknown_1h` score `225.28` n `32` status `ready` deltaP `6.4933` edge `18.7411` maxDD `-0.2178`
- `news_risk_high->crypto_alt_24h` score `5.5852` n `105` status `ready` deltaP `26.4485` edge `0.8559` maxDD `-21.2934`
- `market_context_high->crypto_alt_4h` score `5.168` n `32` status `ready` deltaP `23.3994` edge `0.3041` maxDD `-1.6876`
- `market_context_high->equity_4h` score `4.9863` n `32` status `ready` deltaP `5.8689` edge `0.4466` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `3.9617` n `32` status `ready` deltaP `20.3506` edge `0.2281` maxDD `-1.6901`
- `market_context_high->equity_1h` score `3.1314` n `32` status `ready` deltaP `9.2253` edge `0.2395` maxDD `-1.2043`
- `market_context_high->index_4h` score `2.4702` n `32` status `ready` deltaP `23.7043` edge `0.0705` maxDD `-0.1474`
- `news_risk_high->crypto_alt_4h` score `1.628` n `128` status `ready` deltaP `10.1182` edge `0.2799` maxDD `-7.4246`
- `market_context_high->crypto_major_1h` score `1.1574` n `32` status `ready` deltaP `9.2253` edge `0.1259` maxDD `-1.1219`
- `market_context_high->crypto_alt_1h` score `1.0468` n `32` status `ready` deltaP `6.9985` edge `0.1317` maxDD `-1.5324`
- `market_context_high->fx_1h` score `0.9107` n `32` status `ready` deltaP `12.0509` edge `0.0127` maxDD `-0.0388`
- `market_context_high->commodity_4h` score `0.8689` n `32` status `ready` deltaP `18.2165` edge `0.0312` maxDD `-1.633`
- `market_context_high->metal_4h` score `0.6112` n `32` status `ready` deltaP `11.7378` edge `0.0426` maxDD `-0.7323`
- `market_context_high->index_1h` score `0.2763` n `32` status `ready` deltaP `2.2268` edge `0.0323` maxDD `-0.2628`
- `market_context_high->metal_1h` score `0.1267` n `32` status `ready` deltaP `4.1916` edge `0.014` maxDD `-0.3895`
- `news_risk_high->crypto_alt_1h` score `-0.2802` n `139` status `ready` deltaP `2.5471` edge `0.0544` maxDD `-4.584`
- `market_context_high->commodity_1h` score `-0.5598` n `32` status `ready` deltaP `-4.753` edge `0.0138` maxDD `-0.6439`
- `news_risk_high->fx_1h` score `-0.5755` n `139` status `ready` deltaP `-0.0894` edge `-0.0031` maxDD `-0.6065`
- `market_context_high->fx_4h` score `-0.62` n `32` status `ready` deltaP `-4.3445` edge `0.0164` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
