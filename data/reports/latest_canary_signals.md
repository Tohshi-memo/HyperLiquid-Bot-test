# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T21:37:28.246925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0231` n `12`; crypto_alt avg `0.0946` n `231`; crypto_major avg `0.1899` n `8`; equity avg `-0.0017` n `127`; fx avg `0.0073` n `6`; index avg `-0.0118` n `26`; metal avg `0.0191` n `20`; unknown avg `0.2836` n `793`
- 1h: commodity avg `0.0344` n `12`; crypto_alt avg `0.0964` n `231`; crypto_major avg `0.1995` n `8`; equity avg `-0.0146` n `127`; fx avg `-0.0109` n `6`; index avg `0.0006` n `26`; metal avg `0.0312` n `20`; unknown avg `0.3419` n `793`
- 4h: commodity avg `0.0563` n `12`; crypto_alt avg `-0.0861` n `231`; crypto_major avg `-0.297` n `8`; equity avg `-0.0918` n `127`; fx avg `-0.0326` n `6`; index avg `-0.0333` n `26`; metal avg `-0.1547` n `20`; unknown avg `1.1143` n `793`
- 24h: commodity avg `-0.081` n `12`; crypto_alt avg `-3.1006` n `231`; crypto_major avg `-3.3467` n `8`; equity avg `-2.1142` n `127`; fx avg `-0.1374` n `6`; index avg `-0.1967` n `26`; metal avg `-0.3436` n `20`; unknown avg `-0.5648` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
