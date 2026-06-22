# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T02:52:26.813424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0273` n `12`; crypto_alt avg `-0.2941` n `228`; crypto_major avg `-0.2951` n `8`; equity avg `-0.1544` n `79`; fx avg `-0.0072` n `6`; index avg `-0.0061` n `23`; metal avg `-0.1336` n `18`; unknown avg `-0.2952` n `701`
- 1h: commodity avg `-0.0682` n `12`; crypto_alt avg `-0.4126` n `228`; crypto_major avg `-0.4341` n `8`; equity avg `0.0425` n `79`; fx avg `0.0105` n `6`; index avg `-0.0292` n `23`; metal avg `-0.1453` n `18`; unknown avg `0.3001` n `701`
- 4h: commodity avg `-0.4226` n `12`; crypto_alt avg `0.8096` n `228`; crypto_major avg `0.7057` n `8`; equity avg `-0.3284` n `79`; fx avg `0.1412` n `6`; index avg `0.0763` n `23`; metal avg `0.2849` n `18`; unknown avg `-0.1196` n `685`
- 24h: commodity avg `-0.3103` n `12`; crypto_alt avg `0.2912` n `228`; crypto_major avg `-0.2712` n `8`; equity avg `-0.4578` n `79`; fx avg `0.0273` n `6`; index avg `0.0004` n `23`; metal avg `0.1785` n `18`; unknown avg `0.1184` n `629`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
