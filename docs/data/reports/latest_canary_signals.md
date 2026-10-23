# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T23:28:21.573502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.066` n `13`; crypto_alt avg `0.6675` n `237`; crypto_major avg `0.3503` n `8`; equity avg `0.1238` n `152`; fx avg `-0.0257` n `6`; index avg `0.0127` n `26`; metal avg `0.0335` n `20`; unknown avg `1.9138` n `1230`
- 1h: commodity avg `0.0087` n `13`; crypto_alt avg `-1.2098` n `237`; crypto_major avg `-0.7405` n `8`; equity avg `-0.2405` n `152`; fx avg `-0.0357` n `6`; index avg `-0.0424` n `26`; metal avg `-0.0417` n `20`; unknown avg `1.9886` n `1228`
- 4h: commodity avg `0.1499` n `13`; crypto_alt avg `-1.4067` n `237`; crypto_major avg `-0.5573` n `8`; equity avg `-0.3091` n `152`; fx avg `0.0015` n `6`; index avg `-0.0261` n `26`; metal avg `-0.0681` n `20`; unknown avg `109.7701` n `1134`
- 24h: commodity avg `0.507` n `13`; crypto_alt avg `-0.786` n `237`; crypto_major avg `-0.3006` n `8`; equity avg `1.2915` n `152`; fx avg `-0.0633` n `6`; index avg `0.0681` n `26`; metal avg `-0.1945` n `20`; unknown avg `199.6035` n `1024`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2033`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
