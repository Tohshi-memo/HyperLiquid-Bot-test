# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T08:07:24.351524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `0.0767` n `230`; crypto_major avg `0.019` n `8`; equity avg `0.0463` n `112`; fx avg `0.0006` n `6`; index avg `0.0221` n `25`; metal avg `-0.0136` n `20`; unknown avg `-0.0196` n `785`
- 1h: commodity avg `-0.0718` n `12`; crypto_alt avg `0.1184` n `230`; crypto_major avg `0.0569` n `8`; equity avg `0.1841` n `112`; fx avg `0.0018` n `6`; index avg `0.049` n `25`; metal avg `-0.0411` n `20`; unknown avg `0.0499` n `785`
- 4h: commodity avg `-0.0779` n `12`; crypto_alt avg `0.4259` n `230`; crypto_major avg `0.4768` n `8`; equity avg `0.3304` n `112`; fx avg `0.1011` n `6`; index avg `0.0709` n `25`; metal avg `0.1549` n `20`; unknown avg `57.2562` n `753`
- 24h: commodity avg `0.3113` n `12`; crypto_alt avg `0.8994` n `230`; crypto_major avg `0.1493` n `8`; equity avg `0.0732` n `112`; fx avg `0.2059` n `6`; index avg `0.0881` n `25`; metal avg `-0.0224` n `20`; unknown avg `56.9377` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
