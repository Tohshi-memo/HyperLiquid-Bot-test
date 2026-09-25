# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T10:22:31.941268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `0.0896` n `234`; crypto_major avg `0.0648` n `8`; equity avg `0.0896` n `141`; fx avg `-0.0016` n `6`; index avg `0.0139` n `26`; metal avg `0.0928` n `20`; unknown avg `0.1077` n `946`
- 1h: commodity avg `-0.0004` n `12`; crypto_alt avg `0.1005` n `234`; crypto_major avg `-0.0281` n `8`; equity avg `-0.09` n `141`; fx avg `0.0177` n `6`; index avg `-0.0095` n `26`; metal avg `0.1236` n `20`; unknown avg `1.6741` n `944`
- 4h: commodity avg `-0.0461` n `12`; crypto_alt avg `1.1981` n `234`; crypto_major avg `0.7246` n `8`; equity avg `0.1902` n `141`; fx avg `-0.0203` n `6`; index avg `0.0506` n `26`; metal avg `0.2521` n `20`; unknown avg `0.4937` n `926`
- 24h: commodity avg `0.0415` n `12`; crypto_alt avg `5.2759` n `234`; crypto_major avg `3.0363` n `8`; equity avg `2.021` n `141`; fx avg `-0.2089` n `6`; index avg `0.3284` n `26`; metal avg `0.3921` n `20`; unknown avg `13.0133` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
