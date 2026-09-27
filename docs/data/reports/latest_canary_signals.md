# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T22:37:26.720536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0353` n `12`; crypto_alt avg `-0.2101` n `234`; crypto_major avg `-0.368` n `8`; equity avg `-0.0997` n `141`; fx avg `0.0018` n `6`; index avg `-0.0099` n `26`; metal avg `-0.0408` n `20`; unknown avg `0.4645` n `942`
- 1h: commodity avg `-0.3048` n `12`; crypto_alt avg `-0.4182` n `234`; crypto_major avg `-0.4725` n `8`; equity avg `-0.3844` n `141`; fx avg `0.0301` n `6`; index avg `-0.1126` n `26`; metal avg `-0.1753` n `20`; unknown avg `1.8021` n `926`
- 4h: commodity avg `-0.277` n `12`; crypto_alt avg `-0.8091` n `234`; crypto_major avg `-1.0125` n `8`; equity avg `-0.3684` n `141`; fx avg `-0.0099` n `6`; index avg `-0.0999` n `26`; metal avg `-0.1725` n `20`; unknown avg `2.0463` n `860`
- 24h: commodity avg `-0.4408` n `12`; crypto_alt avg `0.2909` n `234`; crypto_major avg `-0.379` n `8`; equity avg `-0.005` n `141`; fx avg `-0.0105` n `6`; index avg `-0.0569` n `26`; metal avg `-0.1865` n `20`; unknown avg `5.2886` n `827`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
