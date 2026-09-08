# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T22:52:29.252315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `0.1598` n `233`; crypto_major avg `0.0742` n `8`; equity avg `0.0424` n `134`; fx avg `0.0018` n `6`; index avg `0.0153` n `26`; metal avg `-0.0075` n `20`; unknown avg `0.2892` n `797`
- 1h: commodity avg `-0.0326` n `12`; crypto_alt avg `0.4006` n `233`; crypto_major avg `0.3548` n `8`; equity avg `0.0129` n `134`; fx avg `0.0037` n `6`; index avg `-0.0056` n `26`; metal avg `-0.0639` n `20`; unknown avg `0.4602` n `763`
- 4h: commodity avg `-0.0275` n `12`; crypto_alt avg `0.2612` n `233`; crypto_major avg `0.3469` n `8`; equity avg `-0.1998` n `134`; fx avg `-0.028` n `6`; index avg `-0.0518` n `26`; metal avg `-0.0626` n `20`; unknown avg `0.282` n `725`
- 24h: commodity avg `0.0358` n `12`; crypto_alt avg `0.3154` n `232`; crypto_major avg `0.4377` n `8`; equity avg `0.5021` n `134`; fx avg `-0.1028` n `6`; index avg `-0.1285` n `26`; metal avg `-0.3246` n `20`; unknown avg `0.7624` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
