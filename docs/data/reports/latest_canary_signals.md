# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T16:52:31.302031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0294` n `12`; crypto_alt avg `0.2336` n `228`; crypto_major avg `0.4039` n `8`; equity avg `0.0436` n `78`; fx avg `-0.0507` n `6`; index avg `-0.0085` n `23`; metal avg `0.0061` n `18`; unknown avg `-0.1373` n `702`
- 1h: commodity avg `0.0848` n `12`; crypto_alt avg `-0.0278` n `228`; crypto_major avg `0.0125` n `8`; equity avg `-0.0397` n `78`; fx avg `-0.063` n `6`; index avg `0.0063` n `23`; metal avg `-0.016` n `18`; unknown avg `-0.7001` n `702`
- 4h: commodity avg `0.0449` n `12`; crypto_alt avg `0.4601` n `228`; crypto_major avg `0.5268` n `8`; equity avg `-0.0088` n `78`; fx avg `0.0595` n `6`; index avg `-0.0035` n `23`; metal avg `-0.0102` n `18`; unknown avg `-0.5082` n `702`
- 24h: commodity avg `0.0985` n `12`; crypto_alt avg `1.3908` n `228`; crypto_major avg `0.2628` n `8`; equity avg `0.3714` n `78`; fx avg `-0.0507` n `6`; index avg `0.025` n `23`; metal avg `-0.0544` n `18`; unknown avg `-0.1245` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
