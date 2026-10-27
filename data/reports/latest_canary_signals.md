# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T17:52:35.129314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `13`; crypto_alt avg `-0.1077` n `238`; crypto_major avg `-0.1218` n `8`; equity avg `-0.0723` n `154`; fx avg `0.0045` n `6`; index avg `-0.0056` n `27`; metal avg `-0.0567` n `20`; unknown avg `1.1358` n `1238`
- 1h: commodity avg `-0.032` n `13`; crypto_alt avg `0.0968` n `238`; crypto_major avg `0.0735` n `8`; equity avg `0.0558` n `154`; fx avg `-0.0019` n `6`; index avg `-0.0024` n `27`; metal avg `-0.0078` n `20`; unknown avg `-0.0457` n `1234`
- 4h: commodity avg `-0.2109` n `13`; crypto_alt avg `1.0039` n `238`; crypto_major avg `0.9543` n `8`; equity avg `1.318` n `154`; fx avg `-0.0214` n `6`; index avg `0.2357` n `27`; metal avg `0.2595` n `20`; unknown avg `0.6606` n `1150`
- 24h: commodity avg `-0.5597` n `13`; crypto_alt avg `0.417` n `237`; crypto_major avg `0.784` n `8`; equity avg `1.339` n `154`; fx avg `-0.0685` n `6`; index avg `0.3888` n `27`; metal avg `0.1031` n `20`; unknown avg `26.2922` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2227`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1984`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
