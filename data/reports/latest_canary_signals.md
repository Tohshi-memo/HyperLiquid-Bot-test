# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T11:22:28.062952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0215` n `12`; crypto_alt avg `0.0283` n `232`; crypto_major avg `0.0444` n `8`; equity avg `0.0525` n `133`; fx avg `-0.0012` n `6`; index avg `-0.0026` n `26`; metal avg `0.0015` n `20`; unknown avg `-0.1312` n `793`
- 1h: commodity avg `-0.0282` n `12`; crypto_alt avg `0.4289` n `232`; crypto_major avg `0.4483` n `8`; equity avg `0.0654` n `133`; fx avg `0.0027` n `6`; index avg `0.0062` n `26`; metal avg `0.0254` n `20`; unknown avg `-0.0298` n `791`
- 4h: commodity avg `-0.1403` n `12`; crypto_alt avg `0.8813` n `232`; crypto_major avg `0.5018` n `8`; equity avg `0.4265` n `133`; fx avg `-0.0182` n `6`; index avg `0.0421` n `26`; metal avg `0.0112` n `20`; unknown avg `-0.0597` n `785`
- 24h: commodity avg `-0.4746` n `12`; crypto_alt avg `2.7599` n `232`; crypto_major avg `4.211` n `8`; equity avg `2.2175` n `133`; fx avg `0.027` n `6`; index avg `0.4088` n `26`; metal avg `0.4819` n `20`; unknown avg `1.9387` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
