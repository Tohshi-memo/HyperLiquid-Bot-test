# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T12:37:17.786332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1462` n `12`; crypto_alt avg `0.1182` n `228`; crypto_major avg `0.0259` n `8`; equity avg `-0.0293` n `67`; fx avg `-0.0035` n `6`; index avg `0.0143` n `23`; metal avg `-0.0188` n `18`; unknown avg `0.0527` n `396`
- 1h: commodity avg `0.0868` n `12`; crypto_alt avg `-0.1305` n `228`; crypto_major avg `-0.1061` n `8`; equity avg `-0.081` n `67`; fx avg `-0.0118` n `6`; index avg `0.0605` n `23`; metal avg `-0.0056` n `18`; unknown avg `0.1572` n `396`
- 4h: commodity avg `0.1081` n `12`; crypto_alt avg `0.4262` n `228`; crypto_major avg `0.1227` n `8`; equity avg `0.1252` n `67`; fx avg `0.0313` n `6`; index avg `0.0531` n `23`; metal avg `-0.0698` n `18`; unknown avg `0.5576` n `396`
- 24h: commodity avg `0.563` n `12`; crypto_alt avg `-6.1443` n `228`; crypto_major avg `-4.63` n `8`; equity avg `-1.8673` n `67`; fx avg `0.0601` n `6`; index avg `-0.1656` n `23`; metal avg `-0.2649` n `18`; unknown avg `-2.0079` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0653`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0648`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0599`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0572`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0555`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0552`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.054`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0536`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.047`, n `669`, weak_sample_signal
