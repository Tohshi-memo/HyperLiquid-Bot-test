# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T22:37:24.813349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `5.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1995` n `12`; crypto_alt avg `-0.2083` n `228`; crypto_major avg `-0.1555` n `8`; equity avg `-0.0479` n `69`; fx avg `0.0055` n `6`; index avg `-0.0133` n `23`; metal avg `0.0274` n `18`; unknown avg `-0.1262` n `422`
- 1h: commodity avg `0.2552` n `12`; crypto_alt avg `-0.4627` n `228`; crypto_major avg `-0.0772` n `8`; equity avg `-0.0626` n `69`; fx avg `-0.0208` n `6`; index avg `-0.0404` n `23`; metal avg `0.0063` n `18`; unknown avg `0.0721` n `422`
- 4h: commodity avg `0.2655` n `12`; crypto_alt avg `-1.0771` n `228`; crypto_major avg `-0.4349` n `8`; equity avg `-0.8289` n `69`; fx avg `-0.0245` n `6`; index avg `-0.5371` n `23`; metal avg `-0.2172` n `18`; unknown avg `-0.5227` n `422`
- 24h: commodity avg `0.2775` n `12`; crypto_alt avg `-0.6845` n `228`; crypto_major avg `-1.6938` n `8`; equity avg `-0.2875` n `69`; fx avg `0.0378` n `6`; index avg `-0.068` n `23`; metal avg `-0.0664` n `18`; unknown avg `1.5347` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
