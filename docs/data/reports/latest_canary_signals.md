# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T08:07:24.562573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0431` n `12`; crypto_alt avg `0.042` n `231`; crypto_major avg `0.0963` n `8`; equity avg `-0.1013` n `127`; fx avg `0.009` n `6`; index avg `-0.0244` n `26`; metal avg `0.0474` n `20`; unknown avg `0.0038` n `792`
- 1h: commodity avg `-0.0869` n `12`; crypto_alt avg `0.0095` n `231`; crypto_major avg `0.1428` n `8`; equity avg `-0.1043` n `127`; fx avg `-0.0063` n `6`; index avg `-0.0197` n `26`; metal avg `0.072` n `20`; unknown avg `0.1493` n `792`
- 4h: commodity avg `-0.0849` n `12`; crypto_alt avg `0.1923` n `231`; crypto_major avg `0.1556` n `8`; equity avg `-0.4133` n `127`; fx avg `-0.0538` n `6`; index avg `-0.0397` n `26`; metal avg `0.4408` n `20`; unknown avg `0.0399` n `760`
- 24h: commodity avg `0.3636` n `12`; crypto_alt avg `-0.3982` n `231`; crypto_major avg `0.6265` n `8`; equity avg `-1.0167` n `127`; fx avg `-0.0735` n `6`; index avg `-0.0335` n `26`; metal avg `0.5297` n `20`; unknown avg `0.4563` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
