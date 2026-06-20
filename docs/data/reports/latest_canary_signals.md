# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T21:43:33.657871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `0.0386` n `228`; crypto_major avg `0.1062` n `8`; equity avg `-0.0007` n `78`; fx avg `-0.005` n `6`; index avg `0.0007` n `23`; metal avg `-0.0041` n `18`; unknown avg `0.1716` n `701`
- 1h: commodity avg `0.1065` n `12`; crypto_alt avg `0.3944` n `228`; crypto_major avg `0.3973` n `8`; equity avg `0.0426` n `78`; fx avg `-0.0074` n `6`; index avg `0.0021` n `23`; metal avg `0.0111` n `18`; unknown avg `0.1535` n `701`
- 4h: commodity avg `0.0317` n `12`; crypto_alt avg `0.5344` n `228`; crypto_major avg `0.714` n `8`; equity avg `0.1691` n `78`; fx avg `0.1285` n `6`; index avg `0.015` n `23`; metal avg `-0.0148` n `18`; unknown avg `0.1069` n `701`
- 24h: commodity avg `0.2989` n `12`; crypto_alt avg `0.9724` n `228`; crypto_major avg `1.4413` n `8`; equity avg `0.5126` n `78`; fx avg `0.1072` n `6`; index avg `0.0672` n `23`; metal avg `-0.0473` n `18`; unknown avg `0.048` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
