# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T02:52:20.253755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0613` n `12`; crypto_alt avg `0.039` n `228`; crypto_major avg `-0.1848` n `8`; equity avg `-0.0386` n `69`; fx avg `-0.0023` n `6`; index avg `0.0286` n `23`; metal avg `-0.0437` n `18`; unknown avg `0.7405` n `422`
- 1h: commodity avg `0.0083` n `12`; crypto_alt avg `0.1914` n `228`; crypto_major avg `0.3192` n `8`; equity avg `0.3928` n `69`; fx avg `-0.0149` n `6`; index avg `0.1062` n `23`; metal avg `0.3676` n `18`; unknown avg `0.6524` n `422`
- 4h: commodity avg `-0.4028` n `12`; crypto_alt avg `-0.7482` n `228`; crypto_major avg `-0.5379` n `8`; equity avg `-0.4264` n `69`; fx avg `0.0491` n `6`; index avg `-0.4651` n `23`; metal avg `0.043` n `18`; unknown avg `0.4131` n `422`
- 24h: commodity avg `-0.2617` n `12`; crypto_alt avg `-1.4866` n `228`; crypto_major avg `-1.4878` n `8`; equity avg `-0.7154` n `69`; fx avg `-0.0154` n `6`; index avg `-0.7953` n `23`; metal avg `-0.3274` n `18`; unknown avg `2.7393` n `406`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
