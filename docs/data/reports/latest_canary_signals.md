# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T19:38:14.944581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.022` n `13`; crypto_alt avg `-0.1588` n `235`; crypto_major avg `-0.1584` n `8`; equity avg `0.0726` n `150`; fx avg `-0.0012` n `6`; index avg `0.0021` n `26`; metal avg `-0.0256` n `20`; unknown avg `16.9246` n `1077`
- 1h: commodity avg `0.108` n `13`; crypto_alt avg `0.1026` n `235`; crypto_major avg `0.1112` n `8`; equity avg `-0.0229` n `150`; fx avg `0.0111` n `6`; index avg `-0.0192` n `26`; metal avg `-0.0734` n `20`; unknown avg `18.6676` n `1075`
- 4h: commodity avg `-0.2268` n `13`; crypto_alt avg `0.5527` n `235`; crypto_major avg `-0.1595` n `8`; equity avg `0.0867` n `150`; fx avg `0.0045` n `6`; index avg `0.0269` n `26`; metal avg `-0.1256` n `20`; unknown avg `10.9808` n `1068`
- 24h: commodity avg `0.3618` n `13`; crypto_alt avg `-4.2388` n `235`; crypto_major avg `-3.2422` n `8`; equity avg `-1.2789` n `150`; fx avg `-0.1667` n `6`; index avg `-0.2111` n `26`; metal avg `-0.7467` n `20`; unknown avg `27.6962` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
