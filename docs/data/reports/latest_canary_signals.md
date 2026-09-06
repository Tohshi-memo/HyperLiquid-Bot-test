# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T09:07:27.020875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `0.1882` n `232`; crypto_major avg `0.1068` n `8`; equity avg `0.0135` n `134`; fx avg `-0.017` n `6`; index avg `0.0022` n `26`; metal avg `0.0042` n `20`; unknown avg `329.0508` n `792`
- 1h: commodity avg `0.0179` n `12`; crypto_alt avg `0.0664` n `232`; crypto_major avg `0.0243` n `8`; equity avg `0.0185` n `134`; fx avg `-0.0265` n `6`; index avg `0.0037` n `26`; metal avg `0.0066` n `20`; unknown avg `331.641` n `786`
- 4h: commodity avg `0.0386` n `12`; crypto_alt avg `-0.2095` n `232`; crypto_major avg `-0.2351` n `8`; equity avg `0.0768` n `134`; fx avg `-0.0007` n `6`; index avg `0.0034` n `26`; metal avg `-0.0051` n `20`; unknown avg `-0.2665` n `764`
- 24h: commodity avg `0.1543` n `12`; crypto_alt avg `1.629` n `232`; crypto_major avg `1.7591` n `8`; equity avg `0.4234` n `134`; fx avg `-0.0443` n `6`; index avg `0.0904` n `26`; metal avg `0.0126` n `20`; unknown avg `493.2064` n `676`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
