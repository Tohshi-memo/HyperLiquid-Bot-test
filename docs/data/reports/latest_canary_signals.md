# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T12:52:20.677560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1586` n `12`; crypto_alt avg `0.1304` n `228`; crypto_major avg `0.0834` n `8`; equity avg `0.0505` n `66`; fx avg `0.0022` n `6`; index avg `-0.0044` n `23`; metal avg `-0.0523` n `18`; unknown avg `0.1008` n `384`
- 1h: commodity avg `-0.5751` n `12`; crypto_alt avg `0.6137` n `228`; crypto_major avg `0.4214` n `8`; equity avg `0.2764` n `66`; fx avg `-0.0135` n `6`; index avg `0.0868` n `23`; metal avg `-0.0753` n `18`; unknown avg `0.5337` n `384`
- 4h: commodity avg `-0.1232` n `12`; crypto_alt avg `0.2867` n `228`; crypto_major avg `0.4477` n `8`; equity avg `0.2592` n `66`; fx avg `0.0499` n `6`; index avg `0.103` n `23`; metal avg `-0.046` n `18`; unknown avg `-0.32` n `384`
- 24h: commodity avg `-0.5886` n `12`; crypto_alt avg `1.1526` n `228`; crypto_major avg `0.7638` n `8`; equity avg `1.701` n `66`; fx avg `-0.0673` n `6`; index avg `0.2764` n `23`; metal avg `-0.7187` n `18`; unknown avg `0.7234` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.047`, n `668`, weak_sample_signal
