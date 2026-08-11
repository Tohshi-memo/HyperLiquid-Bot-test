# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T02:52:29.936121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.0547` n `230`; crypto_major avg `0.0034` n `8`; equity avg `0.0655` n `113`; fx avg `-0.0018` n `6`; index avg `0.0185` n `25`; metal avg `-0.0681` n `20`; unknown avg `-0.0515` n `785`
- 1h: commodity avg `-0.0239` n `12`; crypto_alt avg `-0.1821` n `230`; crypto_major avg `-0.0708` n `8`; equity avg `0.0426` n `113`; fx avg `0.0064` n `6`; index avg `0.0021` n `25`; metal avg `-0.2178` n `20`; unknown avg `-0.1135` n `785`
- 4h: commodity avg `0.0376` n `12`; crypto_alt avg `0.2068` n `230`; crypto_major avg `0.1057` n `8`; equity avg `0.4671` n `113`; fx avg `-0.0329` n `6`; index avg `0.1284` n `25`; metal avg `0.0236` n `20`; unknown avg `-0.2638` n `785`
- 24h: commodity avg `0.8346` n `12`; crypto_alt avg `-0.6233` n `230`; crypto_major avg `-0.7365` n `8`; equity avg `-1.0205` n `113`; fx avg `0.1119` n `6`; index avg `0.0222` n `25`; metal avg `0.522` n `20`; unknown avg `103.7992` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1705`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
