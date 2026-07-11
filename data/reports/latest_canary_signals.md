# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T15:52:28.950037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `12`; crypto_alt avg `0.0036` n `230`; crypto_major avg `-0.0925` n `8`; equity avg `-0.0279` n `92`; fx avg `-0.0051` n `6`; index avg `-0.0053` n `25`; metal avg `0.002` n `20`; unknown avg `0.1812` n `765`
- 1h: commodity avg `-0.0143` n `12`; crypto_alt avg `-0.248` n `230`; crypto_major avg `-0.2432` n `8`; equity avg `-0.0689` n `92`; fx avg `-0.0089` n `6`; index avg `0.003` n `25`; metal avg `-0.0346` n `20`; unknown avg `0.382` n `765`
- 4h: commodity avg `-0.0391` n `12`; crypto_alt avg `0.2488` n `230`; crypto_major avg `0.2942` n `8`; equity avg `-0.1448` n `92`; fx avg `-0.0181` n `6`; index avg `0.0081` n `25`; metal avg `-0.0229` n `20`; unknown avg `0.3263` n `765`
- 24h: commodity avg `0.2991` n `12`; crypto_alt avg `1.0012` n `229`; crypto_major avg `0.6348` n `8`; equity avg `0.3708` n `92`; fx avg `-0.0382` n `6`; index avg `0.1235` n `25`; metal avg `0.0293` n `20`; unknown avg `3.0118` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
