# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T23:37:27.721915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `-0.1611` n `230`; crypto_major avg `-0.0742` n `8`; equity avg `-0.0532` n `112`; fx avg `-0.0045` n `6`; index avg `-0.0156` n `25`; metal avg `-0.0335` n `20`; unknown avg `-0.041` n `785`
- 1h: commodity avg `0.0303` n `12`; crypto_alt avg `-0.8188` n `230`; crypto_major avg `-0.4461` n `8`; equity avg `0.0133` n `112`; fx avg `-0.0039` n `6`; index avg `-0.0012` n `25`; metal avg `0.0089` n `20`; unknown avg `0.1164` n `785`
- 4h: commodity avg `0.3383` n `12`; crypto_alt avg `-0.8864` n `230`; crypto_major avg `-0.8222` n `8`; equity avg `-0.2018` n `112`; fx avg `-0.0031` n `6`; index avg `-0.0648` n `25`; metal avg `-0.1511` n `20`; unknown avg `0.2785` n `785`
- 24h: commodity avg `0.4554` n `12`; crypto_alt avg `0.4743` n `230`; crypto_major avg `-0.4437` n `8`; equity avg `-0.0254` n `112`; fx avg `-0.0023` n `6`; index avg `-0.0321` n `25`; metal avg `-0.0879` n `20`; unknown avg `-0.4378` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
