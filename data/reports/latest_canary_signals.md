# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T11:21:07.679092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `12`; crypto_alt avg `-0.1441` n `228`; crypto_major avg `-0.038` n `8`; equity avg `0.0202` n `74`; fx avg `0.0148` n `6`; index avg `0.0205` n `23`; metal avg `-0.0026` n `18`; unknown avg `0.3618` n `645`
- 1h: commodity avg `0.1532` n `12`; crypto_alt avg `-0.5802` n `228`; crypto_major avg `-0.3463` n `8`; equity avg `-0.0078` n `74`; fx avg `-0.0078` n `6`; index avg `-0.0014` n `23`; metal avg `-0.0848` n `18`; unknown avg `0.3584` n `645`
- 4h: commodity avg `0.0608` n `12`; crypto_alt avg `-0.2271` n `228`; crypto_major avg `-0.0428` n `8`; equity avg `0.3509` n `74`; fx avg `-0.0125` n `6`; index avg `0.1072` n `23`; metal avg `-0.045` n `18`; unknown avg `0.6205` n `629`
- 24h: commodity avg `-0.5612` n `12`; crypto_alt avg `-0.4114` n `228`; crypto_major avg `0.5105` n `8`; equity avg `0.9494` n `74`; fx avg `-0.02` n `6`; index avg `0.2349` n `23`; metal avg `0.262` n `18`; unknown avg `-0.683` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
