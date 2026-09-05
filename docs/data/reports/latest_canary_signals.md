# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T18:37:23.783855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `0.0102` n `232`; crypto_major avg `-0.0587` n `8`; equity avg `-0.0053` n `134`; fx avg `-0.0066` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.0856` n `794`
- 1h: commodity avg `0.0357` n `12`; crypto_alt avg `0.1765` n `232`; crypto_major avg `0.4904` n `8`; equity avg `0.0015` n `134`; fx avg `-0.0111` n `6`; index avg `-0.0064` n `26`; metal avg `0.0073` n `20`; unknown avg `0.0588` n `792`
- 4h: commodity avg `0.0543` n `12`; crypto_alt avg `0.4425` n `232`; crypto_major avg `1.1738` n `8`; equity avg `0.1257` n `134`; fx avg `-0.0324` n `6`; index avg `0.0285` n `26`; metal avg `0.0397` n `20`; unknown avg `-0.5734` n `786`
- 24h: commodity avg `-0.0678` n `12`; crypto_alt avg `2.8953` n `232`; crypto_major avg `3.0064` n `8`; equity avg `0.5003` n `134`; fx avg `-0.0361` n `6`; index avg `0.0569` n `26`; metal avg `0.1581` n `20`; unknown avg `0.0562` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
