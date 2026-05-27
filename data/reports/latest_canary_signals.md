# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T01:22:17.522722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0855` n `12`; crypto_alt avg `-0.2834` n `228`; crypto_major avg `-0.2028` n `8`; equity avg `0.113` n `67`; fx avg `0.002` n `6`; index avg `0.037` n `23`; metal avg `0.0691` n `18`; unknown avg `0.0691` n `418`
- 1h: commodity avg `-0.0935` n `12`; crypto_alt avg `0.164` n `228`; crypto_major avg `0.1414` n `8`; equity avg `0.2991` n `67`; fx avg `-0.0195` n `6`; index avg `0.1051` n `23`; metal avg `-0.1245` n `18`; unknown avg `0.7809` n `418`
- 4h: commodity avg `-0.4094` n `12`; crypto_alt avg `0.1463` n `228`; crypto_major avg `0.2716` n `8`; equity avg `0.2363` n `67`; fx avg `-0.0133` n `6`; index avg `0.219` n `23`; metal avg `0.1844` n `18`; unknown avg `-0.4394` n `418`
- 24h: commodity avg `0.1521` n `12`; crypto_alt avg `-0.2353` n `228`; crypto_major avg `-0.4443` n `8`; equity avg `0.8254` n `67`; fx avg `-0.046` n `6`; index avg `1.0121` n `23`; metal avg `-0.0709` n `18`; unknown avg `0.6843` n `397`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
