# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T07:22:24.782874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `-0.3635` n `232`; crypto_major avg `-0.1667` n `8`; equity avg `-0.0394` n `134`; fx avg `-0.0053` n `6`; index avg `-0.0046` n `26`; metal avg `-0.0099` n `20`; unknown avg `-0.0202` n `792`
- 1h: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.3319` n `232`; crypto_major avg `-0.2775` n `8`; equity avg `-0.0331` n `134`; fx avg `-0.0117` n `6`; index avg `-0.0088` n `26`; metal avg `-0.0099` n `20`; unknown avg `-0.08` n `788`
- 4h: commodity avg `0.0163` n `12`; crypto_alt avg `-0.4276` n `232`; crypto_major avg `0.0283` n `8`; equity avg `0.0506` n `134`; fx avg `0.004` n `6`; index avg `0.0036` n `26`; metal avg `0.0037` n `20`; unknown avg `457.9736` n `728`
- 24h: commodity avg `0.1411` n `12`; crypto_alt avg `1.5166` n `232`; crypto_major avg `2.2354` n `8`; equity avg `0.4287` n `134`; fx avg `-0.0408` n `6`; index avg `0.0784` n `26`; metal avg `-0.0002` n `20`; unknown avg `493.5349` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
