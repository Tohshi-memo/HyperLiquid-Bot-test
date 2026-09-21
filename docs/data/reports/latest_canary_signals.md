# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T13:52:30.657169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0546` n `12`; crypto_alt avg `0.419` n `234`; crypto_major avg `0.7404` n `8`; equity avg `0.2817` n `140`; fx avg `-0.0056` n `6`; index avg `0.0442` n `26`; metal avg `-0.0446` n `20`; unknown avg `0.2102` n `944`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `-0.1317` n `234`; crypto_major avg `0.4573` n `8`; equity avg `0.1408` n `140`; fx avg `-0.0054` n `6`; index avg `0.0382` n `26`; metal avg `-0.0886` n `20`; unknown avg `106.2877` n `942`
- 4h: commodity avg `-0.1592` n `12`; crypto_alt avg `0.9748` n `234`; crypto_major avg `1.0834` n `8`; equity avg `0.2079` n `140`; fx avg `0.0213` n `6`; index avg `0.0664` n `26`; metal avg `0.1504` n `20`; unknown avg `11.7699` n `910`
- 24h: commodity avg `-0.8119` n `12`; crypto_alt avg `7.3428` n `234`; crypto_major avg `6.4388` n `8`; equity avg `2.2529` n `140`; fx avg `-0.0693` n `6`; index avg `0.4175` n `26`; metal avg `0.1494` n `20`; unknown avg `2.812` n `733`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
