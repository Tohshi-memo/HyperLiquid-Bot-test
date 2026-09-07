# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T22:52:24.652581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `-0.0241` n `232`; crypto_major avg `0.0721` n `8`; equity avg `-0.0243` n `134`; fx avg `-0.0056` n `6`; index avg `-0.0079` n `26`; metal avg `-0.008` n `20`; unknown avg `0.4271` n `797`
- 1h: commodity avg `0.0487` n `12`; crypto_alt avg `-0.6246` n `232`; crypto_major avg `-0.2574` n `8`; equity avg `-0.1988` n `134`; fx avg `-0.0163` n `6`; index avg `-0.0486` n `26`; metal avg `-0.0307` n `20`; unknown avg `15.9334` n `794`
- 4h: commodity avg `0.0254` n `12`; crypto_alt avg `-0.3292` n `232`; crypto_major avg `-0.274` n `8`; equity avg `-0.0911` n `134`; fx avg `-0.0103` n `6`; index avg `-0.0321` n `26`; metal avg `0.0028` n `20`; unknown avg `7.5501` n `752`
- 24h: commodity avg `0.2332` n `12`; crypto_alt avg `-0.5597` n `232`; crypto_major avg `-1.4573` n `8`; equity avg `0.3193` n `134`; fx avg `-0.1691` n `6`; index avg `0.0441` n `26`; metal avg `0.0281` n `20`; unknown avg `7789.3602` n `642`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
