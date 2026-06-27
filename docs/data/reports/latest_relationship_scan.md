# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T10:07:31.323071+00:00`
- Price records: `672`
- Market context records: `4922`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9398`

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

- `market_context_high->unknown_1h` score `16.7841` n `103` status `ready` deltaP `10.3395` edge `1.3715` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.1206` n `103` status `ready` deltaP `28.5046` edge `0.7881` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `7.1203` n `103` status `ready` deltaP `23.5777` edge `0.5714` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.6655` n `103` status `ready` deltaP `18.6109` edge `0.5538` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.9859` n `85` status `ready` deltaP `26.2174` edge `0.3583` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.2933` n `103` status `ready` deltaP `9.4957` edge `0.1107` maxDD `-1.9651`
- `market_context_high->equity_4h` score `1.0364` n `103` status `ready` deltaP `13.7728` edge `0.1792` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.6766` n `103` status `ready` deltaP `9.2633` edge `0.0408` maxDD `-0.6938`
- `market_context_high->crypto_major_1h` score `0.4355` n `103` status `ready` deltaP `5.2758` edge `0.1245` maxDD `-5.6406`
- `market_context_high->equity_1h` score `0.3732` n `103` status `ready` deltaP `5.9386` edge `0.0656` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.2649` n `103` status `ready` deltaP `6.0156` edge `0.0961` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.0868` n `103` status `ready` deltaP `2.6626` edge `0.033` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.1738` n `103` status `ready` deltaP `4.0782` edge `0.0165` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5408` n `103` status `ready` deltaP `-0.7122` edge `0.0109` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.717` n `103` status `ready` deltaP `8.1474` edge `0.0046` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-0.9254` n `103` status `ready` deltaP `-2.9408` edge `-0.002` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.5323` n `103` status `ready` deltaP `-9.2146` edge `-0.005` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-2.0197` n `85` status `ready` deltaP `-7.5123` edge `-0.0172` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.9976` n `85` status `ready` deltaP `-10.5985` edge `-0.1615` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.0683` n `85` status `ready` deltaP `13.2639` edge `0.0001` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
