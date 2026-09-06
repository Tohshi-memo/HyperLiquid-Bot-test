# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T07:07:24.820114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `-0.088` n `232`; crypto_major avg `-0.0037` n `8`; equity avg `-0.0107` n `134`; fx avg `0.0009` n `6`; index avg `0.002` n `26`; metal avg `0.0024` n `20`; unknown avg `-0.0305` n `790`
- 1h: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.1559` n `232`; crypto_major avg `-0.219` n `8`; equity avg `0.0213` n `134`; fx avg `0.001` n `6`; index avg `-0.0071` n `26`; metal avg `-0.0039` n `20`; unknown avg `-0.0212` n `788`
- 4h: commodity avg `0.0222` n `12`; crypto_alt avg `-0.0014` n `232`; crypto_major avg `0.251` n `8`; equity avg `0.1038` n `134`; fx avg `0.0077` n `6`; index avg `0.0204` n `26`; metal avg `0.0145` n `20`; unknown avg `462.8744` n `728`
- 24h: commodity avg `0.1309` n `12`; crypto_alt avg `1.9074` n `232`; crypto_major avg `2.5226` n `8`; equity avg `0.4421` n `134`; fx avg `-0.0396` n `6`; index avg `0.0719` n `26`; metal avg `0.0197` n `20`; unknown avg `493.3828` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
