# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T22:07:28.131038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0551` n `13`; crypto_alt avg `0.071` n `235`; crypto_major avg `0.1199` n `8`; equity avg `0.0175` n `150`; fx avg `-0.0133` n `6`; index avg `0.0143` n `26`; metal avg `-0.0374` n `20`; unknown avg `0.0657` n `1132`
- 1h: commodity avg `-0.0803` n `13`; crypto_alt avg `-0.0556` n `235`; crypto_major avg `-0.0915` n `8`; equity avg `-0.0041` n `150`; fx avg `-0.0064` n `6`; index avg `0.0096` n `26`; metal avg `-0.0281` n `20`; unknown avg `0.0497` n `1118`
- 4h: commodity avg `0.0424` n `13`; crypto_alt avg `-0.3325` n `235`; crypto_major avg `-0.5398` n `8`; equity avg `-0.0421` n `150`; fx avg `-0.0255` n `6`; index avg `0.0073` n `26`; metal avg `-0.0139` n `20`; unknown avg `0.1496` n `1088`
- 24h: commodity avg `-0.0076` n `13`; crypto_alt avg `1.4178` n `235`; crypto_major avg `0.5034` n `8`; equity avg `0.2155` n `150`; fx avg `-0.0071` n `6`; index avg `0.0377` n `26`; metal avg `0.0444` n `20`; unknown avg `0.6377` n `965`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
