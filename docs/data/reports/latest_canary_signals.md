# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T19:37:13.018181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `-0.0077` n `228`; crypto_major avg `-0.0322` n `8`; equity avg `-0.023` n `67`; fx avg `-0.0037` n `6`; index avg `-0.0126` n `23`; metal avg `-0.0172` n `18`; unknown avg `-0.111` n `396`
- 1h: commodity avg `-0.1999` n `12`; crypto_alt avg `-0.0885` n `228`; crypto_major avg `-0.0625` n `8`; equity avg `-0.0577` n `67`; fx avg `-0.0074` n `6`; index avg `-0.1191` n `23`; metal avg `0.0156` n `18`; unknown avg `0.0327` n `396`
- 4h: commodity avg `-0.9969` n `12`; crypto_alt avg `1.5103` n `228`; crypto_major avg `0.9794` n `8`; equity avg `0.575` n `67`; fx avg `-0.0113` n `6`; index avg `0.2438` n `23`; metal avg `0.1452` n `18`; unknown avg `0.9314` n `396`
- 24h: commodity avg `-0.7757` n `12`; crypto_alt avg `1.103` n `228`; crypto_major avg `0.578` n `8`; equity avg `0.3917` n `67`; fx avg `-0.0247` n `6`; index avg `0.2137` n `23`; metal avg `0.1405` n `18`; unknown avg `-0.8323` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
