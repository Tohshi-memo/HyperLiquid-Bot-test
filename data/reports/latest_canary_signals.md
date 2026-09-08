# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T15:37:29.875362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.067` n `12`; crypto_alt avg `0.1042` n `232`; crypto_major avg `0.1202` n `8`; equity avg `0.0742` n `134`; fx avg `-0.0251` n `6`; index avg `-0.0087` n `26`; metal avg `-0.009` n `20`; unknown avg `0.3784` n `797`
- 1h: commodity avg `-0.0761` n `12`; crypto_alt avg `0.6843` n `232`; crypto_major avg `0.427` n `8`; equity avg `0.6314` n `134`; fx avg `0.0039` n `6`; index avg `0.0654` n `26`; metal avg `0.0055` n `20`; unknown avg `1.087` n `795`
- 4h: commodity avg `-0.5224` n `12`; crypto_alt avg `0.5158` n `232`; crypto_major avg `0.4453` n `8`; equity avg `1.0474` n `134`; fx avg `0.0102` n `6`; index avg `0.0552` n `26`; metal avg `-0.0749` n `20`; unknown avg `0.5804` n `775`
- 24h: commodity avg `-0.3015` n `12`; crypto_alt avg `1.4554` n `232`; crypto_major avg `0.5468` n `8`; equity avg `1.1057` n `134`; fx avg `-0.0806` n `6`; index avg `-0.0106` n `26`; metal avg `-0.0045` n `20`; unknown avg `7062.5812` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
