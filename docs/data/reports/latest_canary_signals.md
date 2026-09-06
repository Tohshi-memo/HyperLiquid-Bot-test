# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T05:22:25.799707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0292` n `12`; crypto_alt avg `0.1101` n `232`; crypto_major avg `0.0145` n `8`; equity avg `0.009` n `134`; fx avg `0.0108` n `6`; index avg `0.0025` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.0894` n `790`
- 1h: commodity avg `0.0071` n `12`; crypto_alt avg `0.4606` n `232`; crypto_major avg `0.1934` n `8`; equity avg `0.013` n `134`; fx avg `0.014` n `6`; index avg `-0.0021` n `26`; metal avg `0.0022` n `20`; unknown avg `0.0873` n `776`
- 4h: commodity avg `0.0113` n `12`; crypto_alt avg `0.157` n `232`; crypto_major avg `0.5101` n `8`; equity avg `0.0379` n `134`; fx avg `-0.0177` n `6`; index avg `0.0062` n `26`; metal avg `-0.0059` n `20`; unknown avg `448.1483` n `746`
- 24h: commodity avg `0.1254` n `12`; crypto_alt avg `3.1429` n `232`; crypto_major avg `3.1835` n `8`; equity avg `0.3625` n `134`; fx avg `-0.0491` n `6`; index avg `0.0838` n `26`; metal avg `0.014` n `20`; unknown avg `494.3767` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
