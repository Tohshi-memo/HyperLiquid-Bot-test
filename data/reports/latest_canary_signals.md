# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T16:18:59.450013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `-0.1426` n `228`; crypto_major avg `-0.0216` n `8`; equity avg `0.0109` n `78`; fx avg `-0.0055` n `6`; index avg `-0.0159` n `23`; metal avg `-0.002` n `18`; unknown avg `-0.3119` n `702`
- 1h: commodity avg `-0.0201` n `12`; crypto_alt avg `0.1157` n `228`; crypto_major avg `-0.0883` n `8`; equity avg `-0.0023` n `78`; fx avg `-0.0049` n `6`; index avg `-0.0289` n `23`; metal avg `-0.0133` n `18`; unknown avg `-0.3012` n `702`
- 4h: commodity avg `-0.0844` n `12`; crypto_alt avg `0.6498` n `228`; crypto_major avg `0.6581` n `8`; equity avg `0.0296` n `78`; fx avg `0.0475` n `6`; index avg `-0.0261` n `23`; metal avg `-0.0075` n `18`; unknown avg `-0.0164` n `702`
- 24h: commodity avg `0.0259` n `12`; crypto_alt avg `1.5027` n `228`; crypto_major avg `0.0026` n `8`; equity avg `0.3117` n `78`; fx avg `0.0154` n `6`; index avg `-0.0026` n `23`; metal avg `-0.0979` n `18`; unknown avg `0.2044` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
