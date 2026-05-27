# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T14:07:27.733983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.114` n `12`; crypto_alt avg `0.1776` n `228`; crypto_major avg `0.0872` n `8`; equity avg `0.2433` n `67`; fx avg `-0.0098` n `6`; index avg `0.0156` n `23`; metal avg `0.0641` n `18`; unknown avg `-0.1751` n `418`
- 1h: commodity avg `0.4357` n `12`; crypto_alt avg `-0.1649` n `228`; crypto_major avg `-0.4817` n `8`; equity avg `-0.4039` n `67`; fx avg `-0.0244` n `6`; index avg `-0.5351` n `23`; metal avg `0.2686` n `18`; unknown avg `-0.0292` n `418`
- 4h: commodity avg `0.3238` n `12`; crypto_alt avg `0.1659` n `228`; crypto_major avg `-0.7442` n `8`; equity avg `-0.6354` n `67`; fx avg `-0.0352` n `6`; index avg `-0.5981` n `23`; metal avg `-0.694` n `18`; unknown avg `0.0578` n `418`
- 24h: commodity avg `-1.4232` n `12`; crypto_alt avg `-2.5951` n `228`; crypto_major avg `-2.3382` n `8`; equity avg `0.0319` n `67`; fx avg `-0.0548` n `6`; index avg `-0.286` n `23`; metal avg `-1.1329` n `18`; unknown avg `0.1105` n `398`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.182`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1754`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
