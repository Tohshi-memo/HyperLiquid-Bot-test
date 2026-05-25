# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T06:52:13.932675+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0475` n `12`; crypto_alt avg `0.0098` n `228`; crypto_major avg `-0.0165` n `8`; equity avg `0.0451` n `67`; fx avg `0.0163` n `6`; index avg `0.0441` n `23`; metal avg `0.0655` n `18`; unknown avg `-0.2055` n `397`
- 1h: commodity avg `0.2706` n `12`; crypto_alt avg `-0.0047` n `228`; crypto_major avg `-0.0337` n `8`; equity avg `-0.1198` n `67`; fx avg `0.0269` n `6`; index avg `0.0911` n `23`; metal avg `0.0755` n `18`; unknown avg `0.0704` n `387`
- 4h: commodity avg `-0.1878` n `12`; crypto_alt avg `1.0575` n `228`; crypto_major avg `0.6036` n `8`; equity avg `0.2575` n `67`; fx avg `0.0562` n `6`; index avg `0.1846` n `23`; metal avg `-0.118` n `18`; unknown avg `0.3537` n `386`
- 24h: commodity avg `0.3538` n `12`; crypto_alt avg `-0.0837` n `228`; crypto_major avg `-0.0015` n `8`; equity avg `0.4467` n `67`; fx avg `-0.0176` n `6`; index avg `-0.0491` n `23`; metal avg `0.3511` n `18`; unknown avg `0.0813` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
