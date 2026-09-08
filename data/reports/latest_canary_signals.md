# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T23:22:29.047157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.0923` n `233`; crypto_major avg `-0.0399` n `8`; equity avg `-0.044` n `134`; fx avg `-0.0164` n `6`; index avg `-0.0053` n `26`; metal avg `0.0042` n `20`; unknown avg `3.1808` n `797`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `-0.0349` n `233`; crypto_major avg `0.0141` n `8`; equity avg `0.0428` n `134`; fx avg `-0.0174` n `6`; index avg `0.0144` n `26`; metal avg `0.0055` n `20`; unknown avg `2.3528` n `795`
- 4h: commodity avg `0.0975` n `12`; crypto_alt avg `-0.2215` n `233`; crypto_major avg `0.0474` n `8`; equity avg `-0.2224` n `134`; fx avg `-0.0444` n `6`; index avg `-0.0481` n `26`; metal avg `-0.1106` n `20`; unknown avg `1.0099` n `725`
- 24h: commodity avg `0.0595` n `12`; crypto_alt avg `-0.1036` n `232`; crypto_major avg `0.2007` n `8`; equity avg `0.558` n `134`; fx avg `-0.1047` n `6`; index avg `-0.1009` n `26`; metal avg `-0.3512` n `20`; unknown avg `1.8674` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
