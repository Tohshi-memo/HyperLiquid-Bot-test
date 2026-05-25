# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T07:07:16.922046+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.062` n `12`; crypto_alt avg `0.1381` n `228`; crypto_major avg `0.0411` n `8`; equity avg `0.0404` n `67`; fx avg `-0.0184` n `6`; index avg `0.0015` n `23`; metal avg `0.12` n `18`; unknown avg `0.0181` n `397`
- 1h: commodity avg `0.0975` n `12`; crypto_alt avg `-0.0244` n `228`; crypto_major avg `-0.1189` n `8`; equity avg `-0.0036` n `67`; fx avg `0.0086` n `6`; index avg `0.0676` n `23`; metal avg `0.2371` n `18`; unknown avg `-0.0745` n `397`
- 4h: commodity avg `-0.0731` n `12`; crypto_alt avg `1.2409` n `228`; crypto_major avg `0.7271` n `8`; equity avg `0.2593` n `67`; fx avg `0.044` n `6`; index avg `0.1358` n `23`; metal avg `0.1639` n `18`; unknown avg `0.2093` n `387`
- 24h: commodity avg `0.2031` n `12`; crypto_alt avg `0.0988` n `228`; crypto_major avg `0.066` n `8`; equity avg `0.4597` n `67`; fx avg `-0.0275` n `6`; index avg `-0.0846` n `23`; metal avg `0.4551` n `18`; unknown avg `0.0456` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
