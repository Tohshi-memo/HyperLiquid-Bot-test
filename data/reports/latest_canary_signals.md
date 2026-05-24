# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T23:22:19.720388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5837` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0354` n `12`; crypto_alt avg `-0.0154` n `228`; crypto_major avg `0.0952` n `8`; equity avg `0.0807` n `67`; fx avg `0.0025` n `6`; index avg `-0.0068` n `23`; metal avg `0.1584` n `18`; unknown avg `0.8812` n `396`
- 1h: commodity avg `-0.1748` n `12`; crypto_alt avg `-0.0741` n `228`; crypto_major avg `0.0401` n `8`; equity avg `0.0241` n `67`; fx avg `0.017` n `6`; index avg `-0.0259` n `23`; metal avg `0.5243` n `18`; unknown avg `0.7721` n `396`
- 4h: commodity avg `-0.8417` n `12`; crypto_alt avg `-0.5928` n `228`; crypto_major avg `-0.1977` n `8`; equity avg `-0.0696` n `67`; fx avg `0.0713` n `6`; index avg `-0.1197` n `23`; metal avg `1.386` n `18`; unknown avg `0.6069` n `396`
- 24h: commodity avg `0.3669` n `12`; crypto_alt avg `-1.7489` n `228`; crypto_major avg `0.5753` n `8`; equity avg `0.2643` n `67`; fx avg `0.0899` n `6`; index avg `-0.1091` n `23`; metal avg `1.2352` n `18`; unknown avg `1.2533` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
