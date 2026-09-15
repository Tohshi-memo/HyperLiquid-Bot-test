# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T23:22:28.517846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `0.3122` n `234`; crypto_major avg `0.2837` n `8`; equity avg `0.004` n `137`; fx avg `-0.0018` n `6`; index avg `-0.0068` n `27`; metal avg `-0.0092` n `20`; unknown avg `-0.0708` n `919`
- 1h: commodity avg `-0.0035` n `12`; crypto_alt avg `1.0885` n `234`; crypto_major avg `0.9737` n `8`; equity avg `0.0803` n `137`; fx avg `0.0027` n `6`; index avg `0.0021` n `27`; metal avg `-0.0182` n `20`; unknown avg `1.4123` n `909`
- 4h: commodity avg `0.0364` n `12`; crypto_alt avg `-0.4792` n `234`; crypto_major avg `-0.2507` n `8`; equity avg `-0.0921` n `137`; fx avg `0.0108` n `6`; index avg `0.0306` n `27`; metal avg `-0.0287` n `20`; unknown avg `1.703` n `845`
- 24h: commodity avg `0.4399` n `12`; crypto_alt avg `-3.446` n `234`; crypto_major avg `-3.7802` n `8`; equity avg `-1.2722` n `137`; fx avg `0.2487` n `6`; index avg `-0.0742` n `27`; metal avg `0.1994` n `20`; unknown avg `2.1105` n `802`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
