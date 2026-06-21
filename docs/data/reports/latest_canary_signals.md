# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T10:37:26.979594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0365` n `12`; crypto_alt avg `-0.0737` n `228`; crypto_major avg `0.0049` n `8`; equity avg `-0.0092` n `78`; fx avg `0.0046` n `6`; index avg `-0.0007` n `23`; metal avg `0.0015` n `18`; unknown avg `-0.0283` n `702`
- 1h: commodity avg `-0.0348` n `12`; crypto_alt avg `0.3006` n `228`; crypto_major avg `0.22` n `8`; equity avg `-0.0224` n `78`; fx avg `0.0026` n `6`; index avg `0.0019` n `23`; metal avg `0.0045` n `18`; unknown avg `-0.2085` n `702`
- 4h: commodity avg `-0.0932` n `12`; crypto_alt avg `0.5932` n `228`; crypto_major avg `-0.0192` n `8`; equity avg `-0.031` n `78`; fx avg `-0.0072` n `6`; index avg `0.0212` n `23`; metal avg `-0.0272` n `18`; unknown avg `-0.2724` n `694`
- 24h: commodity avg `0.0324` n `12`; crypto_alt avg `1.6186` n `228`; crypto_major avg `0.2781` n `8`; equity avg `0.3769` n `78`; fx avg `0.029` n `6`; index avg `0.0455` n `23`; metal avg `-0.0109` n `18`; unknown avg `0.2361` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
