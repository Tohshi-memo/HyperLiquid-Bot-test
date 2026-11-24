# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T10:22:31.321797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `13`; crypto_alt avg `0.1384` n `239`; crypto_major avg `-0.0118` n `8`; equity avg `0.0588` n `166`; fx avg `-0.0162` n `6`; index avg `0.0071` n `27`; metal avg `-0.0214` n `20`; unknown avg `0.3296` n `1248`
- 1h: commodity avg `0.0865` n `13`; crypto_alt avg `-0.0732` n `239`; crypto_major avg `0.1123` n `8`; equity avg `-0.2229` n `166`; fx avg `0.0532` n `6`; index avg `-0.0275` n `27`; metal avg `0.0082` n `20`; unknown avg `1.336` n `1218`
- 4h: commodity avg `0.282` n `13`; crypto_alt avg `-1.5777` n `239`; crypto_major avg `-1.0247` n `8`; equity avg `-1.7053` n `166`; fx avg `0.0975` n `6`; index avg `-0.2002` n `27`; metal avg `-0.1654` n `20`; unknown avg `0.0594` n `1200`
- 24h: commodity avg `-0.6139` n `13`; crypto_alt avg `-0.9398` n `239`; crypto_major avg `-1.116` n `8`; equity avg `1.331` n `166`; fx avg `-0.0993` n `6`; index avg `0.3333` n `27`; metal avg `-0.4388` n `20`; unknown avg `1.059` n `1140`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
