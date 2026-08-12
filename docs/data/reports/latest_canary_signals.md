# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T06:37:27.863780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.089` n `12`; crypto_alt avg `-0.1507` n `230`; crypto_major avg `-0.0112` n `8`; equity avg `0.0394` n `113`; fx avg `0.0038` n `6`; index avg `0.0211` n `25`; metal avg `0.0382` n `20`; unknown avg `0.0033` n `786`
- 1h: commodity avg `-0.0709` n `12`; crypto_alt avg `-0.273` n `230`; crypto_major avg `-0.2438` n `8`; equity avg `-0.056` n `113`; fx avg `0.0179` n `6`; index avg `0.0036` n `25`; metal avg `0.0347` n `20`; unknown avg `-0.0292` n `770`
- 4h: commodity avg `-0.0841` n `12`; crypto_alt avg `-0.4475` n `230`; crypto_major avg `-0.227` n `8`; equity avg `0.0193` n `113`; fx avg `-0.0004` n `6`; index avg `0.0122` n `25`; metal avg `-0.0125` n `20`; unknown avg `-0.0362` n `770`
- 24h: commodity avg `-0.0702` n `12`; crypto_alt avg `-1.2112` n `230`; crypto_major avg `0.6064` n `8`; equity avg `1.9034` n `113`; fx avg `-0.0106` n `6`; index avg `0.1859` n `25`; metal avg `0.1843` n `20`; unknown avg `-0.039` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2213`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2191`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2116`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2097`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
