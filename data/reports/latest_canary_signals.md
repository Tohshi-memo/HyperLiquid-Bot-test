# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T05:07:27.632583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `0.0972` n `232`; crypto_major avg `0.0713` n `8`; equity avg `-0.0004` n `134`; fx avg `-0.0023` n `6`; index avg `0.0096` n `26`; metal avg `-0.0009` n `20`; unknown avg `-0.056` n `782`
- 1h: commodity avg `-0.0337` n `12`; crypto_alt avg `-0.1013` n `232`; crypto_major avg `0.0542` n `8`; equity avg `-0.0091` n `134`; fx avg `0.0134` n `6`; index avg `-0.0037` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.3846` n `776`
- 4h: commodity avg `-0.0508` n `12`; crypto_alt avg `0.057` n `232`; crypto_major avg `0.456` n `8`; equity avg `0.0269` n `134`; fx avg `0.0209` n `6`; index avg `0.0028` n `26`; metal avg `-0.0076` n `20`; unknown avg `1.8091` n `744`
- 24h: commodity avg `0.1018` n `12`; crypto_alt avg `3.1556` n `232`; crypto_major avg `3.2462` n `8`; equity avg `0.3453` n `134`; fx avg `-0.053` n `6`; index avg `0.0786` n `26`; metal avg `0.0317` n `20`; unknown avg `1.6781` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
