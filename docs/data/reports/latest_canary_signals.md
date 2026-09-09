# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T12:37:33.150505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0364` n `12`; crypto_alt avg `0.0836` n `233`; crypto_major avg `0.0549` n `8`; equity avg `0.0245` n `134`; fx avg `0.0051` n `6`; index avg `0.0156` n `26`; metal avg `0.0038` n `20`; unknown avg `0.4872` n `792`
- 1h: commodity avg `-0.0546` n `12`; crypto_alt avg `0.3399` n `233`; crypto_major avg `0.5682` n `8`; equity avg `0.0118` n `134`; fx avg `0.0066` n `6`; index avg `-0.004` n `26`; metal avg `-0.0619` n `20`; unknown avg `0.2393` n `790`
- 4h: commodity avg `0.0939` n `12`; crypto_alt avg `-0.4402` n `233`; crypto_major avg `-0.217` n `8`; equity avg `-0.8444` n `134`; fx avg `-0.0014` n `6`; index avg `-0.1787` n `26`; metal avg `-0.1176` n `20`; unknown avg `14.0061` n `790`
- 24h: commodity avg `0.1001` n `12`; crypto_alt avg `0.4221` n `232`; crypto_major avg `1.59` n `8`; equity avg `0.065` n `134`; fx avg `-0.0799` n `6`; index avg `-0.1949` n `26`; metal avg `-0.1179` n `20`; unknown avg `1.1787` n `689`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
