# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T07:22:27.520306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `-0.0815` n `232`; crypto_major avg `-0.1158` n `8`; equity avg `-0.0427` n `134`; fx avg `-0.0046` n `6`; index avg `-0.0249` n `26`; metal avg `-0.0054` n `20`; unknown avg `-0.1269` n `796`
- 1h: commodity avg `-0.0767` n `12`; crypto_alt avg `-0.1964` n `232`; crypto_major avg `-0.2132` n `8`; equity avg `-0.0161` n `134`; fx avg `0.0338` n `6`; index avg `0.0168` n `26`; metal avg `0.0261` n `20`; unknown avg `0.171` n `784`
- 4h: commodity avg `0.0638` n `12`; crypto_alt avg `-0.1223` n `232`; crypto_major avg `-0.1954` n `8`; equity avg `0.1467` n `134`; fx avg `-0.0519` n `6`; index avg `0.0696` n `26`; metal avg `-0.0233` n `20`; unknown avg `-0.0585` n `758`
- 24h: commodity avg `0.0307` n `12`; crypto_alt avg `0.5364` n `232`; crypto_major avg `-0.4894` n `8`; equity avg `0.4543` n `134`; fx avg `-0.0115` n `6`; index avg `0.0437` n `26`; metal avg `-0.1543` n `20`; unknown avg `382.6585` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
