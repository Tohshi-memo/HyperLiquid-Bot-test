# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T14:07:18.607623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0198` n `12`; crypto_alt avg `0.002` n `228`; crypto_major avg `0.0108` n `8`; equity avg `-0.074` n `65`; fx avg `-0.0019` n `5`; index avg `-0.0111` n `23`; metal avg `0.0015` n `18`; unknown avg `0.03` n `376`
- 1h: commodity avg `-0.0368` n `12`; crypto_alt avg `0.3157` n `228`; crypto_major avg `0.337` n `8`; equity avg `-0.0195` n `65`; fx avg `-0.0019` n `5`; index avg `0.0043` n `23`; metal avg `0.0887` n `18`; unknown avg `-0.1972` n `376`
- 4h: commodity avg `-0.0651` n `12`; crypto_alt avg `0.5885` n `228`; crypto_major avg `0.1906` n `8`; equity avg `0.0718` n `65`; fx avg `-0.0121` n `5`; index avg `-0.0207` n `23`; metal avg `0.2477` n `18`; unknown avg `-0.3985` n `376`
- 24h: commodity avg `-0.0983` n `12`; crypto_alt avg `0.6945` n `228`; crypto_major avg `0.1744` n `8`; equity avg `0.9096` n `65`; fx avg `-0.0288` n `5`; index avg `0.2398` n `23`; metal avg `0.6657` n `18`; unknown avg `0.3073` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
