# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T16:22:22.643286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3129` n `12`; crypto_alt avg `0.526` n `228`; crypto_major avg `0.5681` n `8`; equity avg `0.0845` n `67`; fx avg `-0.0085` n `6`; index avg `0.0958` n `23`; metal avg `0.3228` n `18`; unknown avg `0.1438` n `419`
- 1h: commodity avg `-0.1637` n `12`; crypto_alt avg `0.7831` n `228`; crypto_major avg `0.7732` n `8`; equity avg `0.1803` n `67`; fx avg `-0.0064` n `6`; index avg `0.1381` n `23`; metal avg `0.6075` n `18`; unknown avg `-0.1286` n `419`
- 4h: commodity avg `0.0535` n `12`; crypto_alt avg `0.8164` n `228`; crypto_major avg `1.1814` n `8`; equity avg `2.0841` n `67`; fx avg `0.0244` n `6`; index avg `1.2794` n `23`; metal avg `2.165` n `18`; unknown avg `0.0116` n `419`
- 24h: commodity avg `0.4295` n `12`; crypto_alt avg `-5.1612` n `228`; crypto_major avg `-2.3837` n `8`; equity avg `1.262` n `67`; fx avg `-0.0017` n `6`; index avg `0.9134` n `23`; metal avg `0.544` n `18`; unknown avg `-1.2648` n `408`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
