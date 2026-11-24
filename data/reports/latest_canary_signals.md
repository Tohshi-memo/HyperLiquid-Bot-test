# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T22:52:30.467596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0222` n `13`; crypto_alt avg `-0.0208` n `239`; crypto_major avg `0.051` n `8`; equity avg `-0.1712` n `168`; fx avg `0.0078` n `6`; index avg `-0.0093` n `27`; metal avg `-0.0129` n `20`; unknown avg `0.0004` n `1233`
- 1h: commodity avg `-0.0302` n `13`; crypto_alt avg `0.4492` n `239`; crypto_major avg `0.3455` n `8`; equity avg `0.4001` n `168`; fx avg `0.0047` n `6`; index avg `0.0179` n `27`; metal avg `0.0323` n `20`; unknown avg `-0.2247` n `1219`
- 4h: commodity avg `-0.1542` n `13`; crypto_alt avg `-0.1764` n `239`; crypto_major avg `0.2385` n `8`; equity avg `0.2674` n `168`; fx avg `-0.0315` n `6`; index avg `-0.0022` n `27`; metal avg `0.0488` n `20`; unknown avg `24.1218` n `1185`
- 24h: commodity avg `0.611` n `13`; crypto_alt avg `-1.886` n `239`; crypto_major avg `-1.7591` n `8`; equity avg `-4.0917` n `167`; fx avg `0.2171` n `6`; index avg `-0.3122` n `27`; metal avg `-1.0623` n `20`; unknown avg `439.1412` n `1079`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
