# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T11:52:15.353316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1089` n `12`; crypto_alt avg `-0.3214` n `228`; crypto_major avg `-0.1192` n `8`; equity avg `-0.0064` n `67`; fx avg `-0.014` n `6`; index avg `-0.0024` n `23`; metal avg `-0.0567` n `18`; unknown avg `-0.0907` n `397`
- 1h: commodity avg `-0.0548` n `12`; crypto_alt avg `-0.3511` n `228`; crypto_major avg `-0.0719` n `8`; equity avg `0.0505` n `67`; fx avg `0.0244` n `6`; index avg `0.0163` n `23`; metal avg `0.0135` n `18`; unknown avg `-0.1621` n `397`
- 4h: commodity avg `-0.2612` n `12`; crypto_alt avg `0.2096` n `228`; crypto_major avg `0.1315` n `8`; equity avg `0.2976` n `67`; fx avg `0.0332` n `6`; index avg `0.0956` n `23`; metal avg `0.2098` n `18`; unknown avg `-0.1642` n `397`
- 24h: commodity avg `-0.2614` n `12`; crypto_alt avg `0.3193` n `228`; crypto_major avg `-0.1946` n `8`; equity avg `0.5579` n `67`; fx avg `0.0397` n `6`; index avg `0.0512` n `23`; metal avg `0.7147` n `18`; unknown avg `0.6016` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
