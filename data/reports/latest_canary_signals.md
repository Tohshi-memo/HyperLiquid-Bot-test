# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T18:07:26.525167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `0.0996` n `232`; crypto_major avg `0.0839` n `8`; equity avg `0.0247` n `134`; fx avg `-0.0031` n `6`; index avg `0.0031` n `26`; metal avg `0.0074` n `20`; unknown avg `142.0043` n `791`
- 1h: commodity avg `-0.0206` n `12`; crypto_alt avg `0.1319` n `232`; crypto_major avg `0.1819` n `8`; equity avg `0.0789` n `134`; fx avg `0.0046` n `6`; index avg `0.0033` n `26`; metal avg `0.0239` n `20`; unknown avg `-0.5236` n `783`
- 4h: commodity avg `0.0046` n `12`; crypto_alt avg `-0.1957` n `232`; crypto_major avg `-0.3305` n `8`; equity avg `0.0503` n `134`; fx avg `-0.0274` n `6`; index avg `0.0053` n `26`; metal avg `0.0003` n `20`; unknown avg `145.1142` n `776`
- 24h: commodity avg `0.0754` n `12`; crypto_alt avg `1.2399` n `232`; crypto_major avg `-0.4117` n `8`; equity avg `0.2638` n `134`; fx avg `-0.0195` n `6`; index avg `0.0177` n `26`; metal avg `-0.0376` n `20`; unknown avg `2.4252` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
