# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T16:22:18.174058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0663` n `12`; crypto_alt avg `0.0462` n `228`; crypto_major avg `0.085` n `8`; equity avg `0.007` n `67`; fx avg `0.0012` n `6`; index avg `0.0107` n `23`; metal avg `0.0466` n `18`; unknown avg `0.0801` n `396`
- 1h: commodity avg `-0.095` n `12`; crypto_alt avg `0.4114` n `228`; crypto_major avg `0.3039` n `8`; equity avg `-0.0846` n `67`; fx avg `0.0115` n `6`; index avg `0.0071` n `23`; metal avg `0.0868` n `18`; unknown avg `-0.2163` n `396`
- 4h: commodity avg `0.5051` n `12`; crypto_alt avg `-0.1838` n `228`; crypto_major avg `-0.2881` n `8`; equity avg `-0.3269` n `67`; fx avg `0.0376` n `6`; index avg `-0.3713` n `23`; metal avg `-0.3564` n `18`; unknown avg `0.2641` n `396`
- 24h: commodity avg `-1.48` n `12`; crypto_alt avg `0.922` n `228`; crypto_major avg `2.6387` n `8`; equity avg `1.613` n `67`; fx avg `0.0846` n `6`; index avg `0.6049` n `23`; metal avg `0.7003` n `18`; unknown avg `1.0241` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
