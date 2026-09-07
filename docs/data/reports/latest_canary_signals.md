# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T14:07:29.227710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0448` n `12`; crypto_alt avg `-0.2015` n `232`; crypto_major avg `-0.2818` n `8`; equity avg `-0.0522` n `134`; fx avg `0.0145` n `6`; index avg `0.0044` n `26`; metal avg `0.0303` n `20`; unknown avg `1.2501` n `794`
- 1h: commodity avg `-0.0382` n `12`; crypto_alt avg `-0.5021` n `232`; crypto_major avg `-0.6289` n `8`; equity avg `-0.0032` n `134`; fx avg `0.0115` n `6`; index avg `0.0178` n `26`; metal avg `0.0841` n `20`; unknown avg `0.7354` n `794`
- 4h: commodity avg `0.2967` n `12`; crypto_alt avg `0.6563` n `232`; crypto_major avg `-0.0016` n `8`; equity avg `-0.0331` n `134`; fx avg `0.0475` n `6`; index avg `-0.0063` n `26`; metal avg `0.0448` n `20`; unknown avg `6683.7492` n `748`
- 24h: commodity avg `0.2104` n `12`; crypto_alt avg `0.674` n `232`; crypto_major avg `-0.797` n `8`; equity avg `0.3851` n `134`; fx avg `-0.0917` n `6`; index avg `0.0545` n `26`; metal avg `-0.0554` n `20`; unknown avg `224.171` n `680`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
