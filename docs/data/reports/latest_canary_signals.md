# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T07:07:32.080398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.136` n `12`; crypto_alt avg `0.0897` n `228`; crypto_major avg `-0.0066` n `8`; equity avg `0.0089` n `77`; fx avg `0.0292` n `6`; index avg `0.0318` n `23`; metal avg `0.2321` n `18`; unknown avg `-0.0025` n `687`
- 1h: commodity avg `0.1243` n `12`; crypto_alt avg `0.3055` n `228`; crypto_major avg `0.4616` n `8`; equity avg `0.1845` n `77`; fx avg `-0.0054` n `6`; index avg `0.0467` n `23`; metal avg `0.347` n `18`; unknown avg `0.492` n `687`
- 4h: commodity avg `0.061` n `12`; crypto_alt avg `1.4458` n `228`; crypto_major avg `1.6403` n `8`; equity avg `0.5468` n `77`; fx avg `-0.0242` n `6`; index avg `0.0663` n `23`; metal avg `0.3449` n `18`; unknown avg `1.1695` n `647`
- 24h: commodity avg `0.6077` n `12`; crypto_alt avg `0.7682` n `228`; crypto_major avg `2.8134` n `8`; equity avg `1.3613` n `76`; fx avg `-0.1235` n `6`; index avg `0.4032` n `23`; metal avg `0.2019` n `16`; unknown avg `1.7724` n `608`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
