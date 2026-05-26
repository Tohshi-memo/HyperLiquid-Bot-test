# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T02:22:16.496383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0171` n `12`; crypto_alt avg `0.1293` n `228`; crypto_major avg `0.109` n `8`; equity avg `0.03` n `67`; fx avg `0.0194` n `6`; index avg `-0.0146` n `23`; metal avg `0.0745` n `18`; unknown avg `-0.0854` n `407`
- 1h: commodity avg `-0.0331` n `12`; crypto_alt avg `-0.3247` n `228`; crypto_major avg `-0.2643` n `8`; equity avg `-0.0779` n `67`; fx avg `0.0011` n `6`; index avg `-0.0106` n `23`; metal avg `-0.2661` n `18`; unknown avg `0.6039` n `407`
- 4h: commodity avg `0.5846` n `12`; crypto_alt avg `-1.7693` n `228`; crypto_major avg `-1.3136` n `8`; equity avg `-0.9706` n `67`; fx avg `-0.0968` n `6`; index avg `-0.3435` n `23`; metal avg `-0.9327` n `18`; unknown avg `2.0087` n `405`
- 24h: commodity avg `-0.0169` n `12`; crypto_alt avg `-0.2854` n `228`; crypto_major avg `-1.0462` n `8`; equity avg `-0.2564` n `67`; fx avg `-0.0066` n `6`; index avg `0.0826` n `23`; metal avg `-0.29` n `18`; unknown avg `1.1357` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
