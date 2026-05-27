# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T06:07:17.595539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1001` n `12`; crypto_alt avg `0.2161` n `228`; crypto_major avg `0.1675` n `8`; equity avg `-0.0202` n `67`; fx avg `0.0084` n `6`; index avg `-0.0172` n `23`; metal avg `-0.0388` n `18`; unknown avg `-0.0968` n `400`
- 1h: commodity avg `-0.0807` n `12`; crypto_alt avg `0.4052` n `228`; crypto_major avg `0.2807` n `8`; equity avg `-0.1355` n `67`; fx avg `0.0321` n `6`; index avg `-0.0487` n `23`; metal avg `-0.6217` n `18`; unknown avg `0.1883` n `400`
- 4h: commodity avg `-0.2416` n `12`; crypto_alt avg `0.1586` n `228`; crypto_major avg `0.4943` n `8`; equity avg `-0.4001` n `67`; fx avg `-0.0155` n `6`; index avg `-0.186` n `23`; metal avg `-0.5064` n `18`; unknown avg `0.1486` n `400`
- 24h: commodity avg `-0.3332` n `12`; crypto_alt avg `-1.0908` n `228`; crypto_major avg `-0.4213` n `8`; equity avg `0.3001` n `67`; fx avg `-0.0168` n `6`; index avg `0.7674` n `23`; metal avg `-0.5343` n `18`; unknown avg `0.581` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1776`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
