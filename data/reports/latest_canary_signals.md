# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T14:37:38.507099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0413` n `13`; crypto_alt avg `0.0496` n `239`; crypto_major avg `-0.145` n `8`; equity avg `-0.4048` n `166`; fx avg `-0.002` n `6`; index avg `-0.0267` n `27`; metal avg `0.0518` n `20`; unknown avg `147.1915` n `1267`
- 1h: commodity avg `0.1702` n `13`; crypto_alt avg `0.2605` n `239`; crypto_major avg `0.0142` n `8`; equity avg `-0.1888` n `166`; fx avg `0.0233` n `6`; index avg `0.0079` n `27`; metal avg `0.0397` n `20`; unknown avg `267.5118` n `1251`
- 4h: commodity avg `0.3316` n `13`; crypto_alt avg `-0.591` n `239`; crypto_major avg `-0.0941` n `8`; equity avg `-0.6328` n `166`; fx avg `0.0838` n `6`; index avg `-0.0944` n `27`; metal avg `0.086` n `20`; unknown avg `218.2934` n `1246`
- 24h: commodity avg `-0.0042` n `13`; crypto_alt avg `-5.5878` n `239`; crypto_major avg `-6.4818` n `8`; equity avg `-4.0878` n `166`; fx avg `0.1182` n `6`; index avg `-0.2769` n `27`; metal avg `-0.8888` n `20`; unknown avg `20.2409` n `1136`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
