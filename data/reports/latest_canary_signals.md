# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T19:37:28.982250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0262` n `12`; crypto_alt avg `0.1228` n `234`; crypto_major avg `-0.0436` n `8`; equity avg `0.0098` n `140`; fx avg `-0.0032` n `6`; index avg `0.0001` n `26`; metal avg `-0.0048` n `20`; unknown avg `3.9174` n `943`
- 1h: commodity avg `-0.008` n `12`; crypto_alt avg `0.0644` n `234`; crypto_major avg `-0.1469` n `8`; equity avg `0.028` n `140`; fx avg `-0.0051` n `6`; index avg `-0.001` n `26`; metal avg `-0.0016` n `20`; unknown avg `54.9997` n `941`
- 4h: commodity avg `0.0506` n `12`; crypto_alt avg `0.2659` n `234`; crypto_major avg `-0.31` n `8`; equity avg `0.0726` n `140`; fx avg `-0.0106` n `6`; index avg `0.0189` n `26`; metal avg `-0.0035` n `20`; unknown avg `231.8098` n `883`
- 24h: commodity avg `0.035` n `12`; crypto_alt avg `1.868` n `234`; crypto_major avg `0.2823` n `8`; equity avg `0.2683` n `140`; fx avg `-0.001` n `6`; index avg `0.0725` n `26`; metal avg `-0.0403` n `20`; unknown avg `6.9062` n `792`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1726`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
