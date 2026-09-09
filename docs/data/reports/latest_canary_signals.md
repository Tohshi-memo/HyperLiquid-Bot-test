# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T13:22:29.750605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0492` n `12`; crypto_alt avg `-0.0389` n `233`; crypto_major avg `0.0116` n `8`; equity avg `0.1052` n `134`; fx avg `-0.0005` n `6`; index avg `0.0061` n `26`; metal avg `0.1416` n `20`; unknown avg `0.1034` n `799`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `0.1938` n `233`; crypto_major avg `0.121` n `8`; equity avg `0.2393` n `134`; fx avg `-0.0139` n `6`; index avg `0.0368` n `26`; metal avg `0.3921` n `20`; unknown avg `0.7859` n `790`
- 4h: commodity avg `0.0173` n `12`; crypto_alt avg `-0.0795` n `233`; crypto_major avg `0.0357` n `8`; equity avg `-0.5174` n `134`; fx avg `0.0022` n `6`; index avg `-0.1308` n `26`; metal avg `0.3093` n `20`; unknown avg `0.5475` n `790`
- 24h: commodity avg `0.1623` n `12`; crypto_alt avg `0.7573` n `232`; crypto_major avg `1.8044` n `8`; equity avg `0.1695` n `134`; fx avg `-0.1089` n `6`; index avg `-0.2279` n `26`; metal avg `0.1882` n `20`; unknown avg `1.4946` n `689`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
