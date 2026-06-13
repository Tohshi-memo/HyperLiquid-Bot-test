# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T17:07:36.142007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1755` n `12`; crypto_alt avg `0.0413` n `228`; crypto_major avg `-0.0461` n `8`; equity avg `0.0458` n `74`; fx avg `0.0012` n `6`; index avg `0.0818` n `23`; metal avg `-0.0954` n `18`; unknown avg `-0.0762` n `644`
- 1h: commodity avg `-0.1235` n `12`; crypto_alt avg `-0.1728` n `228`; crypto_major avg `-0.2936` n `8`; equity avg `-0.1156` n `74`; fx avg `-0.0055` n `6`; index avg `-0.0048` n `23`; metal avg `-0.0735` n `18`; unknown avg `-0.0581` n `644`
- 4h: commodity avg `-0.0545` n `12`; crypto_alt avg `0.0251` n `228`; crypto_major avg `-0.2565` n `8`; equity avg `-0.0001` n `74`; fx avg `-0.0186` n `6`; index avg `0.0673` n `23`; metal avg `-0.0556` n `18`; unknown avg `-2.2567` n `644`
- 24h: commodity avg `-0.8001` n `12`; crypto_alt avg `1.3389` n `228`; crypto_major avg `-0.358` n `8`; equity avg `-0.1735` n `74`; fx avg `0.0185` n `6`; index avg `0.5512` n `23`; metal avg `0.3511` n `18`; unknown avg `-2.0697` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
