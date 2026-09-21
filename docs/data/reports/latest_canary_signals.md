# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T16:07:33.644224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0622` n `12`; crypto_alt avg `-0.1735` n `234`; crypto_major avg `-0.4893` n `8`; equity avg `-0.0349` n `140`; fx avg `0.0014` n `6`; index avg `-0.0017` n `26`; metal avg `0.045` n `20`; unknown avg `0.0622` n `928`
- 1h: commodity avg `-0.0909` n `12`; crypto_alt avg `-0.4916` n `234`; crypto_major avg `-0.4713` n `8`; equity avg `0.1626` n `140`; fx avg `-0.0042` n `6`; index avg `0.0499` n `26`; metal avg `0.0308` n `20`; unknown avg `-0.2601` n `928`
- 4h: commodity avg `-0.2141` n `12`; crypto_alt avg `0.1601` n `234`; crypto_major avg `0.6193` n `8`; equity avg `0.7267` n `140`; fx avg `-0.0133` n `6`; index avg `0.1805` n `26`; metal avg `-0.096` n `20`; unknown avg `10.8268` n `870`
- 24h: commodity avg `-1.0405` n `12`; crypto_alt avg `5.8585` n `234`; crypto_major avg `5.8055` n `8`; equity avg `2.6958` n `140`; fx avg `-0.0647` n `6`; index avg `0.5763` n `26`; metal avg `0.0721` n `20`; unknown avg `4.5335` n `723`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
