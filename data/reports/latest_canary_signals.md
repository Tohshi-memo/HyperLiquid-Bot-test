# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T12:37:28.054574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.038` n `12`; crypto_alt avg `0.0539` n `232`; crypto_major avg `0.0313` n `8`; equity avg `-0.0195` n `134`; fx avg `-0.0266` n `6`; index avg `0.0071` n `26`; metal avg `0.0411` n `20`; unknown avg `0.4729` n `790`
- 1h: commodity avg `-0.0385` n `12`; crypto_alt avg `0.4395` n `232`; crypto_major avg `0.2951` n `8`; equity avg `-0.0284` n `134`; fx avg `-0.0276` n `6`; index avg `0.0019` n `26`; metal avg `0.0755` n `20`; unknown avg `6685.1716` n `748`
- 4h: commodity avg `0.3467` n `12`; crypto_alt avg `0.9976` n `232`; crypto_major avg `0.5318` n `8`; equity avg `-0.1161` n `134`; fx avg `0.0461` n `6`; index avg `-0.056` n `26`; metal avg `-0.1527` n `20`; unknown avg `6720.7887` n `744`
- 24h: commodity avg `0.2056` n `12`; crypto_alt avg `0.4744` n `232`; crypto_major avg `-0.7065` n `8`; equity avg `0.1068` n `134`; fx avg `-0.1007` n `6`; index avg `-0.0254` n `26`; metal avg `-0.1515` n `20`; unknown avg `217.012` n `616`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
