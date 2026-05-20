# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T07:07:19.702096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0276` n `12`; crypto_alt avg `-0.0551` n `228`; crypto_major avg `-0.1031` n `8`; equity avg `0.0964` n `66`; fx avg `-0.0044` n `6`; index avg `-0.0072` n `23`; metal avg `-0.084` n `18`; unknown avg `0.0557` n `384`
- 1h: commodity avg `-0.405` n `12`; crypto_alt avg `0.0576` n `228`; crypto_major avg `0.1751` n `8`; equity avg `0.3569` n `66`; fx avg `-0.0431` n `6`; index avg `0.0998` n `23`; metal avg `0.4466` n `18`; unknown avg `-0.0188` n `384`
- 4h: commodity avg `-0.3869` n `12`; crypto_alt avg `1.3821` n `228`; crypto_major avg `1.0456` n `8`; equity avg `0.755` n `66`; fx avg `-0.0062` n `6`; index avg `0.3251` n `23`; metal avg `1.1211` n `18`; unknown avg `0.4131` n `374`
- 24h: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.1443` n `228`; crypto_major avg `-0.063` n `8`; equity avg `0.3945` n `66`; fx avg `-0.1581` n `6`; index avg `-0.4745` n `23`; metal avg `-1.2922` n `18`; unknown avg `0.1321` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
