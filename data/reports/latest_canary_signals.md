# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T04:07:25.998344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0257` n `12`; crypto_alt avg `-0.128` n `232`; crypto_major avg `-0.1108` n `8`; equity avg `-0.0099` n `133`; fx avg `-0.0003` n `6`; index avg `0.0048` n `26`; metal avg `-0.0121` n `20`; unknown avg `0.0453` n `791`
- 1h: commodity avg `0.0625` n `12`; crypto_alt avg `-0.4309` n `232`; crypto_major avg `-0.2455` n `8`; equity avg `-0.0096` n `133`; fx avg `0.0108` n `6`; index avg `0.0071` n `26`; metal avg `-0.0498` n `20`; unknown avg `0.0897` n `791`
- 4h: commodity avg `0.0376` n `12`; crypto_alt avg `-0.3636` n `232`; crypto_major avg `-0.1506` n `8`; equity avg `0.1822` n `133`; fx avg `0.0889` n `6`; index avg `0.0434` n `26`; metal avg `-0.1625` n `20`; unknown avg `0.7026` n `784`
- 24h: commodity avg `-0.1184` n `12`; crypto_alt avg `2.5753` n `232`; crypto_major avg `3.9847` n `8`; equity avg `1.2345` n `133`; fx avg `-0.0946` n `6`; index avg `0.1906` n `26`; metal avg `0.4022` n `20`; unknown avg `1.0524` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
