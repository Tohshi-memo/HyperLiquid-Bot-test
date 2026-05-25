# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T14:16:32.706010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0244` n `12`; crypto_alt avg `0.1456` n `228`; crypto_major avg `0.0084` n `8`; equity avg `-0.025` n `67`; fx avg `0.0015` n `6`; index avg `-0.0127` n `23`; metal avg `-0.0306` n `18`; unknown avg `-0.2184` n `405`
- 1h: commodity avg `-0.1862` n `12`; crypto_alt avg `0.5111` n `228`; crypto_major avg `0.2259` n `8`; equity avg `0.1014` n `67`; fx avg `-0.0138` n `6`; index avg `0.0534` n `23`; metal avg `0.268` n `18`; unknown avg `0.1252` n `405`
- 4h: commodity avg `0.4627` n `12`; crypto_alt avg `0.3824` n `228`; crypto_major avg `0.2069` n `8`; equity avg `0.066` n `67`; fx avg `0.0178` n `6`; index avg `0.0903` n `23`; metal avg `-0.121` n `18`; unknown avg `-0.0865` n `397`
- 24h: commodity avg `-0.6789` n `12`; crypto_alt avg `2.3719` n `228`; crypto_major avg `1.0957` n `8`; equity avg `0.9034` n `67`; fx avg `0.0016` n `6`; index avg `0.332` n `23`; metal avg `1.3123` n `18`; unknown avg `0.7535` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
