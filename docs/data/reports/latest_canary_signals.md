# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T16:07:26.125916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.031` n `12`; crypto_alt avg `0.1164` n `228`; crypto_major avg `-0.0724` n `8`; equity avg `-0.0517` n `78`; fx avg `0.0025` n `6`; index avg `0.006` n `23`; metal avg `-0.0217` n `18`; unknown avg `-0.0428` n `702`
- 1h: commodity avg `-0.0453` n `12`; crypto_alt avg `0.1056` n `228`; crypto_major avg `-0.1421` n `8`; equity avg `-0.004` n `78`; fx avg `-0.0026` n `6`; index avg `-0.0091` n `23`; metal avg `-0.0103` n `18`; unknown avg `-0.0242` n `702`
- 4h: commodity avg `-0.0806` n `12`; crypto_alt avg `0.6327` n `228`; crypto_major avg `0.4347` n `8`; equity avg `0.0085` n `78`; fx avg `0.0207` n `6`; index avg `-0.0211` n `23`; metal avg `-0.0167` n `18`; unknown avg `0.3045` n `702`
- 24h: commodity avg `0.0386` n `12`; crypto_alt avg `1.5608` n `228`; crypto_major avg `-0.0434` n `8`; equity avg `0.3382` n `78`; fx avg `0.0209` n `6`; index avg `0.0297` n `23`; metal avg `-0.0959` n `18`; unknown avg `0.4209` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
