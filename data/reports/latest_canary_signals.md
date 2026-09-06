# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T20:52:25.435190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0262` n `12`; crypto_alt avg `0.0232` n `232`; crypto_major avg `0.1358` n `8`; equity avg `-0.0135` n `134`; fx avg `0.0035` n `6`; index avg `0.0001` n `26`; metal avg `0.0021` n `20`; unknown avg `144.743` n `793`
- 1h: commodity avg `-0.0064` n `12`; crypto_alt avg `0.3116` n `232`; crypto_major avg `0.4205` n `8`; equity avg `-0.0275` n `134`; fx avg `0.0026` n `6`; index avg `0.0045` n `26`; metal avg `0.0146` n `20`; unknown avg `-0.1276` n `775`
- 4h: commodity avg `-0.047` n `12`; crypto_alt avg `0.2053` n `232`; crypto_major avg `0.3301` n `8`; equity avg `0.1708` n `134`; fx avg `-0.0052` n `6`; index avg `0.0263` n `26`; metal avg `0.0397` n `20`; unknown avg `0.2092` n `755`
- 24h: commodity avg `0.0098` n `12`; crypto_alt avg `1.3384` n `232`; crypto_major avg `0.4689` n `8`; equity avg `0.3588` n `134`; fx avg `0.0082` n `6`; index avg `0.0161` n `26`; metal avg `-0.0122` n `20`; unknown avg `134.5691` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
