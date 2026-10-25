# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T11:37:25.635779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.026` n `13`; crypto_alt avg `-0.2797` n `237`; crypto_major avg `-0.1771` n `8`; equity avg `-0.0654` n `152`; fx avg `-0.0121` n `6`; index avg `0.0062` n `26`; metal avg `-0.0033` n `20`; unknown avg `3.1632` n `1231`
- 1h: commodity avg `0.0123` n `13`; crypto_alt avg `-0.0597` n `237`; crypto_major avg `0.1172` n `8`; equity avg `0.0292` n `152`; fx avg `0.0065` n `6`; index avg `0.0107` n `26`; metal avg `0.0091` n `20`; unknown avg `3.9777` n `1229`
- 4h: commodity avg `-0.0773` n `13`; crypto_alt avg `-0.7663` n `237`; crypto_major avg `-0.5539` n `8`; equity avg `-0.09` n `152`; fx avg `0.0087` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0041` n `20`; unknown avg `16.7707` n `1181`
- 24h: commodity avg `-0.0096` n `13`; crypto_alt avg `-1.8228` n `237`; crypto_major avg `-0.1643` n `8`; equity avg `0.0117` n `152`; fx avg `-0.004` n `6`; index avg `0.0368` n `26`; metal avg `-0.0298` n `20`; unknown avg `18.693` n `1048`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1998`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
