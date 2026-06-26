# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T04:22:28.242208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `0.0042` n `228`; crypto_major avg `-0.055` n `8`; equity avg `-0.0115` n `86`; fx avg `-0.0165` n `6`; index avg `-0.0069` n `23`; metal avg `0.0632` n `20`; unknown avg `5.6097` n `765`
- 1h: commodity avg `-0.0086` n `12`; crypto_alt avg `1.3223` n `228`; crypto_major avg `1.4697` n `8`; equity avg `0.4892` n `86`; fx avg `-0.0162` n `6`; index avg `0.0619` n `23`; metal avg `0.1469` n `20`; unknown avg `2.3789` n `749`
- 4h: commodity avg `-0.2099` n `12`; crypto_alt avg `-0.5779` n `228`; crypto_major avg `-0.4473` n `8`; equity avg `-1.6267` n `86`; fx avg `-0.0226` n `6`; index avg `-0.3721` n `23`; metal avg `-0.3304` n `20`; unknown avg `-0.3801` n `749`
- 24h: commodity avg `0.2946` n `12`; crypto_alt avg `-1.3517` n `228`; crypto_major avg `-1.201` n `8`; equity avg `-3.8291` n `86`; fx avg `0.0103` n `6`; index avg `-0.6244` n `23`; metal avg `-0.0385` n `20`; unknown avg `0.6432` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
