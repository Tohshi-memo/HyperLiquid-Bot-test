# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T04:52:33.697105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `12`; crypto_alt avg `-0.0533` n `228`; crypto_major avg `0.0317` n `8`; equity avg `-0.0705` n `77`; fx avg `-0.0292` n `6`; index avg `0.11` n `23`; metal avg `-0.0183` n `18`; unknown avg `0.0093` n `687`
- 1h: commodity avg `-0.0504` n `12`; crypto_alt avg `-0.697` n `228`; crypto_major avg `-0.3583` n `8`; equity avg `-0.1076` n `77`; fx avg `-0.027` n `6`; index avg `-0.0719` n `23`; metal avg `-0.1468` n `18`; unknown avg `0.1148` n `687`
- 4h: commodity avg `-0.4329` n `12`; crypto_alt avg `-0.8186` n `228`; crypto_major avg `-0.3355` n `8`; equity avg `0.1831` n `77`; fx avg `-0.0584` n `6`; index avg `0.072` n `23`; metal avg `0.0155` n `18`; unknown avg `-0.0493` n `671`
- 24h: commodity avg `0.3337` n `12`; crypto_alt avg `-0.1532` n `228`; crypto_major avg `1.7277` n `8`; equity avg `1.0156` n `76`; fx avg `-0.0986` n `6`; index avg `0.5716` n `23`; metal avg `-0.4189` n `18`; unknown avg `0.8452` n `503`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
