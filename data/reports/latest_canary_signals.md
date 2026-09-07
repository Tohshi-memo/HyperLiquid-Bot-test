# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T17:37:27.320222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0177` n `12`; crypto_alt avg `-0.1118` n `232`; crypto_major avg `-0.1132` n `8`; equity avg `0.024` n `134`; fx avg `-0.0076` n `6`; index avg `-0.0042` n `26`; metal avg `-0.0061` n `20`; unknown avg `-0.2412` n `796`
- 1h: commodity avg `0.0298` n `12`; crypto_alt avg `0.0465` n `232`; crypto_major avg `0.0939` n `8`; equity avg `0.1552` n `134`; fx avg `-0.0055` n `6`; index avg `0.0302` n `26`; metal avg `-0.0118` n `20`; unknown avg `0.225` n `794`
- 4h: commodity avg `-0.0168` n `12`; crypto_alt avg `-0.8107` n `232`; crypto_major avg `-0.8182` n `8`; equity avg `0.0914` n `134`; fx avg `-0.0462` n `6`; index avg `0.0413` n `26`; metal avg `0.1169` n `20`; unknown avg `-0.3392` n `788`
- 24h: commodity avg `0.1371` n `12`; crypto_alt avg `0.2915` n `232`; crypto_major avg `-0.9096` n `8`; equity avg `0.5165` n `134`; fx avg `-0.1211` n `6`; index avg `0.0874` n `26`; metal avg `0.0132` n `20`; unknown avg `1.0322` n `681`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
