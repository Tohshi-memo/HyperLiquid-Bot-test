# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T12:52:26.813377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `-0.1486` n `228`; crypto_major avg `-0.0665` n `8`; equity avg `-0.3797` n `88`; fx avg `-0.0112` n `6`; index avg `-0.0326` n `23`; metal avg `0.0644` n `20`; unknown avg `-0.1439` n `765`
- 1h: commodity avg `-0.1276` n `12`; crypto_alt avg `-0.3087` n `228`; crypto_major avg `-0.2144` n `8`; equity avg `-0.9009` n `88`; fx avg `-0.0371` n `6`; index avg `-0.0989` n `23`; metal avg `-0.0461` n `20`; unknown avg `-0.0329` n `765`
- 4h: commodity avg `-0.0486` n `12`; crypto_alt avg `0.0049` n `228`; crypto_major avg `-0.6651` n `8`; equity avg `-0.7688` n `88`; fx avg `-0.0059` n `6`; index avg `-0.0589` n `23`; metal avg `0.4871` n `20`; unknown avg `-0.1387` n `765`
- 24h: commodity avg `-0.6552` n `12`; crypto_alt avg `0.9908` n `228`; crypto_major avg `0.1368` n `8`; equity avg `0.1149` n `88`; fx avg `0.0991` n `6`; index avg `-0.0807` n `23`; metal avg `-0.0843` n `20`; unknown avg `-0.1116` n `743`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
