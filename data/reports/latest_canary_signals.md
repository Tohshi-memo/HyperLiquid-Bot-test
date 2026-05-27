# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T05:52:21.424266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0691` n `12`; crypto_alt avg `0.0735` n `228`; crypto_major avg `-0.0805` n `8`; equity avg `-0.1045` n `67`; fx avg `0.0106` n `6`; index avg `-0.0418` n `23`; metal avg `-0.2495` n `18`; unknown avg `-0.3294` n `418`
- 1h: commodity avg `-0.1503` n `12`; crypto_alt avg `0.3933` n `228`; crypto_major avg `0.2551` n `8`; equity avg `-0.1727` n `67`; fx avg `0.0199` n `6`; index avg `-0.0674` n `23`; metal avg `-0.6448` n `18`; unknown avg `0.4306` n `418`
- 4h: commodity avg `-0.5054` n `12`; crypto_alt avg `-0.5514` n `228`; crypto_major avg `0.0655` n `8`; equity avg `-0.3799` n `67`; fx avg `-0.0226` n `6`; index avg `-0.1836` n `23`; metal avg `-0.5277` n `18`; unknown avg `-0.6572` n `418`
- 24h: commodity avg `-0.4863` n `12`; crypto_alt avg `-1.2183` n `228`; crypto_major avg `-0.538` n `8`; equity avg `0.3918` n `67`; fx avg `-0.0284` n `6`; index avg `0.8117` n `23`; metal avg `-0.4076` n `18`; unknown avg `1.3794` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1817`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1794`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
