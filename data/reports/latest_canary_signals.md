# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T10:37:24.166268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `0.0515` n `232`; crypto_major avg `-0.0676` n `8`; equity avg `0.0139` n `134`; fx avg `0.0167` n `6`; index avg `-0.0132` n `26`; metal avg `-0.0072` n `20`; unknown avg `161.0293` n `794`
- 1h: commodity avg `0.0013` n `12`; crypto_alt avg `0.223` n `232`; crypto_major avg `-0.1819` n `8`; equity avg `0.0628` n `134`; fx avg `0.0382` n `6`; index avg `0.0074` n `26`; metal avg `-0.0183` n `20`; unknown avg `-0.0399` n `792`
- 4h: commodity avg `-0.0062` n `12`; crypto_alt avg `0.4008` n `232`; crypto_major avg `0.0109` n `8`; equity avg `0.1085` n `134`; fx avg `0.0384` n `6`; index avg `0.0105` n `26`; metal avg `-0.009` n `20`; unknown avg `326.0137` n `784`
- 24h: commodity avg `0.1848` n `12`; crypto_alt avg `2.0449` n `232`; crypto_major avg `1.9989` n `8`; equity avg `0.5174` n `134`; fx avg `0.0065` n `6`; index avg `0.087` n `26`; metal avg `0.0065` n `20`; unknown avg `493.3881` n `676`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
