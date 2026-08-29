# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T14:37:27.711385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.0688` n `231`; crypto_major avg `0.0813` n `8`; equity avg `-0.0035` n `127`; fx avg `0.0082` n `6`; index avg `0.0027` n `26`; metal avg `-0.0068` n `20`; unknown avg `0.0851` n `793`
- 1h: commodity avg `-0.0094` n `12`; crypto_alt avg `0.4139` n `231`; crypto_major avg `0.2644` n `8`; equity avg `0.0098` n `127`; fx avg `0.0049` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.1946` n `793`
- 4h: commodity avg `0.0074` n `12`; crypto_alt avg `0.7131` n `231`; crypto_major avg `0.4316` n `8`; equity avg `-0.0213` n `127`; fx avg `-0.0006` n `6`; index avg `0.0036` n `26`; metal avg `0.0177` n `20`; unknown avg `0.1365` n `761`
- 24h: commodity avg `0.1029` n `12`; crypto_alt avg `-1.9735` n `231`; crypto_major avg `-2.3307` n `8`; equity avg `-1.3857` n `127`; fx avg `-0.0407` n `6`; index avg `-0.2138` n `26`; metal avg `-0.701` n `20`; unknown avg `-0.4787` n `743`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2054`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
