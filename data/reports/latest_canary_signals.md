# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T18:52:28.838150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1744` n `12`; crypto_alt avg `-0.6836` n `233`; crypto_major avg `-0.5043` n `8`; equity avg `-0.274` n `134`; fx avg `-0.0118` n `6`; index avg `-0.0614` n `26`; metal avg `-0.1796` n `20`; unknown avg `0.7033` n `797`
- 1h: commodity avg `0.3954` n `12`; crypto_alt avg `-0.8341` n `233`; crypto_major avg `-0.4748` n `8`; equity avg `-0.3486` n `134`; fx avg `-0.0415` n `6`; index avg `-0.0583` n `26`; metal avg `-0.2143` n `20`; unknown avg `0.1204` n `795`
- 4h: commodity avg `0.2832` n `12`; crypto_alt avg `-0.704` n `232`; crypto_major avg `0.0141` n `8`; equity avg `0.1245` n `134`; fx avg `-0.0345` n `6`; index avg `-0.0164` n `26`; metal avg `-0.2103` n `20`; unknown avg `-0.6515` n `765`
- 24h: commodity avg `0.0872` n `12`; crypto_alt avg `-0.2769` n `232`; crypto_major avg `-0.1814` n `8`; equity avg `0.6249` n `134`; fx avg `-0.0851` n `6`; index avg `-0.109` n `26`; metal avg `-0.259` n `20`; unknown avg `8.4519` n `706`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
