# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T23:21:39.036116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0217` n `12`; crypto_alt avg `0.0143` n `230`; crypto_major avg `-0.0019` n `8`; equity avg `-0.0018` n `113`; fx avg `0.0025` n `6`; index avg `0.0085` n `25`; metal avg `0.0436` n `20`; unknown avg `0.023` n `787`
- 1h: commodity avg `0.0256` n `12`; crypto_alt avg `-0.0718` n `230`; crypto_major avg `-0.2095` n `8`; equity avg `0.0059` n `113`; fx avg `0.0022` n `6`; index avg `0.001` n `25`; metal avg `0.0533` n `20`; unknown avg `0.2033` n `787`
- 4h: commodity avg `-0.002` n `12`; crypto_alt avg `0.267` n `230`; crypto_major avg `-0.049` n `8`; equity avg `0.0491` n `113`; fx avg `0.0036` n `6`; index avg `0.0113` n `25`; metal avg `0.0744` n `20`; unknown avg `0.1147` n `787`
- 24h: commodity avg `-0.4428` n `12`; crypto_alt avg `0.6894` n `230`; crypto_major avg `0.7085` n `8`; equity avg `1.6439` n `113`; fx avg `0.0241` n `6`; index avg `0.3254` n `25`; metal avg `-0.4354` n `20`; unknown avg `0.1682` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2441`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
