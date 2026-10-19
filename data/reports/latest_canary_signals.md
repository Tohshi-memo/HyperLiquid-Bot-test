# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T23:37:50.030462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `13`; crypto_alt avg `0.1698` n `237`; crypto_major avg `0.1124` n `8`; equity avg `0.0044` n `151`; fx avg `0.0109` n `6`; index avg `0.013` n `26`; metal avg `0.0069` n `20`; unknown avg `-0.0756` n `1198`
- 1h: commodity avg `0.0249` n `13`; crypto_alt avg `0.0329` n `237`; crypto_major avg `0.1169` n `8`; equity avg `-0.0453` n `151`; fx avg `0.009` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0191` n `20`; unknown avg `-0.1194` n `1194`
- 4h: commodity avg `-0.0553` n `13`; crypto_alt avg `0.8098` n `237`; crypto_major avg `0.6598` n `8`; equity avg `-0.241` n `151`; fx avg `0.0018` n `6`; index avg `-0.0172` n `26`; metal avg `-0.088` n `20`; unknown avg `4.311` n `1114`
- 24h: commodity avg `0.078` n `13`; crypto_alt avg `0.9138` n `237`; crypto_major avg `0.4857` n `8`; equity avg `1.4438` n `151`; fx avg `-0.0097` n `6`; index avg `0.313` n `26`; metal avg `-0.1941` n `20`; unknown avg `5.1097` n `980`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1935`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
