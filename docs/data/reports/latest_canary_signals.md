# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T15:07:51.810184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1994` n `12`; crypto_alt avg `0.035` n `228`; crypto_major avg `0.155` n `8`; equity avg `-0.0845` n `77`; fx avg `0.0193` n `6`; index avg `-0.0904` n `23`; metal avg `0.0104` n `18`; unknown avg `-0.0276` n `687`
- 1h: commodity avg `-0.1452` n `12`; crypto_alt avg `-0.9746` n `228`; crypto_major avg `-0.8135` n `8`; equity avg `-0.9783` n `77`; fx avg `0.0495` n `6`; index avg `-0.5811` n `23`; metal avg `-0.4131` n `18`; unknown avg `-0.2075` n `687`
- 4h: commodity avg `0.0173` n `12`; crypto_alt avg `-1.6756` n `228`; crypto_major avg `-1.2808` n `8`; equity avg `-1.4132` n `77`; fx avg `0.0073` n `6`; index avg `-0.6033` n `23`; metal avg `-0.2545` n `18`; unknown avg `0.2572` n `687`
- 24h: commodity avg `-0.5038` n `12`; crypto_alt avg `-2.3432` n `228`; crypto_major avg `-0.4401` n `8`; equity avg `-0.2437` n `77`; fx avg `-0.0373` n `6`; index avg `-0.3676` n `23`; metal avg `-0.3482` n `18`; unknown avg `-0.1011` n `623`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0414`, n `668`, weak_sample_signal
