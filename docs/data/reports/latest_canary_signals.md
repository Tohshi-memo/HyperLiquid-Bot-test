# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T19:52:19.416013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.084` n `12`; crypto_alt avg `0.0428` n `228`; crypto_major avg `0.086` n `8`; equity avg `-0.0025` n `66`; fx avg `0.0008` n `6`; index avg `-0.061` n `23`; metal avg `0.0006` n `18`; unknown avg `0.725` n `384`
- 1h: commodity avg `0.0894` n `12`; crypto_alt avg `0.4262` n `228`; crypto_major avg `0.5017` n `8`; equity avg `0.0701` n `66`; fx avg `0.0078` n `6`; index avg `0.1126` n `23`; metal avg `0.0127` n `18`; unknown avg `0.7687` n `384`
- 4h: commodity avg `-0.0855` n `12`; crypto_alt avg `0.3835` n `228`; crypto_major avg `0.2503` n `8`; equity avg `0.0224` n `66`; fx avg `0.0318` n `6`; index avg `0.1317` n `23`; metal avg `0.0777` n `18`; unknown avg `1.4551` n `384`
- 24h: commodity avg `-2.54` n `12`; crypto_alt avg `3.0387` n `228`; crypto_major avg `1.9996` n `8`; equity avg `1.6331` n `66`; fx avg `-0.0499` n `6`; index avg `1.1876` n `23`; metal avg `1.6111` n `18`; unknown avg `2.2231` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0489`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
