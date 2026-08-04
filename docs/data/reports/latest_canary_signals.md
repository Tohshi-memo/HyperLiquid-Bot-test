# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T14:52:37.613545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0291` n `12`; crypto_alt avg `0.1383` n `230`; crypto_major avg `0.1965` n `8`; equity avg `0.1872` n `107`; fx avg `0.0017` n `6`; index avg `0.0007` n `25`; metal avg `0.1035` n `20`; unknown avg `0.0107` n `782`
- 1h: commodity avg `0.1065` n `12`; crypto_alt avg `-0.0817` n `230`; crypto_major avg `0.2296` n `8`; equity avg `0.2914` n `107`; fx avg `0.0366` n `6`; index avg `0.0245` n `25`; metal avg `-0.0001` n `20`; unknown avg `0.0523` n `782`
- 4h: commodity avg `-1.0169` n `12`; crypto_alt avg `-0.3706` n `230`; crypto_major avg `0.159` n `8`; equity avg `1.1996` n `107`; fx avg `-0.0555` n `6`; index avg `0.3248` n `25`; metal avg `0.4906` n `20`; unknown avg `-0.2187` n `781`
- 24h: commodity avg `-0.916` n `12`; crypto_alt avg `-0.0885` n `230`; crypto_major avg `0.4689` n `8`; equity avg `3.451` n `107`; fx avg `0.0983` n `6`; index avg `0.6539` n `25`; metal avg `1.0994` n `20`; unknown avg `0.5788` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
