# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T14:22:23.044632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0669` n `12`; crypto_alt avg `0.2302` n `228`; crypto_major avg `0.3198` n `8`; equity avg `0.1723` n `67`; fx avg `0.0017` n `6`; index avg `0.0599` n `23`; metal avg `-0.0002` n `18`; unknown avg `0.0694` n `418`
- 1h: commodity avg `0.2165` n `12`; crypto_alt avg `0.8066` n `228`; crypto_major avg `1.1614` n `8`; equity avg `0.1449` n `67`; fx avg `-0.0235` n `6`; index avg `0.4175` n `23`; metal avg `-0.2084` n `18`; unknown avg `0.4837` n `418`
- 4h: commodity avg `0.4119` n `12`; crypto_alt avg `1.1735` n `228`; crypto_major avg `1.5719` n `8`; equity avg `0.2831` n `67`; fx avg `-0.0478` n `6`; index avg `0.5421` n `23`; metal avg `0.0884` n `18`; unknown avg `0.9494` n `417`
- 24h: commodity avg `0.8775` n `12`; crypto_alt avg `0.336` n `228`; crypto_major avg `0.2055` n `8`; equity avg `-0.2193` n `67`; fx avg `-0.1449` n `6`; index avg `0.5006` n `23`; metal avg `-0.7481` n `18`; unknown avg `-0.0206` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.181`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
