# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T09:37:28.476371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `0.0113` n `232`; crypto_major avg `-0.0583` n `8`; equity avg `0.0178` n `134`; fx avg `-0.0112` n `6`; index avg `0.0068` n `26`; metal avg `-0.0018` n `20`; unknown avg `1.0415` n `792`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `0.2741` n `232`; crypto_major avg `0.1687` n `8`; equity avg `0.0424` n `134`; fx avg `-0.0149` n `6`; index avg `0.009` n `26`; metal avg `0.0028` n `20`; unknown avg `0.0775` n `788`
- 4h: commodity avg `-0.0188` n `12`; crypto_alt avg `0.9166` n `232`; crypto_major avg `0.9652` n `8`; equity avg `0.0393` n `134`; fx avg `-0.01` n `6`; index avg `0.0121` n `26`; metal avg `-0.0348` n `20`; unknown avg `6.7538` n `744`
- 24h: commodity avg `0.1706` n `12`; crypto_alt avg `0.4471` n `232`; crypto_major avg `-1.3698` n `8`; equity avg `0.9709` n `134`; fx avg `-0.137` n `6`; index avg `0.0808` n `26`; metal avg `-0.1003` n `20`; unknown avg `16.6374` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
