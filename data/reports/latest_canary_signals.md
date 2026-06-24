# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T02:22:26.593189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `-4.348` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-4.3437` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0156` n `12`; crypto_alt avg `-0.0633` n `228`; crypto_major avg `-0.1987` n `8`; equity avg `-0.0111` n `86`; fx avg `0.0147` n `6`; index avg `-0.0182` n `23`; metal avg `-0.0947` n `20`; unknown avg `-0.1361` n `764`
- 1h: commodity avg `-0.0286` n `12`; crypto_alt avg `-0.071` n `228`; crypto_major avg `-0.1921` n `8`; equity avg `4.1559` n `86`; fx avg `0.0155` n `6`; index avg `0.0377` n `23`; metal avg `-0.0318` n `20`; unknown avg `-0.135` n `764`
- 4h: commodity avg `-0.0575` n `12`; crypto_alt avg `-0.3157` n `228`; crypto_major avg `0.0382` n `8`; equity avg `4.3819` n `86`; fx avg `0.0591` n `6`; index avg `0.0817` n `23`; metal avg `-0.1961` n `20`; unknown avg `-0.4018` n `756`
- 24h: commodity avg `-0.4601` n `12`; crypto_alt avg `-2.1805` n `228`; crypto_major avg `-2.9273` n `8`; equity avg `2.7406` n `86`; fx avg `-0.1144` n `6`; index avg `-0.4228` n `23`; metal avg `-1.0065` n `20`; unknown avg `0.1085` n `588`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
