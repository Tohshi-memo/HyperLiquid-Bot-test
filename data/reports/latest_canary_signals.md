# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T13:52:26.852741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `0.3365` n `228`; crypto_major avg `0.282` n `8`; equity avg `0.1086` n `66`; fx avg `-0.0043` n `6`; index avg `0.2121` n `23`; metal avg `0.0181` n `18`; unknown avg `-0.0118` n `384`
- 1h: commodity avg `0.1517` n `12`; crypto_alt avg `-0.3376` n `228`; crypto_major avg `-0.0596` n `8`; equity avg `-0.3963` n `66`; fx avg `-0.0025` n `6`; index avg `0.1488` n `23`; metal avg `-0.3935` n `18`; unknown avg `0.7229` n `384`
- 4h: commodity avg `-0.2532` n `12`; crypto_alt avg `-0.0749` n `228`; crypto_major avg `0.344` n `8`; equity avg `-0.1397` n `66`; fx avg `0.0367` n `6`; index avg `0.1992` n `23`; metal avg `-0.3834` n `18`; unknown avg `1.6226` n `384`
- 24h: commodity avg `-0.6089` n `12`; crypto_alt avg `0.3504` n `228`; crypto_major avg `0.523` n `8`; equity avg `1.188` n `66`; fx avg `-0.0725` n `6`; index avg `0.7232` n `23`; metal avg `-0.1065` n `18`; unknown avg `1.3183` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0493`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
