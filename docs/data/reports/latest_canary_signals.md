# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T05:52:27.551784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0314` n `13`; crypto_alt avg `-0.2903` n `235`; crypto_major avg `-0.2971` n `8`; equity avg `-0.019` n `150`; fx avg `0.0006` n `6`; index avg `-0.0063` n `26`; metal avg `-0.0645` n `20`; unknown avg `2.4448` n `1078`
- 1h: commodity avg `0.0037` n `13`; crypto_alt avg `0.2931` n `235`; crypto_major avg `0.2256` n `8`; equity avg `0.3945` n `150`; fx avg `0.0225` n `6`; index avg `0.0281` n `26`; metal avg `0.1126` n `20`; unknown avg `0.7739` n `1076`
- 4h: commodity avg `-0.0693` n `13`; crypto_alt avg `0.7663` n `235`; crypto_major avg `0.4872` n `8`; equity avg `0.3921` n `150`; fx avg `0.0422` n `6`; index avg `0.0614` n `26`; metal avg `0.1384` n `20`; unknown avg `0.7539` n `1068`
- 24h: commodity avg `0.0458` n `13`; crypto_alt avg `-1.0501` n `235`; crypto_major avg `-1.9754` n `8`; equity avg `-1.2074` n `150`; fx avg `0.1412` n `6`; index avg `-0.1188` n `26`; metal avg `0.3731` n `20`; unknown avg `5.5617` n `989`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
