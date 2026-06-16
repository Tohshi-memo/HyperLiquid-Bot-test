# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T09:22:41.151181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0325` n `12`; crypto_alt avg `-0.3454` n `228`; crypto_major avg `-0.2528` n `8`; equity avg `-0.0631` n `77`; fx avg `0.0035` n `6`; index avg `-0.0556` n `23`; metal avg `-0.0951` n `18`; unknown avg `-0.0207` n `687`
- 1h: commodity avg `0.0594` n `12`; crypto_alt avg `0.3033` n `228`; crypto_major avg `0.4866` n `8`; equity avg `0.1806` n `77`; fx avg `0.0185` n `6`; index avg `0.0181` n `23`; metal avg `0.2084` n `18`; unknown avg `0.1207` n `687`
- 4h: commodity avg `-0.5061` n `12`; crypto_alt avg `1.254` n `228`; crypto_major avg `1.2744` n `8`; equity avg `0.5904` n `77`; fx avg `0.0385` n `6`; index avg `0.3169` n `23`; metal avg `0.7289` n `18`; unknown avg `0.3336` n `647`
- 24h: commodity avg `0.0672` n `12`; crypto_alt avg `1.3397` n `228`; crypto_major avg `3.3237` n `8`; equity avg `1.7633` n `76`; fx avg `-0.0691` n `6`; index avg `0.5305` n `23`; metal avg `0.0986` n `18`; unknown avg `0.2318` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
