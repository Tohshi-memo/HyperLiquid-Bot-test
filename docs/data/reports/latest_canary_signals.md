# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T06:07:27.785308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0247` n `12`; crypto_alt avg `-0.1008` n `232`; crypto_major avg `-0.119` n `8`; equity avg `-0.1975` n `134`; fx avg `-0.0011` n `6`; index avg `-0.0485` n `26`; metal avg `-0.0696` n `20`; unknown avg `0.9569` n `763`
- 1h: commodity avg `0.116` n `12`; crypto_alt avg `-0.0825` n `232`; crypto_major avg `-0.0805` n `8`; equity avg `-0.4841` n `134`; fx avg `0.0392` n `6`; index avg `-0.1311` n `26`; metal avg `-0.1524` n `20`; unknown avg `1.3438` n `763`
- 4h: commodity avg `0.2368` n `12`; crypto_alt avg `-0.6713` n `232`; crypto_major avg `-0.7411` n `8`; equity avg `-0.6446` n `134`; fx avg `0.0829` n `6`; index avg `-0.1725` n `26`; metal avg `-0.18` n `20`; unknown avg `0.8021` n `749`
- 24h: commodity avg `0.1376` n `12`; crypto_alt avg `0.5226` n `232`; crypto_major avg `-1.2786` n `8`; equity avg `-0.1636` n `134`; fx avg `-0.2136` n `6`; index avg `-0.0187` n `26`; metal avg `0.2627` n `20`; unknown avg `7509.6083` n `666`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
