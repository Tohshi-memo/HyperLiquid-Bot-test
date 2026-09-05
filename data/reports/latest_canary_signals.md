# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T20:52:25.849160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `0.0662` n `232`; crypto_major avg `0.0403` n `8`; equity avg `-0.0066` n `134`; fx avg `-0.0068` n `6`; index avg `-0.0014` n `26`; metal avg `0.0035` n `20`; unknown avg `-0.267` n `794`
- 1h: commodity avg `-0.0167` n `12`; crypto_alt avg `0.1471` n `232`; crypto_major avg `-0.0542` n `8`; equity avg `0.0102` n `134`; fx avg `-0.002` n `6`; index avg `-0.0029` n `26`; metal avg `0.0045` n `20`; unknown avg `-0.1823` n `774`
- 4h: commodity avg `0.054` n `12`; crypto_alt avg `0.4881` n `232`; crypto_major avg `0.2742` n `8`; equity avg `0.0324` n `134`; fx avg `-0.0417` n `6`; index avg `0.024` n `26`; metal avg `0.0086` n `20`; unknown avg `1.1214` n `774`
- 24h: commodity avg `0.1084` n `12`; crypto_alt avg `2.8472` n `232`; crypto_major avg `2.4505` n `8`; equity avg `0.2332` n `134`; fx avg `-0.0312` n `6`; index avg `0.036` n `26`; metal avg `0.0641` n `20`; unknown avg `322.0622` n `688`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
