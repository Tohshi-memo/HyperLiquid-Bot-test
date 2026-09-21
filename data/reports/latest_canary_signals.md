# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T07:16:14.021774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.1929` n `234`; crypto_major avg `-0.0691` n `8`; equity avg `-0.0124` n `140`; fx avg `0.0171` n `6`; index avg `-0.006` n `26`; metal avg `-0.0418` n `20`; unknown avg `2.464` n `944`
- 1h: commodity avg `0.0062` n `12`; crypto_alt avg `-0.1225` n `234`; crypto_major avg `-0.2089` n `8`; equity avg `0.1443` n `140`; fx avg `-0.0077` n `6`; index avg `0.0329` n `26`; metal avg `0.0118` n `20`; unknown avg `1.7078` n `920`
- 4h: commodity avg `0.0606` n `12`; crypto_alt avg `0.5626` n `234`; crypto_major avg `0.2329` n `8`; equity avg `0.1516` n `140`; fx avg `-0.0006` n `6`; index avg `0.0536` n `26`; metal avg `-0.0428` n `20`; unknown avg `2.2471` n `890`
- 24h: commodity avg `-0.5936` n `12`; crypto_alt avg `4.0402` n `234`; crypto_major avg `2.847` n `8`; equity avg `1.3102` n `140`; fx avg `-0.0397` n `6`; index avg `0.2807` n `26`; metal avg `-0.0194` n `20`; unknown avg `2.4478` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
