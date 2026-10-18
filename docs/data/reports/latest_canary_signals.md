# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T23:22:32.915232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0292` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0165` n `13`; crypto_alt avg `0.2048` n `237`; crypto_major avg `0.0908` n `8`; equity avg `0.1486` n `151`; fx avg `-0.0043` n `6`; index avg `0.013` n `26`; metal avg `0.0055` n `20`; unknown avg `0.1944` n `1194`
- 1h: commodity avg `-0.0627` n `13`; crypto_alt avg `0.6623` n `237`; crypto_major avg `0.3631` n `8`; equity avg `0.3898` n `151`; fx avg `-0.017` n `6`; index avg `0.0006` n `26`; metal avg `0.0285` n `20`; unknown avg `3.5041` n `1192`
- 4h: commodity avg `-0.3317` n `13`; crypto_alt avg `1.7502` n `237`; crypto_major avg `1.6975` n `8`; equity avg `1.4025` n `151`; fx avg `-0.0259` n `6`; index avg `0.2496` n `26`; metal avg `0.2163` n `20`; unknown avg `19.5999` n `1090`
- 24h: commodity avg `-0.2876` n `13`; crypto_alt avg `-1.6716` n `236`; crypto_major avg `0.4626` n `8`; equity avg `1.0687` n `151`; fx avg `-0.0278` n `6`; index avg `0.2049` n `26`; metal avg `0.2178` n `20`; unknown avg `2.0757` n `961`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2005`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1376`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0962`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0887`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0755`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.072`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
