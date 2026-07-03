# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T17:52:25.085114+00:00`
- Price records: `672`
- Market context records: `5581`
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

- `market_context_high->equity_24h` score `4.1023` n `174` status `ready` deltaP `15.0084` edge `0.7497` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.1838` n `196` status `ready` deltaP `11.4298` edge `0.2517` maxDD `-14.0065`
- `market_context_high->fx_24h` score `0.8999` n `174` status `ready` deltaP `17.9658` edge `0.0526` maxDD `-1.457`
- `market_context_high->crypto_major_24h` score `0.6438` n `174` status `ready` deltaP `13.4519` edge `0.418` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `0.6029` n `196` status `ready` deltaP `6.9033` edge `0.1683` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.5551` n `196` status `ready` deltaP `5.6433` edge `0.1725` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.191` n `208` status `ready` deltaP `5.8815` edge `0.037` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.1983` n `208` status `ready` deltaP `3.7368` edge `0.0079` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3229` n `208` status `ready` deltaP `0.6938` edge `0.0008` maxDD `-0.4122`
- `market_context_high->fx_4h` score `-0.3637` n `196` status `ready` deltaP `5.1269` edge `0.0089` maxDD `-0.8712`
- `market_context_high->metal_1h` score `-0.5274` n `208` status `ready` deltaP `-0.1497` edge `0.0009` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5972` n `208` status `ready` deltaP `1.0335` edge `0.0395` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7409` n `208` status `ready` deltaP `2.6716` edge `0.045` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.1933` n `208` status `ready` deltaP `-2.1591` edge `-0.0085` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.545` n `196` status `ready` deltaP `2.5168` edge `0.0154` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.0945` n `174` status `ready` deltaP `12.518` edge `0.0467` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0449` n `196` status `ready` deltaP `-13.6231` edge `-0.0612` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.2927` n `196` status `ready` deltaP `-5.9358` edge `-0.0506` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.9459` n `174` status `ready` deltaP `-8.3273` edge `-0.2271` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-9.4299` n `174` status `ready` deltaP `3.2388` edge `0.0623` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
