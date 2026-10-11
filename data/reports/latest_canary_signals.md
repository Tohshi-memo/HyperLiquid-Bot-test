# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T23:52:26.698796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0961` n `13`; crypto_alt avg `0.0242` n `235`; crypto_major avg `0.0357` n `8`; equity avg `-0.0475` n `150`; fx avg `0.003` n `6`; index avg `-0.0365` n `26`; metal avg `-0.0384` n `20`; unknown avg `0.6881` n `1134`
- 1h: commodity avg `-0.4148` n `13`; crypto_alt avg `0.243` n `235`; crypto_major avg `0.1426` n `8`; equity avg `0.0877` n `150`; fx avg `0.0178` n `6`; index avg `0.0215` n `26`; metal avg `0.0497` n `20`; unknown avg `0.2597` n `1124`
- 4h: commodity avg `-0.331` n `13`; crypto_alt avg `0.2269` n `235`; crypto_major avg `0.0888` n `8`; equity avg `0.1095` n `150`; fx avg `-0.0035` n `6`; index avg `0.0157` n `26`; metal avg `-0.0015` n `20`; unknown avg `-0.2582` n `1090`
- 24h: commodity avg `-0.2405` n `13`; crypto_alt avg `2.1419` n `235`; crypto_major avg `0.8185` n `8`; equity avg `0.3815` n `150`; fx avg `0.0171` n `6`; index avg `0.0515` n `26`; metal avg `0.0658` n `20`; unknown avg `0.6398` n `957`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
