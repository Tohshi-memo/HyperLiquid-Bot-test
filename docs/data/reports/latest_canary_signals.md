# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T10:07:29.323104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.018` n `13`; crypto_alt avg `0.0431` n `237`; crypto_major avg `0.0127` n `8`; equity avg `0.0139` n `152`; fx avg `0.0045` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0041` n `20`; unknown avg `0.0312` n `1228`
- 1h: commodity avg `0.0058` n `13`; crypto_alt avg `0.0896` n `237`; crypto_major avg `-0.1454` n `8`; equity avg `-0.0333` n `152`; fx avg `0.016` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0217` n `20`; unknown avg `1.5053` n `1216`
- 4h: commodity avg `0.0219` n `13`; crypto_alt avg `-0.6271` n `237`; crypto_major avg `-0.8012` n `8`; equity avg `-0.2789` n `152`; fx avg `0.0112` n `6`; index avg `-0.0255` n `26`; metal avg `-0.0376` n `20`; unknown avg `0.1597` n `1196`
- 24h: commodity avg `0.1471` n `13`; crypto_alt avg `-2.6118` n `237`; crypto_major avg `-2.278` n `8`; equity avg `-0.8056` n `152`; fx avg `0.0075` n `6`; index avg `-0.0147` n `26`; metal avg `-0.1476` n `20`; unknown avg `193.6205` n `1053`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
