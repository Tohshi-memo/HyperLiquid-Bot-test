# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T00:52:38.773943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0153` n `12`; crypto_alt avg `0.0344` n `233`; crypto_major avg `0.1136` n `8`; equity avg `0.2494` n `134`; fx avg `-0.0037` n `6`; index avg `0.0533` n `26`; metal avg `0.0865` n `20`; unknown avg `1.3362` n `797`
- 1h: commodity avg `-0.044` n `12`; crypto_alt avg `0.0211` n `233`; crypto_major avg `0.3611` n `8`; equity avg `0.3907` n `134`; fx avg `0.014` n `6`; index avg `0.1101` n `26`; metal avg `0.0992` n `20`; unknown avg `0.0831` n `789`
- 4h: commodity avg `0.0057` n `12`; crypto_alt avg `0.1362` n `233`; crypto_major avg `0.5623` n `8`; equity avg `0.2541` n `134`; fx avg `-0.0205` n `6`; index avg `0.0752` n `26`; metal avg `0.0861` n `20`; unknown avg `3.2514` n `741`
- 24h: commodity avg `0.1484` n `12`; crypto_alt avg `-0.723` n `232`; crypto_major avg `0.3114` n `8`; equity avg `0.2572` n `134`; fx avg `-0.0195` n `6`; index avg `-0.1503` n `26`; metal avg `-0.3402` n `20`; unknown avg `0.55` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
