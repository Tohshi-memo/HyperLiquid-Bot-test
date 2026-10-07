# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T20:37:31.165697+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0854` n `13`; crypto_alt avg `-0.0656` n `235`; crypto_major avg `-0.1913` n `8`; equity avg `-0.0105` n `150`; fx avg `-0.0011` n `6`; index avg `-0.0065` n `26`; metal avg `0.0037` n `20`; unknown avg `0.4984` n `1033`
- 1h: commodity avg `0.1079` n `13`; crypto_alt avg `0.2249` n `235`; crypto_major avg `-0.0453` n `8`; equity avg `0.0071` n `150`; fx avg `0.0085` n `6`; index avg `0.0011` n `26`; metal avg `0.0375` n `20`; unknown avg `0.2039` n `1005`
- 4h: commodity avg `0.0691` n `13`; crypto_alt avg `0.1853` n `235`; crypto_major avg `-0.3214` n `8`; equity avg `0.1308` n `150`; fx avg `0.0127` n `6`; index avg `0.0187` n `26`; metal avg `-0.0726` n `20`; unknown avg `0.5903` n `1004`
- 24h: commodity avg `0.409` n `13`; crypto_alt avg `-4.2512` n `235`; crypto_major avg `-3.5153` n `8`; equity avg `-1.4107` n `150`; fx avg `-0.1541` n `6`; index avg `-0.2192` n `26`; metal avg `-0.6886` n `20`; unknown avg `1.2618` n `972`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
