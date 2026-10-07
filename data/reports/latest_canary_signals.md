# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T19:52:31.917525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0332` n `13`; crypto_alt avg `0.04` n `235`; crypto_major avg `-0.106` n `8`; equity avg `-0.0326` n `150`; fx avg `0.0001` n `6`; index avg `0.0039` n `26`; metal avg `-0.0179` n `20`; unknown avg `1.0013` n `1077`
- 1h: commodity avg `0.1214` n `13`; crypto_alt avg `-0.0405` n `235`; crypto_major avg `-0.2042` n `8`; equity avg `-0.112` n `150`; fx avg `0.0125` n `6`; index avg `-0.0195` n `26`; metal avg `-0.0987` n `20`; unknown avg `18.7259` n `1075`
- 4h: commodity avg `-0.1396` n `13`; crypto_alt avg `0.2717` n `235`; crypto_major avg `-0.2952` n `8`; equity avg `-0.0148` n `150`; fx avg `0.0128` n `6`; index avg `0.0177` n `26`; metal avg `-0.0897` n `20`; unknown avg `13.3801` n `1068`
- 24h: commodity avg `0.3839` n `13`; crypto_alt avg `-4.2942` n `235`; crypto_major avg `-3.4616` n `8`; equity avg `-1.3294` n `150`; fx avg `-0.163` n `6`; index avg `-0.2014` n `26`; metal avg `-0.7563` n `20`; unknown avg `25.8563` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
