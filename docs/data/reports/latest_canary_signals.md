# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T04:52:24.044826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.1499` n `231`; crypto_major avg `-0.1631` n `8`; equity avg `-0.0162` n `128`; fx avg `-0.0006` n `6`; index avg `0.0053` n `26`; metal avg `-0.006` n `20`; unknown avg `0.1301` n `793`
- 1h: commodity avg `0.0245` n `12`; crypto_alt avg `-0.3555` n `231`; crypto_major avg `-0.2539` n `8`; equity avg `-0.0159` n `128`; fx avg `-0.0006` n `6`; index avg `0.0028` n `26`; metal avg `-0.0088` n `20`; unknown avg `-0.2432` n `793`
- 4h: commodity avg `0.0118` n `12`; crypto_alt avg `-0.3023` n `231`; crypto_major avg `-0.3974` n `8`; equity avg `0.0223` n `128`; fx avg `0.0048` n `6`; index avg `-0.0066` n `26`; metal avg `-0.0045` n `20`; unknown avg `-0.5873` n `793`
- 24h: commodity avg `-0.0144` n `12`; crypto_alt avg `-0.0452` n `231`; crypto_major avg `0.3875` n `8`; equity avg `0.2953` n `128`; fx avg `-0.0157` n `6`; index avg `0.0476` n `26`; metal avg `0.0931` n `20`; unknown avg `0.0647` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
