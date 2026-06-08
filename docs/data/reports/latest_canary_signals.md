# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T20:22:26.361706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0444` n `12`; crypto_alt avg `-0.254` n `228`; crypto_major avg `-0.2364` n `8`; equity avg `-0.1136` n `74`; fx avg `-0.0027` n `6`; index avg `0.1135` n `23`; metal avg `-0.1232` n `18`; unknown avg `-0.0471` n `517`
- 1h: commodity avg `0.0725` n `12`; crypto_alt avg `-0.7577` n `228`; crypto_major avg `-0.5956` n `8`; equity avg `0.0778` n `74`; fx avg `0.0074` n `6`; index avg `0.162` n `23`; metal avg `-0.0895` n `18`; unknown avg `-0.0942` n `517`
- 4h: commodity avg `-0.0303` n `12`; crypto_alt avg `-0.717` n `228`; crypto_major avg `-0.6946` n `8`; equity avg `-0.7804` n `74`; fx avg `-0.0206` n `6`; index avg `-0.3909` n `23`; metal avg `-0.3332` n `18`; unknown avg `-0.1419` n `517`
- 24h: commodity avg `-0.7115` n `12`; crypto_alt avg `2.9591` n `228`; crypto_major avg `3.359` n `8`; equity avg `2.4615` n `74`; fx avg `-0.3067` n `6`; index avg `0.9952` n `23`; metal avg `-0.0416` n `18`; unknown avg `-2.0017` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
