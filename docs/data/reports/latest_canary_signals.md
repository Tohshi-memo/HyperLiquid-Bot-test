# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T12:36:57.498761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1121` n `12`; crypto_alt avg `0.1358` n `229`; crypto_major avg `0.0814` n `8`; equity avg `0.1967` n `91`; fx avg `0.0011` n `6`; index avg `0.0716` n `25`; metal avg `0.0466` n `20`; unknown avg `0.1149` n `765`
- 1h: commodity avg `-0.0837` n `12`; crypto_alt avg `0.2673` n `229`; crypto_major avg `0.26` n `8`; equity avg `0.4409` n `91`; fx avg `0.0031` n `6`; index avg `0.1294` n `25`; metal avg `0.2413` n `20`; unknown avg `0.0944` n `764`
- 4h: commodity avg `0.2172` n `12`; crypto_alt avg `-0.0444` n `229`; crypto_major avg `-0.358` n `8`; equity avg `0.2429` n `91`; fx avg `-0.0255` n `6`; index avg `0.1147` n `25`; metal avg `0.1502` n `20`; unknown avg `-0.0542` n `764`
- 24h: commodity avg `-0.1855` n `12`; crypto_alt avg `1.3175` n `229`; crypto_major avg `0.3915` n `8`; equity avg `3.1647` n `91`; fx avg `0.1521` n `6`; index avg `0.5179` n `25`; metal avg `0.7439` n `20`; unknown avg `0.7345` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0998`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0983`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0754`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0691`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0667`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0602`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0596`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0582`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0579`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0573`, n `669`, weak_sample_signal
