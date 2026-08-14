# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T09:07:27.179695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0214` n `12`; crypto_alt avg `-0.0019` n `230`; crypto_major avg `-0.0001` n `8`; equity avg `-0.0786` n `113`; fx avg `0.0003` n `6`; index avg `-0.0084` n `25`; metal avg `0.0176` n `20`; unknown avg `-0.0195` n `787`
- 1h: commodity avg `-0.109` n `12`; crypto_alt avg `0.1292` n `230`; crypto_major avg `0.112` n `8`; equity avg `-0.0599` n `113`; fx avg `-0.0088` n `6`; index avg `0.0045` n `25`; metal avg `0.0591` n `20`; unknown avg `0.0193` n `787`
- 4h: commodity avg `0.1754` n `12`; crypto_alt avg `-0.2848` n `230`; crypto_major avg `-0.3059` n `8`; equity avg `0.3055` n `113`; fx avg `-0.0059` n `6`; index avg `0.0816` n `25`; metal avg `0.2463` n `20`; unknown avg `0.0633` n `755`
- 24h: commodity avg `0.0664` n `12`; crypto_alt avg `-0.5569` n `230`; crypto_major avg `-0.5958` n `8`; equity avg `1.6361` n `113`; fx avg `-0.0639` n `6`; index avg `0.3316` n `25`; metal avg `-0.0531` n `20`; unknown avg `0.8808` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2035`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
