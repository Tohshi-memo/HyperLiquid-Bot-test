# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T03:07:28.853834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.028` n `12`; crypto_alt avg `0.0336` n `233`; crypto_major avg `-0.1131` n `8`; equity avg `-0.0055` n `136`; fx avg `0.0006` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.1143` n `836`
- 1h: commodity avg `-0.0088` n `12`; crypto_alt avg `0.0049` n `233`; crypto_major avg `-0.001` n `8`; equity avg `-0.0391` n `136`; fx avg `0.0072` n `6`; index avg `-0.0211` n `26`; metal avg `-0.0005` n `20`; unknown avg `-0.1156` n `812`
- 4h: commodity avg `-0.0431` n `12`; crypto_alt avg `0.6733` n `233`; crypto_major avg `0.0661` n `8`; equity avg `-0.1047` n `136`; fx avg `0.0024` n `6`; index avg `-0.0324` n `26`; metal avg `0.0046` n `20`; unknown avg `3.7122` n `806`
- 24h: commodity avg `-0.0274` n `12`; crypto_alt avg `1.0124` n `233`; crypto_major avg `0.138` n `8`; equity avg `-0.4831` n `136`; fx avg `-0.0081` n `6`; index avg `-0.0564` n `26`; metal avg `0.0294` n `20`; unknown avg `-0.2871` n `706`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0451`, n `668`, weak_sample_signal
