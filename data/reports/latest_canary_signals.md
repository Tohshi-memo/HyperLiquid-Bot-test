# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T19:52:26.592336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `-0.0841` n `229`; crypto_major avg `-0.0028` n `8`; equity avg `-0.0591` n `88`; fx avg `-0.003` n `6`; index avg `0.0056` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0061` n `765`
- 1h: commodity avg `-0.0318` n `12`; crypto_alt avg `0.1889` n `229`; crypto_major avg `0.2797` n `8`; equity avg `-0.0249` n `88`; fx avg `0.0005` n `6`; index avg `-0.0077` n `25`; metal avg `-0.0062` n `20`; unknown avg `0.1494` n `765`
- 4h: commodity avg `-0.0065` n `12`; crypto_alt avg `0.4149` n `229`; crypto_major avg `0.8166` n `8`; equity avg `0.1182` n `88`; fx avg `-0.0152` n `6`; index avg `0.0484` n `25`; metal avg `0.0384` n `20`; unknown avg `1.0847` n `765`
- 24h: commodity avg `0.1376` n `12`; crypto_alt avg `2.8275` n `229`; crypto_major avg `2.7724` n `8`; equity avg `1.9132` n `88`; fx avg `-0.042` n `6`; index avg `0.4918` n `25`; metal avg `0.5704` n `20`; unknown avg `8.0661` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
