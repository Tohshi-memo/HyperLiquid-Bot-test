# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T11:37:30.085264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0203` n `12`; crypto_alt avg `-0.0638` n `230`; crypto_major avg `-0.0845` n `8`; equity avg `-0.0329` n `112`; fx avg `0.0018` n `6`; index avg `0.0171` n `25`; metal avg `-0.0299` n `20`; unknown avg `0.0132` n `782`
- 1h: commodity avg `-0.059` n `12`; crypto_alt avg `0.0661` n `230`; crypto_major avg `0.0795` n `8`; equity avg `0.1417` n `112`; fx avg `0.0183` n `6`; index avg `0.0346` n `25`; metal avg `-0.1252` n `20`; unknown avg `0.0013` n `782`
- 4h: commodity avg `-0.3691` n `12`; crypto_alt avg `0.1917` n `230`; crypto_major avg `0.7694` n `8`; equity avg `0.585` n `112`; fx avg `-0.0248` n `6`; index avg `0.068` n `25`; metal avg `0.0452` n `20`; unknown avg `0.252` n `782`
- 24h: commodity avg `0.1535` n `12`; crypto_alt avg `0.5445` n `230`; crypto_major avg `0.2255` n `8`; equity avg `2.0361` n `109`; fx avg `-0.0829` n `6`; index avg `0.0875` n `25`; metal avg `0.2143` n `20`; unknown avg `0.3406` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
