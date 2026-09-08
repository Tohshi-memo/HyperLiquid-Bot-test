# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T01:07:28.393415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `0.046` n `232`; crypto_major avg `0.0048` n `8`; equity avg `-0.0441` n `134`; fx avg `-0.0067` n `6`; index avg `-0.0191` n `26`; metal avg `0.0092` n `20`; unknown avg `1.0366` n `795`
- 1h: commodity avg `-0.0672` n `12`; crypto_alt avg `0.3744` n `232`; crypto_major avg `0.1063` n `8`; equity avg `0.3139` n `134`; fx avg `-0.0104` n `6`; index avg `0.064` n `26`; metal avg `0.0162` n `20`; unknown avg `6.2743` n `789`
- 4h: commodity avg `-0.0256` n `12`; crypto_alt avg `0.3183` n `232`; crypto_major avg `0.1572` n `8`; equity avg `0.2302` n `134`; fx avg `-0.1106` n `6`; index avg `0.0318` n `26`; metal avg `0.1043` n `20`; unknown avg `2.8675` n `788`
- 24h: commodity avg `0.1693` n `12`; crypto_alt avg `0.5377` n `232`; crypto_major avg `-0.9652` n `8`; equity avg `0.6338` n `134`; fx avg `-0.1257` n `6`; index avg `0.1344` n `26`; metal avg `0.2571` n `20`; unknown avg `7766.9317` n `644`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
