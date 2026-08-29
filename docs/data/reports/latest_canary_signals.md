# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T00:37:24.622516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.33` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0123` n `12`; crypto_alt avg `-0.118` n `231`; crypto_major avg `-0.1968` n `8`; equity avg `-0.0113` n `127`; fx avg `-0.0006` n `6`; index avg `-0.0127` n `26`; metal avg `-0.0119` n `20`; unknown avg `-0.1106` n `793`
- 1h: commodity avg `-0.0335` n `12`; crypto_alt avg `0.1385` n `231`; crypto_major avg `0.0208` n `8`; equity avg `0.0477` n `127`; fx avg `-0.0077` n `6`; index avg `0.0034` n `26`; metal avg `0.0093` n `20`; unknown avg `-0.1751` n `793`
- 4h: commodity avg `-0.0428` n `12`; crypto_alt avg `0.6617` n `231`; crypto_major avg `0.4301` n `8`; equity avg `0.0479` n `127`; fx avg `-0.009` n `6`; index avg `0.0029` n `26`; metal avg `0.0761` n `20`; unknown avg `0.2376` n `793`
- 24h: commodity avg `-0.1516` n `12`; crypto_alt avg `-3.1835` n `231`; crypto_major avg `-3.5225` n `8`; equity avg `-2.0846` n `127`; fx avg `-0.1045` n `6`; index avg `-0.2286` n `26`; metal avg `-0.2305` n `20`; unknown avg `-0.7018` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
