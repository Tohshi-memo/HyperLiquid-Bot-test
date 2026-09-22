# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T17:23:09.031518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `12`; crypto_alt avg `0.2178` n `234`; crypto_major avg `0.2381` n `8`; equity avg `-0.0188` n `140`; fx avg `0.0098` n `6`; index avg `-0.0126` n `26`; metal avg `-0.0366` n `20`; unknown avg `-0.0585` n `942`
- 1h: commodity avg `0.0227` n `12`; crypto_alt avg `1.1026` n `234`; crypto_major avg `0.8608` n `8`; equity avg `0.2546` n `140`; fx avg `-0.0043` n `6`; index avg `0.0236` n `26`; metal avg `0.095` n `20`; unknown avg `-0.2677` n `900`
- 4h: commodity avg `0.546` n `12`; crypto_alt avg `0.5772` n `234`; crypto_major avg `0.4429` n `8`; equity avg `0.9927` n `140`; fx avg `-0.0506` n `6`; index avg `0.0929` n `26`; metal avg `-0.092` n `20`; unknown avg `0.5256` n `858`
- 24h: commodity avg `0.3015` n `12`; crypto_alt avg `2.347` n `234`; crypto_major avg `1.5496` n `8`; equity avg `0.8879` n `140`; fx avg `-0.2698` n `6`; index avg `0.1006` n `26`; metal avg `0.0655` n `20`; unknown avg `0.2386` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
