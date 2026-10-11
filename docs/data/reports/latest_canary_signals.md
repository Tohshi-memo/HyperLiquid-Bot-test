# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T23:37:27.385873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1655` n `13`; crypto_alt avg `0.1655` n `235`; crypto_major avg `0.0834` n `8`; equity avg `0.0667` n `150`; fx avg `0.0134` n `6`; index avg `0.03` n `26`; metal avg `0.0367` n `20`; unknown avg `-0.1743` n `1134`
- 1h: commodity avg `-0.3211` n `13`; crypto_alt avg `0.2851` n `235`; crypto_major avg `0.0975` n `8`; equity avg `0.1174` n `150`; fx avg `0.0144` n `6`; index avg `0.0459` n `26`; metal avg `0.0689` n `20`; unknown avg `1.9727` n `1124`
- 4h: commodity avg `-0.2311` n `13`; crypto_alt avg `0.2788` n `235`; crypto_major avg `0.015` n `8`; equity avg `0.1606` n `150`; fx avg `-0.0056` n `6`; index avg `0.051` n `26`; metal avg `0.0427` n `20`; unknown avg `-0.2729` n `1090`
- 24h: commodity avg `-0.1108` n `13`; crypto_alt avg `2.1495` n `235`; crypto_major avg `0.7903` n `8`; equity avg `0.4276` n `150`; fx avg `0.0038` n `6`; index avg `0.0909` n `26`; metal avg `0.1055` n `20`; unknown avg `0.671` n `957`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
