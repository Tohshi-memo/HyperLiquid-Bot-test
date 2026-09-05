# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T15:37:41.415982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.0566` n `232`; crypto_major avg `0.0482` n `8`; equity avg `0.0088` n `134`; fx avg `0.001` n `6`; index avg `-0.0101` n `26`; metal avg `0.0064` n `20`; unknown avg `-0.056` n `794`
- 1h: commodity avg `0.0297` n `12`; crypto_alt avg `-0.2284` n `232`; crypto_major avg `-0.0323` n `8`; equity avg `0.0406` n `134`; fx avg `-0.0037` n `6`; index avg `0.0101` n `26`; metal avg `0.0129` n `20`; unknown avg `-0.4849` n `792`
- 4h: commodity avg `0.0628` n `12`; crypto_alt avg `0.1056` n `232`; crypto_major avg `0.7928` n `8`; equity avg `0.0332` n `134`; fx avg `0.0153` n `6`; index avg `-0.0025` n `26`; metal avg `0.0071` n `20`; unknown avg `-0.3506` n `729`
- 24h: commodity avg `0.0706` n `12`; crypto_alt avg `2.4744` n `232`; crypto_major avg `1.8707` n `8`; equity avg `0.6419` n `134`; fx avg `-0.008` n `6`; index avg `0.0652` n `26`; metal avg `-0.0157` n `20`; unknown avg `0.1202` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
