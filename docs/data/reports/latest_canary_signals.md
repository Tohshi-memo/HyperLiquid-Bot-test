# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T08:07:31.517738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0625` n `13`; crypto_alt avg `-0.0082` n `235`; crypto_major avg `-0.0453` n `8`; equity avg `-0.0397` n `150`; fx avg `0.017` n `6`; index avg `0.0094` n `26`; metal avg `0.0537` n `20`; unknown avg `0.0845` n `1059`
- 1h: commodity avg `0.0434` n `13`; crypto_alt avg `0.2013` n `235`; crypto_major avg `0.0896` n `8`; equity avg `0.0153` n `150`; fx avg `0.0488` n `6`; index avg `0.0287` n `26`; metal avg `0.0201` n `20`; unknown avg `-0.1512` n `1059`
- 4h: commodity avg `0.3639` n `13`; crypto_alt avg `-0.0515` n `235`; crypto_major avg `-0.2209` n `8`; equity avg `-0.6691` n `150`; fx avg `0.0347` n `6`; index avg `-0.1048` n `26`; metal avg `-0.2026` n `20`; unknown avg `0.1322` n `1031`
- 24h: commodity avg `0.6306` n `13`; crypto_alt avg `-0.9796` n `235`; crypto_major avg `-2.2422` n `8`; equity avg `-1.8486` n `150`; fx avg `0.0352` n `6`; index avg `-0.3081` n `26`; metal avg `-0.2367` n `20`; unknown avg `416.7845` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
