# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T12:06:23.834742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `0.0443` n `228`; crypto_major avg `0.0787` n `8`; equity avg `0.0046` n `65`; fx avg `0.0` n `5`; index avg `0.0037` n `23`; metal avg `0.0262` n `18`; unknown avg `0.2968` n `376`
- 1h: commodity avg `-0.0935` n `12`; crypto_alt avg `0.0544` n `228`; crypto_major avg `0.151` n `8`; equity avg `-0.0012` n `65`; fx avg `-0.0108` n `5`; index avg `-0.005` n `23`; metal avg `0.0484` n `18`; unknown avg `0.4678` n `376`
- 4h: commodity avg `-0.0713` n `12`; crypto_alt avg `-0.3436` n `228`; crypto_major avg `-0.1242` n `8`; equity avg `-0.0008` n `65`; fx avg `-0.0045` n `5`; index avg `0.0036` n `23`; metal avg `-0.0017` n `18`; unknown avg `-0.259` n `376`
- 24h: commodity avg `-0.0475` n `12`; crypto_alt avg `3.1652` n `228`; crypto_major avg `2.0149` n `8`; equity avg `2.8164` n `65`; fx avg `-0.022` n `5`; index avg `1.0493` n `23`; metal avg `-0.1169` n `18`; unknown avg `0.5808` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
