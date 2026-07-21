# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T16:07:28.710781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0693` n `12`; crypto_alt avg `0.0199` n `230`; crypto_major avg `-0.0563` n `8`; equity avg `0.1581` n `98`; fx avg `-0.0106` n `6`; index avg `0.0173` n `25`; metal avg `0.0113` n `20`; unknown avg `0.0481` n `771`
- 1h: commodity avg `-0.031` n `12`; crypto_alt avg `0.1198` n `230`; crypto_major avg `0.0781` n `8`; equity avg `0.2773` n `98`; fx avg `-0.0122` n `6`; index avg `0.053` n `25`; metal avg `0.0885` n `20`; unknown avg `0.039` n `771`
- 4h: commodity avg `0.1434` n `12`; crypto_alt avg `-0.0635` n `230`; crypto_major avg `-0.1094` n `8`; equity avg `1.3642` n `98`; fx avg `-0.0167` n `6`; index avg `0.1969` n `25`; metal avg `0.0598` n `20`; unknown avg `0.1633` n `771`
- 24h: commodity avg `0.6519` n `12`; crypto_alt avg `1.063` n `230`; crypto_major avg `0.9944` n `8`; equity avg `2.5213` n `98`; fx avg `0.0063` n `6`; index avg `0.3403` n `25`; metal avg `0.5676` n `20`; unknown avg `0.2576` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0875`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0566`, n `666`, weak_sample_signal
