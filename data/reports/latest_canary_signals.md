# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T12:52:26.685806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `10`; crypto_alt avg `0.0427` n `228`; crypto_major avg `0.0279` n `7`; equity avg `0.0213` n `108`; fx avg `-0.011` n `6`; index avg `0.0114` n `24`; metal avg `0.0108` n `13`; unknown avg `-0.0071` n `769`
- 1h: commodity avg `-0.0042` n `12`; crypto_alt avg `0.0439` n `230`; crypto_major avg `-0.0595` n `8`; equity avg `0.0188` n `112`; fx avg `0.0037` n `6`; index avg `0.0106` n `25`; metal avg `0.0101` n `20`; unknown avg `0.0364` n `785`
- 4h: commodity avg `-0.0612` n `12`; crypto_alt avg `0.2479` n `230`; crypto_major avg `0.1143` n `8`; equity avg `0.0242` n `112`; fx avg `0.0008` n `6`; index avg `0.0083` n `25`; metal avg `0.0041` n `20`; unknown avg `0.0066` n `785`
- 24h: commodity avg `0.1348` n `12`; crypto_alt avg `1.0644` n `230`; crypto_major avg `0.0767` n `8`; equity avg `0.4043` n `112`; fx avg `-0.0161` n `6`; index avg `0.0402` n `25`; metal avg `0.0465` n `20`; unknown avg `0.2619` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0482`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
