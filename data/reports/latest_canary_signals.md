# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T05:07:28.549791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.057` n `12`; crypto_alt avg `-0.3045` n `228`; crypto_major avg `-0.3719` n `8`; equity avg `-0.0634` n `88`; fx avg `0.0036` n `6`; index avg `0.019` n `23`; metal avg `0.0392` n `20`; unknown avg `1.4657` n `764`
- 1h: commodity avg `-0.0876` n `12`; crypto_alt avg `-0.7866` n `228`; crypto_major avg `-0.98` n `8`; equity avg `-0.2746` n `88`; fx avg `-0.004` n `6`; index avg `-0.0543` n `23`; metal avg `-0.1773` n `20`; unknown avg `3.0904` n `764`
- 4h: commodity avg `-0.082` n `12`; crypto_alt avg `-0.0572` n `228`; crypto_major avg `-0.4086` n `8`; equity avg `-0.1562` n `88`; fx avg `0.0677` n `6`; index avg `-0.0521` n `23`; metal avg `-0.1631` n `20`; unknown avg `-0.8961` n `764`
- 24h: commodity avg `-0.3549` n `12`; crypto_alt avg `-0.4459` n `228`; crypto_major avg `-0.5466` n `8`; equity avg `-0.1569` n `88`; fx avg `0.0461` n `6`; index avg `-0.0721` n `23`; metal avg `-0.3006` n `20`; unknown avg `-0.9967` n `722`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
