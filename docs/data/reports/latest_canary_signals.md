# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T04:52:32.722623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `12`; crypto_alt avg `0.0703` n `232`; crypto_major avg `0.0131` n `8`; equity avg `0.0227` n `134`; fx avg `-0.0035` n `6`; index avg `-0.0054` n `26`; metal avg `0.0059` n `20`; unknown avg `-0.135` n `781`
- 1h: commodity avg `0.0571` n `12`; crypto_alt avg `-0.0605` n `232`; crypto_major avg `0.0024` n `8`; equity avg `-0.0321` n `134`; fx avg `0.0635` n `6`; index avg `-0.0254` n `26`; metal avg `0.0148` n `20`; unknown avg `0.9932` n `773`
- 4h: commodity avg `0.1112` n `12`; crypto_alt avg `-0.3256` n `232`; crypto_major avg `-0.4913` n `8`; equity avg `0.1891` n `134`; fx avg `-0.0216` n `6`; index avg `0.0428` n `26`; metal avg `0.1149` n `20`; unknown avg `0.4811` n `767`
- 24h: commodity avg `0.143` n `12`; crypto_alt avg `0.859` n `232`; crypto_major avg `-0.7874` n `8`; equity avg `0.6547` n `134`; fx avg `-0.2767` n `6`; index avg `0.1773` n `26`; metal avg `0.4465` n `20`; unknown avg `7464.1673` n `670`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
