# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T23:52:27.050573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.1362` n `234`; crypto_major avg `-0.004` n `8`; equity avg `0.031` n `140`; fx avg `0.0031` n `6`; index avg `0.0034` n `26`; metal avg `0.0035` n `20`; unknown avg `6.331` n `943`
- 1h: commodity avg `0.0398` n `12`; crypto_alt avg `0.2415` n `234`; crypto_major avg `0.1458` n `8`; equity avg `0.007` n `140`; fx avg `-0.0194` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0024` n `20`; unknown avg `2.6722` n `925`
- 4h: commodity avg `0.0917` n `12`; crypto_alt avg `-0.2738` n `234`; crypto_major avg `-0.5153` n `8`; equity avg `0.0265` n `140`; fx avg `-0.0437` n `6`; index avg `0.0049` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.8256` n `903`
- 24h: commodity avg `-0.0639` n `12`; crypto_alt avg `1.2175` n `234`; crypto_major avg `0.1803` n `8`; equity avg `-0.015` n `140`; fx avg `-0.0945` n `6`; index avg `0.0171` n `26`; metal avg `-0.0029` n `20`; unknown avg `4.9942` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
