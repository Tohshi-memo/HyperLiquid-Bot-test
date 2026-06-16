# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T06:37:37.626713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `12`; crypto_alt avg `0.3119` n `228`; crypto_major avg `0.327` n `8`; equity avg `0.1162` n `77`; fx avg `-0.0113` n `6`; index avg `0.0241` n `23`; metal avg `0.0527` n `18`; unknown avg `-0.0071` n `687`
- 1h: commodity avg `0.234` n `12`; crypto_alt avg `0.4394` n `228`; crypto_major avg `0.4172` n `8`; equity avg `0.2071` n `77`; fx avg `-0.0137` n `6`; index avg `0.0419` n `23`; metal avg `0.1743` n `18`; unknown avg `0.4957` n `647`
- 4h: commodity avg `-0.0716` n `12`; crypto_alt avg `1.411` n `228`; crypto_major avg `1.5178` n `8`; equity avg `0.5366` n `77`; fx avg `-0.016` n `6`; index avg `0.0345` n `23`; metal avg `0.1981` n `18`; unknown avg `0.8181` n `639`
- 24h: commodity avg `0.441` n `12`; crypto_alt avg `0.6629` n `228`; crypto_major avg `2.8617` n `8`; equity avg `1.431` n `76`; fx avg `-0.1325` n `6`; index avg `0.6563` n `23`; metal avg `-0.0778` n `18`; unknown avg `1.9677` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
