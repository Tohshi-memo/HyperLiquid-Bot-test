# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T09:07:20.413486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.195` n `12`; crypto_alt avg `-0.118` n `228`; crypto_major avg `-0.0673` n `8`; equity avg `-0.1003` n `67`; fx avg `0.0011` n `6`; index avg `-0.158` n `23`; metal avg `0.0033` n `18`; unknown avg `0.0485` n `418`
- 1h: commodity avg `-0.2015` n `12`; crypto_alt avg `-0.4713` n `228`; crypto_major avg `-0.0452` n `8`; equity avg `0.165` n `67`; fx avg `-0.0175` n `6`; index avg `0.1194` n `23`; metal avg `0.1862` n `18`; unknown avg `0.852` n `418`
- 4h: commodity avg `-0.8947` n `12`; crypto_alt avg `0.2487` n `228`; crypto_major avg `0.4192` n `8`; equity avg `0.3876` n `67`; fx avg `0.0155` n `6`; index avg `0.0497` n `23`; metal avg `-0.728` n `18`; unknown avg `1.278` n `400`
- 24h: commodity avg `-1.8571` n `12`; crypto_alt avg `-0.9418` n `228`; crypto_major avg `0.1929` n `8`; equity avg `0.74` n `67`; fx avg `-0.0375` n `6`; index avg `0.8505` n `23`; metal avg `-0.4322` n `18`; unknown avg `2.7343` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1817`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
