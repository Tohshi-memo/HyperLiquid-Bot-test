# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T14:37:21.373436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0775` n `12`; crypto_alt avg `-0.0306` n `228`; crypto_major avg `0.0353` n `8`; equity avg `0.0111` n `67`; fx avg `-0.004` n `6`; index avg `-0.0102` n `23`; metal avg `0.2621` n `18`; unknown avg `0.045` n `405`
- 1h: commodity avg `-0.2279` n `12`; crypto_alt avg `0.6068` n `228`; crypto_major avg `0.3889` n `8`; equity avg `0.1087` n `67`; fx avg `-0.0096` n `6`; index avg `-0.0004` n `23`; metal avg `0.4384` n `18`; unknown avg `0.0494` n `405`
- 4h: commodity avg `0.3708` n `12`; crypto_alt avg `0.3611` n `228`; crypto_major avg `0.294` n `8`; equity avg `0.0744` n `67`; fx avg `0.0105` n `6`; index avg `0.0744` n `23`; metal avg `0.2141` n `18`; unknown avg `-0.1297` n `397`
- 24h: commodity avg `-0.6622` n `12`; crypto_alt avg `2.3492` n `228`; crypto_major avg `1.1421` n `8`; equity avg `0.9606` n `67`; fx avg `-0.0062` n `6`; index avg `0.4017` n `23`; metal avg `1.5778` n `18`; unknown avg `0.7928` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
