# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T11:27:54.789903+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `0.1608` n `230`; crypto_major avg `0.0629` n `8`; equity avg `0.0728` n `112`; fx avg `0.0161` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0976` n `20`; unknown avg `0.0404` n `782`
- 1h: commodity avg `-0.0897` n `12`; crypto_alt avg `0.0797` n `230`; crypto_major avg `0.1761` n `8`; equity avg `0.2742` n `112`; fx avg `0.0119` n `6`; index avg `0.0392` n `25`; metal avg `-0.0493` n `20`; unknown avg `-0.0219` n `782`
- 4h: commodity avg `-0.3154` n `12`; crypto_alt avg `0.2088` n `230`; crypto_major avg `0.8526` n `8`; equity avg `0.6228` n `112`; fx avg `-0.0221` n `6`; index avg `0.051` n `25`; metal avg `0.0532` n `20`; unknown avg `0.1746` n `782`
- 24h: commodity avg `0.1569` n `12`; crypto_alt avg `0.7323` n `230`; crypto_major avg `0.3509` n `8`; equity avg `2.4636` n `109`; fx avg `-0.0868` n `6`; index avg `0.1112` n `25`; metal avg `0.2653` n `20`; unknown avg `0.3768` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
