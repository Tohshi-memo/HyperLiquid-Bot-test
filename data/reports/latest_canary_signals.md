# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T03:52:25.739396+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `12`; crypto_alt avg `0.0542` n `228`; crypto_major avg `-0.0044` n `8`; equity avg `0.0317` n `78`; fx avg `-0.0026` n `6`; index avg `0.0051` n `23`; metal avg `-0.0043` n `18`; unknown avg `-0.3847` n `702`
- 1h: commodity avg `0.0151` n `12`; crypto_alt avg `0.0702` n `228`; crypto_major avg `0.1583` n `8`; equity avg `0.1221` n `78`; fx avg `-0.0025` n `6`; index avg `0.015` n `23`; metal avg `0.0151` n `18`; unknown avg `-0.5981` n `702`
- 4h: commodity avg `0.0369` n `12`; crypto_alt avg `0.3403` n `228`; crypto_major avg `-0.0324` n `8`; equity avg `0.1569` n `78`; fx avg `-0.0115` n `6`; index avg `0.0165` n `23`; metal avg `0.0077` n `18`; unknown avg `1.0732` n `701`
- 24h: commodity avg `0.1787` n `12`; crypto_alt avg `1.7353` n `228`; crypto_major avg `1.6062` n `8`; equity avg `0.4332` n `78`; fx avg `0.0487` n `6`; index avg `0.0189` n `23`; metal avg `0.019` n `18`; unknown avg `1.7809` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
