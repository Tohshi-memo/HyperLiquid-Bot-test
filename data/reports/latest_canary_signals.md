# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T14:22:29.948650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0519` n `13`; crypto_alt avg `0.0787` n `239`; crypto_major avg `0.1105` n `8`; equity avg `0.051` n `166`; fx avg `0.0181` n `6`; index avg `0.011` n `27`; metal avg `0.013` n `20`; unknown avg `158.2411` n `1263`
- 1h: commodity avg `0.2771` n `13`; crypto_alt avg `0.4883` n `239`; crypto_major avg `0.2355` n `8`; equity avg `0.2523` n `166`; fx avg `0.0146` n `6`; index avg `0.0374` n `27`; metal avg `-0.083` n `20`; unknown avg `460.6657` n `1253`
- 4h: commodity avg `0.3048` n `13`; crypto_alt avg `-0.9197` n `239`; crypto_major avg `-0.2061` n `8`; equity avg `-0.5615` n `166`; fx avg `0.0885` n `6`; index avg `-0.1113` n `27`; metal avg `0.0789` n `20`; unknown avg `0.2058` n `1246`
- 24h: commodity avg `-0.0547` n `13`; crypto_alt avg `-5.401` n `239`; crypto_major avg `-6.1951` n `8`; equity avg `-4.0765` n `166`; fx avg `0.095` n `6`; index avg `-0.2841` n `27`; metal avg `-0.9457` n `20`; unknown avg `0.1706` n `1140`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
