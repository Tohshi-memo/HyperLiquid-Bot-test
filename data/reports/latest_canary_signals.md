# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T01:22:18.128960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0401` n `12`; crypto_alt avg `0.0907` n `228`; crypto_major avg `0.0919` n `8`; equity avg `0.0061` n `67`; fx avg `-0.0126` n `6`; index avg `0.0063` n `23`; metal avg `-0.0494` n `18`; unknown avg `0.1344` n `396`
- 1h: commodity avg `0.0536` n `12`; crypto_alt avg `0.0578` n `228`; crypto_major avg `-0.0551` n `8`; equity avg `0.081` n `67`; fx avg `-0.0431` n `6`; index avg `0.0932` n `23`; metal avg `-0.0984` n `18`; unknown avg `-0.1624` n `396`
- 4h: commodity avg `-0.6563` n `12`; crypto_alt avg `0.4071` n `228`; crypto_major avg `0.3889` n `8`; equity avg `0.0518` n `67`; fx avg `-0.1226` n `6`; index avg `0.1732` n `23`; metal avg `1.3629` n `18`; unknown avg `0.3449` n `396`
- 24h: commodity avg `0.48` n `12`; crypto_alt avg `-1.4537` n `228`; crypto_major avg `-0.0139` n `8`; equity avg `0.2277` n `67`; fx avg `-0.0473` n `6`; index avg `-0.198` n `23`; metal avg `0.6814` n `18`; unknown avg `-0.3913` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
