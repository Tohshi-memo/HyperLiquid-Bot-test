# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T12:22:34.190763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `0.21` n `228`; crypto_major avg `0.0607` n `8`; equity avg `-0.0832` n `74`; fx avg `0.0056` n `6`; index avg `0.0176` n `23`; metal avg `0.0034` n `18`; unknown avg `-0.0114` n `645`
- 1h: commodity avg `-0.0053` n `12`; crypto_alt avg `0.3046` n `228`; crypto_major avg `0.1105` n `8`; equity avg `-0.0635` n `74`; fx avg `0.0312` n `6`; index avg `0.0554` n `23`; metal avg `0.0419` n `18`; unknown avg `-0.0684` n `645`
- 4h: commodity avg `0.2254` n `12`; crypto_alt avg `-0.0751` n `228`; crypto_major avg `0.1336` n `8`; equity avg `0.0864` n `74`; fx avg `0.0206` n `6`; index avg `0.1046` n `23`; metal avg `-0.0408` n `18`; unknown avg `0.3158` n `629`
- 24h: commodity avg `-0.4646` n `12`; crypto_alt avg `-0.2639` n `228`; crypto_major avg `0.485` n `8`; equity avg `0.8819` n `74`; fx avg `0.0117` n `6`; index avg `0.2978` n `23`; metal avg `0.1721` n `18`; unknown avg `-0.8371` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
