# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T14:37:28.273955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0159` n `12`; crypto_alt avg `0.0244` n `230`; crypto_major avg `0.0329` n `8`; equity avg `-0.1306` n `109`; fx avg `-0.0035` n `6`; index avg `-0.0049` n `25`; metal avg `0.081` n `20`; unknown avg `0.0042` n `781`
- 1h: commodity avg `-0.0494` n `12`; crypto_alt avg `0.2928` n `230`; crypto_major avg `0.4984` n `8`; equity avg `1.8515` n `109`; fx avg `0.0415` n `6`; index avg `0.2139` n `25`; metal avg `0.0887` n `20`; unknown avg `0.3996` n `781`
- 4h: commodity avg `0.0064` n `12`; crypto_alt avg `0.4237` n `230`; crypto_major avg `0.0967` n `8`; equity avg `1.4574` n `109`; fx avg `0.0548` n `6`; index avg `0.164` n `25`; metal avg `-0.0979` n `20`; unknown avg `0.3062` n `781`
- 24h: commodity avg `0.1812` n `12`; crypto_alt avg `0.4642` n `230`; crypto_major avg `-0.6184` n `8`; equity avg `0.1934` n `109`; fx avg `0.0528` n `6`; index avg `-0.1818` n `25`; metal avg `0.15` n `20`; unknown avg `113.3567` n `749`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
