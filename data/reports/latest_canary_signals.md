# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T14:22:30.438960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0999` n `12`; crypto_alt avg `-0.3483` n `229`; crypto_major avg `-0.475` n `8`; equity avg `0.0054` n `88`; fx avg `0.0015` n `6`; index avg `0.032` n `25`; metal avg `0.0439` n `20`; unknown avg `0.0206` n `765`
- 1h: commodity avg `0.0022` n `12`; crypto_alt avg `-0.3757` n `229`; crypto_major avg `-0.4229` n `8`; equity avg `-0.0785` n `88`; fx avg `-0.0208` n `6`; index avg `0.0235` n `25`; metal avg `0.0329` n `20`; unknown avg `-0.1586` n `765`
- 4h: commodity avg `0.0601` n `12`; crypto_alt avg `0.531` n `229`; crypto_major avg `0.3518` n `8`; equity avg `-0.1062` n `88`; fx avg `-0.0159` n `6`; index avg `0.0389` n `25`; metal avg `-0.1518` n `20`; unknown avg `1.177` n `765`
- 24h: commodity avg `0.4683` n `12`; crypto_alt avg `1.761` n `229`; crypto_major avg `1.3879` n `8`; equity avg `-0.5542` n `88`; fx avg `-0.1187` n `6`; index avg `0.1416` n `25`; metal avg `0.5133` n `20`; unknown avg `6.6801` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
