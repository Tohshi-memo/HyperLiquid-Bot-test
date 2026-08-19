# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T05:22:25.362290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0175` n `12`; crypto_alt avg `-0.013` n `230`; crypto_major avg `-0.0594` n `8`; equity avg `-0.1626` n `120`; fx avg `-0.0175` n `6`; index avg `-0.032` n `25`; metal avg `-0.0168` n `20`; unknown avg `0.1474` n `789`
- 1h: commodity avg `0.0106` n `12`; crypto_alt avg `-0.0382` n `230`; crypto_major avg `-0.0949` n `8`; equity avg `-0.2821` n `120`; fx avg `-0.0296` n `6`; index avg `-0.0406` n `25`; metal avg `-0.0971` n `20`; unknown avg `0.0251` n `789`
- 4h: commodity avg `-0.0254` n `12`; crypto_alt avg `-0.1108` n `230`; crypto_major avg `-0.183` n `8`; equity avg `-0.7648` n `120`; fx avg `-0.1145` n `6`; index avg `-0.1688` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.181` n `789`
- 24h: commodity avg `0.2584` n `12`; crypto_alt avg `0.455` n `230`; crypto_major avg `0.1411` n `8`; equity avg `-3.3583` n `120`; fx avg `-0.1637` n `6`; index avg `-0.5336` n `25`; metal avg `-0.6521` n `20`; unknown avg `-0.2514` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
