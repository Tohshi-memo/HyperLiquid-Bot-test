# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T19:22:28.234357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `0.0866` n `234`; crypto_major avg `0.1322` n `8`; equity avg `-0.0598` n `140`; fx avg `-0.0069` n `6`; index avg `0.0076` n `26`; metal avg `0.0146` n `20`; unknown avg `2.6639` n `942`
- 1h: commodity avg `-0.0306` n `12`; crypto_alt avg `0.0269` n `234`; crypto_major avg `0.1019` n `8`; equity avg `0.0374` n `140`; fx avg `0.0048` n `6`; index avg `0.0316` n `26`; metal avg `0.0092` n `20`; unknown avg `2.6989` n `940`
- 4h: commodity avg `0.0005` n `12`; crypto_alt avg `-0.3329` n `234`; crypto_major avg `0.5736` n `8`; equity avg `0.4632` n `140`; fx avg `-0.0082` n `6`; index avg `0.1448` n `26`; metal avg `0.007` n `20`; unknown avg `-0.6839` n `928`
- 24h: commodity avg `-0.9793` n `12`; crypto_alt avg `3.9688` n `234`; crypto_major avg `5.4604` n `8`; equity avg `2.9774` n `140`; fx avg `-0.0532` n `6`; index avg `0.6593` n `26`; metal avg `0.0547` n `20`; unknown avg `3.6847` n `747`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
