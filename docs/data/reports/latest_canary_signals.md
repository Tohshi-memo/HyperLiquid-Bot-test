# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T22:07:27.652603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `12`; crypto_alt avg `0.2722` n `231`; crypto_major avg `0.1794` n `8`; equity avg `-0.0069` n `127`; fx avg `-0.0239` n `6`; index avg `0.0025` n `26`; metal avg `0.013` n `20`; unknown avg `0.2536` n `793`
- 1h: commodity avg `0.0265` n `12`; crypto_alt avg `-0.1531` n `231`; crypto_major avg `-0.0392` n `8`; equity avg `-0.0158` n `127`; fx avg `0.0363` n `6`; index avg `-0.0042` n `26`; metal avg `0.008` n `20`; unknown avg `0.2962` n `793`
- 4h: commodity avg `0.1131` n `12`; crypto_alt avg `-0.135` n `231`; crypto_major avg `-0.4002` n `8`; equity avg `-0.1148` n `127`; fx avg `-0.0004` n `6`; index avg `-0.0371` n `26`; metal avg `-0.0215` n `20`; unknown avg `1.2293` n `793`
- 24h: commodity avg `-0.0897` n `12`; crypto_alt avg `-3.693` n `231`; crypto_major avg `-3.9988` n `8`; equity avg `-2.033` n `127`; fx avg `-0.1109` n `6`; index avg `-0.179` n `26`; metal avg `-0.3403` n `20`; unknown avg `-0.5384` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
