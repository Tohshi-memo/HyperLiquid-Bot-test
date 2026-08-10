# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T09:22:28.484760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0496` n `12`; crypto_alt avg `-0.0217` n `230`; crypto_major avg `-0.0302` n `8`; equity avg `-0.0332` n `112`; fx avg `-0.0051` n `6`; index avg `-0.0088` n `25`; metal avg `-0.0025` n `20`; unknown avg `0.0457` n `785`
- 1h: commodity avg `0.0703` n `12`; crypto_alt avg `-0.0923` n `230`; crypto_major avg `-0.1569` n `8`; equity avg `-0.0735` n `112`; fx avg `0.0196` n `6`; index avg `-0.0102` n `25`; metal avg `-0.045` n `20`; unknown avg `0.0118` n `785`
- 4h: commodity avg `0.1355` n `12`; crypto_alt avg `0.2942` n `230`; crypto_major avg `0.3335` n `8`; equity avg `0.218` n `112`; fx avg `0.0933` n `6`; index avg `0.0256` n `25`; metal avg `0.0417` n `20`; unknown avg `57.3303` n `753`
- 24h: commodity avg `0.409` n `12`; crypto_alt avg `0.9755` n `230`; crypto_major avg `0.3105` n `8`; equity avg `-0.0064` n `112`; fx avg `0.2354` n `6`; index avg `0.0703` n `25`; metal avg `-0.0964` n `20`; unknown avg `57.005` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
