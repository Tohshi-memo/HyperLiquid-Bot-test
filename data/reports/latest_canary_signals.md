# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T23:22:26.320109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0222` n `12`; crypto_alt avg `0.0124` n `230`; crypto_major avg `-0.0394` n `8`; equity avg `0.0269` n `94`; fx avg `-0.0159` n `6`; index avg `0.0222` n `25`; metal avg `-0.0056` n `20`; unknown avg `-0.0293` n `768`
- 1h: commodity avg `-0.0252` n `12`; crypto_alt avg `0.0777` n `230`; crypto_major avg `0.0927` n `8`; equity avg `-0.0812` n `94`; fx avg `-0.0234` n `6`; index avg `-0.015` n `25`; metal avg `-0.0254` n `20`; unknown avg `0.7873` n `768`
- 4h: commodity avg `0.0019` n `12`; crypto_alt avg `0.2745` n `230`; crypto_major avg `0.2304` n `8`; equity avg `0.2832` n `94`; fx avg `-0.0229` n `6`; index avg `0.0589` n `25`; metal avg `-0.0307` n `20`; unknown avg `0.0266` n `768`
- 24h: commodity avg `0.0954` n `12`; crypto_alt avg `0.3214` n `230`; crypto_major avg `0.5551` n `8`; equity avg `-0.8164` n `93`; fx avg `0.2029` n `6`; index avg `-0.1984` n `25`; metal avg `0.1306` n `20`; unknown avg `0.0936` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
