# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T04:36:02.724120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.2251` n `232`; crypto_major avg `-0.1557` n `8`; equity avg `-0.0183` n `134`; fx avg `0.0017` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0372` n `20`; unknown avg `0.0351` n `788`
- 1h: commodity avg `0.0631` n `12`; crypto_alt avg `0.0487` n `232`; crypto_major avg `-0.0542` n `8`; equity avg `0.0939` n `134`; fx avg `0.0208` n `6`; index avg `0.0068` n `26`; metal avg `-0.0709` n `20`; unknown avg `-0.2021` n `786`
- 4h: commodity avg `0.1172` n `12`; crypto_alt avg `-1.1781` n `232`; crypto_major avg `-0.9699` n `8`; equity avg `0.1728` n `134`; fx avg `0.1219` n `6`; index avg `0.0022` n `26`; metal avg `-0.1287` n `20`; unknown avg `0.7102` n `758`
- 24h: commodity avg `0.0739` n `12`; crypto_alt avg `0.0799` n `232`; crypto_major avg `-0.7153` n `8`; equity avg `0.4531` n `134`; fx avg `0.0543` n `6`; index avg `-0.0072` n `26`; metal avg `-0.2198` n `20`; unknown avg `73.349` n `658`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1936`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
