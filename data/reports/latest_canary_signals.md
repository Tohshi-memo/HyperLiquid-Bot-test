# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T23:07:14.590058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `0.0786` n `228`; crypto_major avg `0.1232` n `8`; equity avg `-0.112` n `67`; fx avg `0.0022` n `6`; index avg `-0.0592` n `23`; metal avg `0.1902` n `18`; unknown avg `-0.0365` n `396`
- 1h: commodity avg `-0.1736` n `12`; crypto_alt avg `0.2423` n `228`; crypto_major avg `0.2633` n `8`; equity avg `-0.0321` n `67`; fx avg `0.014` n `6`; index avg `0.0233` n `23`; metal avg `0.5459` n `18`; unknown avg `-0.08` n `396`
- 4h: commodity avg `-0.8517` n `12`; crypto_alt avg `-0.6278` n `228`; crypto_major avg `-0.2869` n `8`; equity avg `-0.1363` n `67`; fx avg `0.0788` n `6`; index avg `-0.09` n `23`; metal avg `1.1716` n `18`; unknown avg `-0.3255` n `396`
- 24h: commodity avg `0.3429` n `12`; crypto_alt avg `-1.7897` n `228`; crypto_major avg `0.4982` n `8`; equity avg `0.2213` n `67`; fx avg `0.0948` n `6`; index avg `-0.0394` n `23`; metal avg `1.0938` n `18`; unknown avg `0.275` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
