# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T23:42:14.866945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `-0.1927` n `228`; crypto_major avg `-0.1551` n `8`; equity avg `-0.0162` n `65`; fx avg `-0.0017` n `5`; index avg `0.0474` n `23`; metal avg `-0.0468` n `18`; unknown avg `0.0859` n `375`
- 1h: commodity avg `0.0475` n `12`; crypto_alt avg `-0.2997` n `228`; crypto_major avg `-0.3161` n `8`; equity avg `0.0063` n `65`; fx avg `0.0008` n `5`; index avg `0.0595` n `23`; metal avg `-0.1824` n `18`; unknown avg `-0.1663` n `375`
- 4h: commodity avg `-0.2743` n `12`; crypto_alt avg `0.27` n `228`; crypto_major avg `-0.1838` n `8`; equity avg `0.6361` n `65`; fx avg `-0.039` n `5`; index avg `0.1739` n `23`; metal avg `-0.4413` n `18`; unknown avg `-0.5047` n `375`
- 24h: commodity avg `-0.8226` n `12`; crypto_alt avg `3.2678` n `228`; crypto_major avg `1.4318` n `8`; equity avg `4.0897` n `65`; fx avg `0.2255` n `5`; index avg `1.641` n `23`; metal avg `0.7145` n `18`; unknown avg `1.0123` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
