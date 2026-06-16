# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T07:22:37.750319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2018` n `12`; crypto_alt avg `-0.1746` n `228`; crypto_major avg `-0.1408` n `8`; equity avg `-0.0011` n `77`; fx avg `0.0219` n `6`; index avg `-0.0063` n `23`; metal avg `0.0009` n `18`; unknown avg `-0.0643` n `687`
- 1h: commodity avg `-0.1988` n `12`; crypto_alt avg `0.1234` n `228`; crypto_major avg `0.2633` n `8`; equity avg `0.135` n `77`; fx avg `-0.0005` n `6`; index avg `0.0215` n `23`; metal avg `0.2801` n `18`; unknown avg `-0.0331` n `687`
- 4h: commodity avg `-0.1454` n `12`; crypto_alt avg `0.9789` n `228`; crypto_major avg `1.3327` n `8`; equity avg `0.4736` n `77`; fx avg `-0.006` n `6`; index avg `-0.0195` n `23`; metal avg `0.3351` n `18`; unknown avg `1.0162` n `647`
- 24h: commodity avg `0.5612` n `12`; crypto_alt avg `0.361` n `228`; crypto_major avg `2.5165` n `8`; equity avg `1.2638` n `76`; fx avg `-0.1064` n `6`; index avg `0.397` n `23`; metal avg `0.0064` n `18`; unknown avg `1.5662` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
