# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T22:04:16.623991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0996` n `12`; crypto_alt avg `-0.4753` n `230`; crypto_major avg `-0.4149` n `8`; equity avg `-0.1347` n `92`; fx avg `-0.0259` n `6`; index avg `-0.0463` n `25`; metal avg `-0.0997` n `20`; unknown avg `0.1461` n `765`
- 1h: commodity avg `-0.1698` n `12`; crypto_alt avg `-0.8549` n `230`; crypto_major avg `-0.8167` n `8`; equity avg `-0.1546` n `92`; fx avg `-0.0148` n `6`; index avg `-0.0519` n `25`; metal avg `-0.1258` n `20`; unknown avg `0.5032` n `765`
- 4h: commodity avg `-0.1247` n `12`; crypto_alt avg `-0.7199` n `230`; crypto_major avg `-0.6879` n `8`; equity avg `-0.0722` n `92`; fx avg `-0.0628` n `6`; index avg `-0.0495` n `25`; metal avg `-0.125` n `20`; unknown avg `0.1824` n `765`
- 24h: commodity avg `0.4593` n `12`; crypto_alt avg `-2.0198` n `230`; crypto_major avg `-1.3853` n `8`; equity avg `-0.3969` n `92`; fx avg `-0.0595` n `6`; index avg `-0.1519` n `25`; metal avg `-0.2159` n `20`; unknown avg `0.2298` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
