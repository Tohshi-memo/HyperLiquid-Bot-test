# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T11:37:24.916482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.03` n `12`; crypto_alt avg `-0.0721` n `232`; crypto_major avg `-0.0053` n `8`; equity avg `0.0003` n `134`; fx avg `0.0057` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0423` n `20`; unknown avg `0.0275` n `796`
- 1h: commodity avg `0.2533` n `12`; crypto_alt avg `0.1893` n `232`; crypto_major avg `0.0655` n `8`; equity avg `-0.078` n `134`; fx avg `0.0268` n `6`; index avg `-0.0472` n `26`; metal avg `-0.0739` n `20`; unknown avg `-0.1076` n `794`
- 4h: commodity avg `0.2038` n `12`; crypto_alt avg `0.9719` n `232`; crypto_major avg `0.497` n `8`; equity avg `0.0032` n `134`; fx avg `-0.0423` n `6`; index avg `-0.0593` n `26`; metal avg `-0.0769` n `20`; unknown avg `1.492` n `784`
- 24h: commodity avg `0.2338` n `12`; crypto_alt avg `-0.1104` n `232`; crypto_major avg `-0.7618` n `8`; equity avg `0.2026` n `134`; fx avg `-0.0823` n `6`; index avg `-0.0253` n `26`; metal avg `-0.2215` n `20`; unknown avg `229.8372` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1941`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
