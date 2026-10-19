# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T20:42:11.126372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `13`; crypto_alt avg `-0.2108` n `237`; crypto_major avg `-0.0336` n `8`; equity avg `0.0359` n `151`; fx avg `-0.0008` n `6`; index avg `0.011` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.9224` n `1194`
- 1h: commodity avg `-0.012` n `13`; crypto_alt avg `0.0101` n `237`; crypto_major avg `0.1503` n `8`; equity avg `-0.3918` n `151`; fx avg `-0.0031` n `6`; index avg `-0.0466` n `26`; metal avg `-0.0519` n `20`; unknown avg `0.0396` n `1128`
- 4h: commodity avg `-0.1291` n `13`; crypto_alt avg `-0.3513` n `237`; crypto_major avg `-0.0009` n `8`; equity avg `-0.5075` n `151`; fx avg `0.0` n `6`; index avg `-0.0555` n `26`; metal avg `-0.0484` n `20`; unknown avg `-0.1219` n `1128`
- 24h: commodity avg `-0.3049` n `13`; crypto_alt avg `3.1751` n `237`; crypto_major avg `2.4844` n `8`; equity avg `2.8973` n `151`; fx avg `-0.0129` n `6`; index avg `0.5909` n `26`; metal avg `0.1111` n `20`; unknown avg `3.0738` n `908`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
