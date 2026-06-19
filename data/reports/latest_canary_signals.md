# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T23:12:24.833489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1101` n `12`; crypto_alt avg `-0.135` n `228`; crypto_major avg `-0.1054` n `8`; equity avg `-0.0203` n `78`; fx avg `-0.0261` n `6`; index avg `0.0015` n `23`; metal avg `-0.0271` n `18`; unknown avg `0.1018` n `687`
- 1h: commodity avg `-0.1829` n `12`; crypto_alt avg `0.2416` n `228`; crypto_major avg `0.3524` n `8`; equity avg `0.1392` n `78`; fx avg `0.0137` n `6`; index avg `0.0038` n `23`; metal avg `0.015` n `18`; unknown avg `-0.2015` n `687`
- 4h: commodity avg `0.0253` n `12`; crypto_alt avg `-0.084` n `228`; crypto_major avg `-0.0021` n `8`; equity avg `0.1011` n `78`; fx avg `-0.045` n `6`; index avg `-0.0116` n `23`; metal avg `0.1567` n `18`; unknown avg `-0.5467` n `687`
- 24h: commodity avg `0.3169` n `12`; crypto_alt avg `-3.7602` n `228`; crypto_major avg `-4.5437` n `8`; equity avg `0.7918` n `78`; fx avg `-0.1226` n `6`; index avg `0.2142` n `23`; metal avg `-4.0996` n `18`; unknown avg `-0.6751` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
