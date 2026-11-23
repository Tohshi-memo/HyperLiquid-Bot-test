# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T09:37:53.491580+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4482`

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

- `market_context_high->unknown_1h` score `19781.7414` n `70` status `ready` deltaP `1.3088` edge `1648.4859` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `13134.9819` n `70` status `ready` deltaP `3.7936` edge `1094.5704` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1298.1599` n `31` status `ready` deltaP `3.4286` edge `108.1747` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1153.0272` n `31` status `ready` deltaP `4.8535` edge `96.0589` maxDD `-0.119`
- `news_risk_high->equity_24h` score `46.375` n `30` status `ready` deltaP `52.2569` edge `3.5162` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.4781` n `30` status `ready` deltaP `48.6111` edge `2.7991` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.8876` n `30` status `ready` deltaP `48.7847` edge `2.4154` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.6508` n `30` status `ready` deltaP `52.2222` edge `0.8169` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.743` n `31` status `ready` deltaP `34.4808` edge `0.7136` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.2484` n `31` status `ready` deltaP `22.6445` edge `0.7901` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.3475` n `30` status `ready` deltaP `50.1736` edge `0.2778` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.478` n `30` status `ready` deltaP `55.1042` edge `0.1853` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.2323` n `31` status `ready` deltaP `11.9001` edge `0.8614` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.6788` n `31` status `ready` deltaP `18.4904` edge `0.202` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.414` n `31` status `ready` deltaP `35.8527` edge `0.0715` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6507` n `31` status `ready` deltaP `31.0943` edge `0.0221` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3176` n `31` status `ready` deltaP `8.6633` edge `0.2855` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9263` n `31` status `ready` deltaP `7.316` edge `0.2339` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5174` n `31` status `ready` deltaP `28.9839` edge `0.0292` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4088` n `31` status `ready` deltaP `19.522` edge `0.1062` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
