# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T05:07:22.274640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0285` n `12`; crypto_alt avg `0.2031` n `228`; crypto_major avg `0.1423` n `8`; equity avg `-0.0577` n `67`; fx avg `-0.0038` n `6`; index avg `-0.0361` n `23`; metal avg `-0.0622` n `18`; unknown avg `-0.1885` n `418`
- 1h: commodity avg `0.1373` n `12`; crypto_alt avg `0.1751` n `228`; crypto_major avg `0.2554` n `8`; equity avg `-0.0999` n `67`; fx avg `-0.0029` n `6`; index avg `-0.0942` n `23`; metal avg `0.1306` n `18`; unknown avg `-0.1593` n `418`
- 4h: commodity avg `-0.3323` n `12`; crypto_alt avg `-1.0108` n `228`; crypto_major avg `-0.2039` n `8`; equity avg `-0.2218` n `67`; fx avg `-0.0524` n `6`; index avg `-0.1384` n `23`; metal avg `-0.1999` n `18`; unknown avg `-0.6213` n `418`
- 24h: commodity avg `-0.4258` n `12`; crypto_alt avg `-1.0732` n `228`; crypto_major avg `-0.3546` n `8`; equity avg `0.5748` n `67`; fx avg `-0.0757` n `6`; index avg `0.7962` n `23`; metal avg `0.1146` n `18`; unknown avg `0.5477` n `397`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
