# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T19:51:19.800244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3638` n `12`; crypto_alt avg `-0.067` n `228`; crypto_major avg `-0.1449` n `8`; equity avg `0.032` n `74`; fx avg `-0.0109` n `6`; index avg `0.0007` n `23`; metal avg `0.0023` n `18`; unknown avg `2.1442` n `515`
- 1h: commodity avg `0.0895` n `12`; crypto_alt avg `0.0818` n `228`; crypto_major avg `-0.1645` n `8`; equity avg `0.1511` n `74`; fx avg `-0.0407` n `6`; index avg `0.0116` n `23`; metal avg `0.0049` n `18`; unknown avg `-0.0293` n `515`
- 4h: commodity avg `0.3019` n `12`; crypto_alt avg `-0.5209` n `228`; crypto_major avg `-1.0588` n `8`; equity avg `0.1175` n `74`; fx avg `0.0678` n `6`; index avg `-0.1141` n `23`; metal avg `0.1116` n `18`; unknown avg `-1.4168` n `515`
- 24h: commodity avg `0.6019` n `12`; crypto_alt avg `-1.1862` n `228`; crypto_major avg `-1.2966` n `8`; equity avg `-1.2922` n `74`; fx avg `0.0567` n `6`; index avg `-0.275` n `23`; metal avg `-0.5716` n `18`; unknown avg `-0.5146` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
