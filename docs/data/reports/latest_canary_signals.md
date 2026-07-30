# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T07:52:36.484279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1292` n `12`; crypto_alt avg `-0.0182` n `230`; crypto_major avg `-0.0549` n `8`; equity avg `0.0714` n `102`; fx avg `0.0148` n `6`; index avg `0.0595` n `25`; metal avg `0.0316` n `20`; unknown avg `-0.0002` n `779`
- 1h: commodity avg `-0.1115` n `12`; crypto_alt avg `0.0106` n `230`; crypto_major avg `0.0889` n `8`; equity avg `-0.0914` n `102`; fx avg `0.0273` n `6`; index avg `-0.038` n `25`; metal avg `0.0387` n `20`; unknown avg `-0.1612` n `779`
- 4h: commodity avg `0.2403` n `12`; crypto_alt avg `-0.2577` n `230`; crypto_major avg `-0.2869` n `8`; equity avg `-0.5278` n `102`; fx avg `-0.0521` n `6`; index avg `-0.1987` n `25`; metal avg `-0.1142` n `20`; unknown avg `2.0668` n `747`
- 24h: commodity avg `0.7995` n `12`; crypto_alt avg `-0.4744` n `230`; crypto_major avg `-0.842` n `8`; equity avg `-3.3047` n `102`; fx avg `0.0036` n `6`; index avg `-0.5073` n `25`; metal avg `-0.1243` n `20`; unknown avg `-0.8267` n `745`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
