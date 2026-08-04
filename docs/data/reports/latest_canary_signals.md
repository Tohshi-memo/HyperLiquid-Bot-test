# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T18:37:28.765901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0787` n `12`; crypto_alt avg `-0.0552` n `230`; crypto_major avg `-0.0589` n `8`; equity avg `-0.0871` n `107`; fx avg `0.0111` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0611` n `20`; unknown avg `0.0608` n `782`
- 1h: commodity avg `0.0383` n `12`; crypto_alt avg `0.1426` n `230`; crypto_major avg `0.0547` n `8`; equity avg `-0.0618` n `107`; fx avg `0.0244` n `6`; index avg `0.0382` n `25`; metal avg `-0.1057` n `20`; unknown avg `0.0289` n `782`
- 4h: commodity avg `-0.1306` n `12`; crypto_alt avg `0.5614` n `230`; crypto_major avg `0.4394` n `8`; equity avg `1.3433` n `107`; fx avg `0.0429` n `6`; index avg `0.3069` n `25`; metal avg `0.1559` n `20`; unknown avg `-0.1331` n `782`
- 24h: commodity avg `-1.1784` n `12`; crypto_alt avg `-0.2496` n `230`; crypto_major avg `0.4082` n `8`; equity avg `4.069` n `107`; fx avg `0.1373` n `6`; index avg `0.8619` n `25`; metal avg `1.0765` n `20`; unknown avg `0.5177` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
