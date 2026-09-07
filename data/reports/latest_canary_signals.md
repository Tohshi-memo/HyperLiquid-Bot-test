# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T03:07:25.299630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `-0.4428` n `232`; crypto_major avg `-0.5234` n `8`; equity avg `-0.0824` n `134`; fx avg `-0.0028` n `6`; index avg `-0.0322` n `26`; metal avg `-0.0621` n `20`; unknown avg `0.8279` n `792`
- 1h: commodity avg `-0.0234` n `12`; crypto_alt avg `0.6683` n `232`; crypto_major avg `0.3191` n `8`; equity avg `0.0611` n `134`; fx avg `0.0334` n `6`; index avg `-0.0416` n `26`; metal avg `-0.0128` n `20`; unknown avg `1.0392` n `764`
- 4h: commodity avg `0.0175` n `12`; crypto_alt avg `-0.181` n `232`; crypto_major avg `-0.4201` n `8`; equity avg `0.2274` n `134`; fx avg `-0.0011` n `6`; index avg `-0.0061` n `26`; metal avg `-0.092` n `20`; unknown avg `134.4729` n `756`
- 24h: commodity avg `-0.0128` n `12`; crypto_alt avg `0.4935` n `232`; crypto_major avg `-0.0647` n `8`; equity avg `0.3642` n `134`; fx avg `0.0399` n `6`; index avg `-0.0109` n `26`; metal avg `-0.1357` n `20`; unknown avg `75.1821` n `650`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
