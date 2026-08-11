# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T00:37:31.029828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.02` n `12`; crypto_alt avg `0.0393` n `230`; crypto_major avg `-0.0428` n `8`; equity avg `0.0803` n `113`; fx avg `-0.0411` n `6`; index avg `0.0375` n `25`; metal avg `-0.0096` n `20`; unknown avg `1.3234` n `785`
- 1h: commodity avg `0.0181` n `12`; crypto_alt avg `0.1952` n `230`; crypto_major avg `-0.0855` n `8`; equity avg `0.2049` n `113`; fx avg `-0.0469` n `6`; index avg `0.0217` n `25`; metal avg `0.0924` n `20`; unknown avg `1.2805` n `785`
- 4h: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.2459` n `230`; crypto_major avg `-0.5041` n `8`; equity avg `-0.0957` n `113`; fx avg `-0.0416` n `6`; index avg `-0.0039` n `25`; metal avg `0.1142` n `20`; unknown avg `0.0249` n `785`
- 24h: commodity avg `0.8146` n `12`; crypto_alt avg `-0.4103` n `230`; crypto_major avg `-0.6187` n `8`; equity avg `-1.5146` n `113`; fx avg `0.1578` n `6`; index avg `-0.0721` n `25`; metal avg `0.5188` n `20`; unknown avg `103.7302` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1917`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
