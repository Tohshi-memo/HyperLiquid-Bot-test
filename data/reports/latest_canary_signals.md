# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T19:52:24.979502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0743` n `12`; crypto_alt avg `0.1205` n `230`; crypto_major avg `0.1845` n `8`; equity avg `0.0097` n `92`; fx avg `0.0081` n `6`; index avg `0.0002` n `25`; metal avg `0.0046` n `20`; unknown avg `-0.0935` n `765`
- 1h: commodity avg `0.009` n `12`; crypto_alt avg `0.1687` n `230`; crypto_major avg `0.0779` n `8`; equity avg `0.0737` n `92`; fx avg `0.0138` n `6`; index avg `0.018` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.0999` n `765`
- 4h: commodity avg `0.1565` n `12`; crypto_alt avg `-0.0481` n `230`; crypto_major avg `0.0837` n `8`; equity avg `0.0493` n `92`; fx avg `-0.0097` n `6`; index avg `-0.0013` n `25`; metal avg `-0.0121` n `20`; unknown avg `-0.2182` n `759`
- 24h: commodity avg `0.6168` n `12`; crypto_alt avg `-1.2709` n `230`; crypto_major avg `-0.3951` n `8`; equity avg `-0.1708` n `92`; fx avg `0.0103` n `6`; index avg `-0.0936` n `25`; metal avg `-0.1002` n `20`; unknown avg `0.1754` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
