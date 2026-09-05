# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T12:52:28.511576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `0.1116` n `232`; crypto_major avg `0.2665` n `8`; equity avg `-0.0028` n `134`; fx avg `0.003` n `6`; index avg `0.0089` n `26`; metal avg `0.0039` n `20`; unknown avg `-0.1564` n `792`
- 1h: commodity avg `0.0001` n `12`; crypto_alt avg `0.3768` n `232`; crypto_major avg `0.6247` n `8`; equity avg `0.0082` n `134`; fx avg `0.0047` n `6`; index avg `0.0094` n `26`; metal avg `-0.0079` n `20`; unknown avg `-0.047` n `783`
- 4h: commodity avg `0.0353` n `12`; crypto_alt avg `0.5651` n `232`; crypto_major avg `0.6752` n `8`; equity avg `0.0993` n `134`; fx avg `0.0056` n `6`; index avg `0.0408` n `26`; metal avg `-0.0037` n `20`; unknown avg `-0.1542` n `780`
- 24h: commodity avg `0.1758` n `12`; crypto_alt avg `2.8984` n `232`; crypto_major avg `1.3276` n `8`; equity avg `1.7893` n `134`; fx avg `0.0833` n `6`; index avg `0.2064` n `26`; metal avg `0.1905` n `20`; unknown avg `17.2662` n `650`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
