# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T09:22:24.025048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `-0.1347` n `230`; crypto_major avg `0.0055` n `8`; equity avg `-0.1625` n `107`; fx avg `0.0052` n `6`; index avg `-0.002` n `25`; metal avg `0.0016` n `20`; unknown avg `0.055` n `781`
- 1h: commodity avg `0.2087` n `12`; crypto_alt avg `-0.158` n `230`; crypto_major avg `-0.1044` n `8`; equity avg `-0.6917` n `107`; fx avg `0.0205` n `6`; index avg `-0.1158` n `25`; metal avg `-0.1322` n `20`; unknown avg `0.0424` n `781`
- 4h: commodity avg `0.1046` n `12`; crypto_alt avg `-0.2726` n `230`; crypto_major avg `-0.2963` n `8`; equity avg `0.5002` n `107`; fx avg `0.098` n `6`; index avg `0.0643` n `25`; metal avg `0.0031` n `20`; unknown avg `0.9104` n `765`
- 24h: commodity avg `0.4163` n `12`; crypto_alt avg `0.9329` n `230`; crypto_major avg `1.1245` n `8`; equity avg `2.7742` n `107`; fx avg `0.0962` n `6`; index avg `0.2557` n `25`; metal avg `0.0646` n `20`; unknown avg `1.0887` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
