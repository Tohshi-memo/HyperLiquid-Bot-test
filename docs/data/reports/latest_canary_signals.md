# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T12:52:27.833581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0387` n `12`; crypto_alt avg `0.181` n `233`; crypto_major avg `0.2072` n `8`; equity avg `0.0932` n `134`; fx avg `-0.0206` n `6`; index avg `0.0104` n `26`; metal avg `0.0791` n `20`; unknown avg `-0.1669` n `798`
- 1h: commodity avg `0.0533` n `12`; crypto_alt avg `0.2886` n `233`; crypto_major avg `0.4191` n `8`; equity avg `-0.0549` n `134`; fx avg `-0.0064` n `6`; index avg `-0.0223` n `26`; metal avg `-0.05` n `20`; unknown avg `0.23` n `790`
- 4h: commodity avg `0.0721` n `12`; crypto_alt avg `-0.2792` n `233`; crypto_major avg `-0.0518` n `8`; equity avg `-0.7213` n `134`; fx avg `-0.0235` n `6`; index avg `-0.1592` n `26`; metal avg `-0.0357` n `20`; unknown avg `13.733` n `790`
- 24h: commodity avg `0.1235` n `12`; crypto_alt avg `0.5488` n `232`; crypto_major avg `1.8024` n `8`; equity avg `0.2` n `134`; fx avg `-0.0873` n `6`; index avg `-0.2139` n `26`; metal avg `-0.0369` n `20`; unknown avg `1.2426` n `689`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
