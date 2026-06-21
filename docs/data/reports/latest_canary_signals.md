# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T13:52:32.797858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `0.102` n `228`; crypto_major avg `0.1239` n `8`; equity avg `-0.0222` n `78`; fx avg `-0.0031` n `6`; index avg `-0.004` n `23`; metal avg `-0.0208` n `18`; unknown avg `0.0154` n `702`
- 1h: commodity avg `-0.0811` n `12`; crypto_alt avg `0.2509` n `228`; crypto_major avg `0.1548` n `8`; equity avg `-0.0602` n `78`; fx avg `0.1075` n `6`; index avg `0.0113` n `23`; metal avg `-0.0186` n `18`; unknown avg `0.0993` n `702`
- 4h: commodity avg `0.0635` n `12`; crypto_alt avg `0.0096` n `228`; crypto_major avg `-0.2912` n `8`; equity avg `-0.09` n `78`; fx avg `0.0234` n `6`; index avg `-0.0034` n `23`; metal avg `-0.0724` n `18`; unknown avg `0.1416` n `702`
- 24h: commodity avg `-0.0388` n `12`; crypto_alt avg `2.1288` n `228`; crypto_major avg `0.3633` n `8`; equity avg `0.5194` n `78`; fx avg `0.0576` n `6`; index avg `0.0456` n `23`; metal avg `-0.0442` n `18`; unknown avg `0.6898` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
