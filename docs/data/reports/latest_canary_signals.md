# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T19:07:29.912135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.1567` n `232`; crypto_major avg `-0.1519` n `8`; equity avg `0.0069` n `134`; fx avg `0.0103` n `6`; index avg `0.0114` n `26`; metal avg `0.0156` n `20`; unknown avg `-0.4036` n `794`
- 1h: commodity avg `-0.0358` n `12`; crypto_alt avg `-0.3167` n `232`; crypto_major avg `-0.2069` n `8`; equity avg `-0.0346` n `134`; fx avg `-0.0031` n `6`; index avg `0.0116` n `26`; metal avg `0.023` n `20`; unknown avg `-0.073` n `794`
- 4h: commodity avg `-0.1081` n `12`; crypto_alt avg `-0.6373` n `232`; crypto_major avg `-0.2851` n `8`; equity avg `0.1349` n `134`; fx avg `-0.0235` n `6`; index avg `0.0661` n `26`; metal avg `0.0082` n `20`; unknown avg `-0.6042` n `768`
- 24h: commodity avg `0.1585` n `12`; crypto_alt avg `0.077` n `232`; crypto_major avg `-1.0057` n `8`; equity avg `0.4104` n `134`; fx avg `-0.1236` n `6`; index avg `0.0902` n `26`; metal avg `0.0044` n `20`; unknown avg `0.9972` n `661`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
