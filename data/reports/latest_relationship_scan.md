# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T17:07:27.308294+00:00`
- Price records: `672`
- Market context records: `5578`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11397`

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

- `market_context_high->equity_24h` score `4.2391` n `174` status `ready` deltaP `15.0084` edge `0.7611` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.216` n `193` status `ready` deltaP `11.2923` edge `0.2553` maxDD `-14.0065`
- `market_context_high->fx_24h` score `0.851` n `174` status `ready` deltaP `17.445` edge `0.052` maxDD `-1.457`
- `market_context_high->crypto_major_24h` score `0.7933` n `174` status `ready` deltaP `13.6255` edge `0.4293` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `0.6302` n `193` status `ready` deltaP `6.7499` edge `0.1716` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.588` n `193` status `ready` deltaP `5.5297` edge `0.176` maxDD `-7.4425`
- `market_context_high->index_1h` score `-0.2095` n `205` status `ready` deltaP `3.5527` edge `0.0082` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.2747` n `205` status `ready` deltaP `5.7748` edge `0.0393` maxDD `-5.0555`
- `market_context_high->fx_4h` score `-0.3218` n `193` status `ready` deltaP `5.6213` edge `0.0091` maxDD `-0.8712`
- `market_context_high->fx_1h` score `-0.4851` n `205` status `ready` deltaP `0.8091` edge `0.001` maxDD `-0.4122`
- `market_context_high->metal_1h` score `-0.523` n `205` status `ready` deltaP `-0.0942` edge `0.0011` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6303` n `205` status `ready` deltaP `0.6645` edge `0.0392` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7852` n `205` status `ready` deltaP `2.2674` edge `0.044` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.2159` n `205` status `ready` deltaP `-2.4558` edge `-0.0084` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.521` n `193` status `ready` deltaP `2.6657` edge `0.0164` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.0339` n `174` status `ready` deltaP `13.0388` edge `0.051` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0782` n `193` status `ready` deltaP `-14.157` edge `-0.0619` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.3892` n `193` status `ready` deltaP `-6.8716` edge `-0.0524` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.8982` n `174` status `ready` deltaP `-7.9801` edge `-0.2233` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-9.2305` n `174` status `ready` deltaP `3.586` edge `0.0766` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
