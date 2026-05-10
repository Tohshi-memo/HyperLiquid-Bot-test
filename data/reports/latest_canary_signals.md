# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T14:13:12.747201+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `12`; crypto_alt avg `0.0626` n `228`; crypto_major avg `0.0866` n `8`; equity avg `-0.0705` n `65`; fx avg `-0.0019` n `5`; index avg `0.0095` n `23`; metal avg `-0.0174` n `18`; unknown avg `0.0811` n `376`
- 1h: commodity avg `-0.0296` n `12`; crypto_alt avg `0.3765` n `228`; crypto_major avg `0.4132` n `8`; equity avg `-0.0159` n `65`; fx avg `-0.0019` n `5`; index avg `0.0249` n `23`; metal avg `0.0698` n `18`; unknown avg `-0.1457` n `376`
- 4h: commodity avg `-0.0579` n `12`; crypto_alt avg `0.6495` n `228`; crypto_major avg `0.2666` n `8`; equity avg `0.0752` n `65`; fx avg `-0.0121` n `5`; index avg `-0.0001` n `23`; metal avg `0.2288` n `18`; unknown avg `-0.3492` n `376`
- 24h: commodity avg `-0.0912` n `12`; crypto_alt avg `0.7545` n `228`; crypto_major avg `0.2502` n `8`; equity avg `0.9124` n `65`; fx avg `-0.0288` n `5`; index avg `0.2605` n `23`; metal avg `0.6466` n `18`; unknown avg `0.326` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
