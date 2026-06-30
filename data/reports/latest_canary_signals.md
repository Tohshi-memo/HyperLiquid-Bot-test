# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T01:07:27.925324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.2013` n `228`; crypto_major avg `-0.2457` n `8`; equity avg `-0.1224` n `88`; fx avg `0.0223` n `6`; index avg `-0.0283` n `23`; metal avg `-0.4812` n `20`; unknown avg `0.1137` n `765`
- 1h: commodity avg `-0.0145` n `12`; crypto_alt avg `-0.7666` n `228`; crypto_major avg `-0.9147` n `8`; equity avg `-0.5925` n `88`; fx avg `0.044` n `6`; index avg `-0.1954` n `23`; metal avg `-0.6592` n `20`; unknown avg `1.7951` n `765`
- 4h: commodity avg `-0.0399` n `12`; crypto_alt avg `-0.8356` n `228`; crypto_major avg `-1.0906` n `8`; equity avg `-0.4933` n `88`; fx avg `0.1021` n `6`; index avg `-0.1902` n `23`; metal avg `-0.7246` n `20`; unknown avg `1.3524` n `763`
- 24h: commodity avg `-0.2664` n `12`; crypto_alt avg `0.3951` n `228`; crypto_major avg `1.4735` n `8`; equity avg `1.5535` n `88`; fx avg `0.2549` n `6`; index avg `0.1055` n `23`; metal avg `-1.0679` n `20`; unknown avg `1.9341` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
