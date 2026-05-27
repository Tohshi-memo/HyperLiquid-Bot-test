# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T10:22:23.968107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `0.201` n `228`; crypto_major avg `0.1277` n `8`; equity avg `-0.0163` n `67`; fx avg `-0.0207` n `6`; index avg `-0.0167` n `23`; metal avg `-0.1293` n `18`; unknown avg `0.1885` n `418`
- 1h: commodity avg `0.2878` n `12`; crypto_alt avg `0.0716` n `228`; crypto_major avg `0.1149` n `8`; equity avg `0.1892` n `67`; fx avg `-0.0156` n `6`; index avg `0.0688` n `23`; metal avg `-0.085` n `18`; unknown avg `-0.1227` n `418`
- 4h: commodity avg `-0.7179` n `12`; crypto_alt avg `0.1018` n `228`; crypto_major avg `0.5111` n `8`; equity avg `0.824` n `67`; fx avg `-0.0459` n `6`; index avg `0.2317` n `23`; metal avg `0.1789` n `18`; unknown avg `-0.1966` n `418`
- 24h: commodity avg `-1.4209` n `12`; crypto_alt avg `-1.6576` n `228`; crypto_major avg `-0.2614` n `8`; equity avg `0.8199` n `67`; fx avg `-0.0899` n `6`; index avg `0.7876` n `23`; metal avg `-0.4832` n `18`; unknown avg `0.6429` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
