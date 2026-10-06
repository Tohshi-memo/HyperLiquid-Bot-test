# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T08:52:47.376440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0289` n `13`; crypto_alt avg `-0.1086` n `235`; crypto_major avg `0.0643` n `8`; equity avg `0.0317` n `149`; fx avg `0.0067` n `6`; index avg `0.013` n `26`; metal avg `-0.0393` n `20`; unknown avg `0.6197` n `1074`
- 1h: commodity avg `-0.1327` n `13`; crypto_alt avg `0.1175` n `235`; crypto_major avg `0.2714` n `8`; equity avg `0.0477` n `149`; fx avg `0.0188` n `6`; index avg `0.0252` n `26`; metal avg `0.0667` n `20`; unknown avg `0.4811` n `1056`
- 4h: commodity avg `-0.4149` n `13`; crypto_alt avg `0.4108` n `235`; crypto_major avg `0.1709` n `8`; equity avg `0.2264` n `149`; fx avg `-0.0025` n `6`; index avg `0.0837` n `26`; metal avg `0.1244` n `20`; unknown avg `-0.0786` n `976`
- 24h: commodity avg `-0.5578` n `13`; crypto_alt avg `-0.8922` n `235`; crypto_major avg `-0.58` n `8`; equity avg `0.3421` n `149`; fx avg `0.0154` n `6`; index avg `0.1927` n `26`; metal avg `-0.1707` n `20`; unknown avg `0.0349` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
