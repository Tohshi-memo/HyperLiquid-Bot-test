# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T05:07:28.565508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `13`; crypto_alt avg `-0.0647` n `237`; crypto_major avg `-0.0358` n `8`; equity avg `-0.1509` n `151`; fx avg `0.0023` n `6`; index avg `-0.0221` n `26`; metal avg `-0.0219` n `20`; unknown avg `0.0347` n `1196`
- 1h: commodity avg `0.011` n `13`; crypto_alt avg `-0.3094` n `237`; crypto_major avg `-0.0683` n `8`; equity avg `-0.3405` n `151`; fx avg `-0.0099` n `6`; index avg `-0.037` n `26`; metal avg `-0.0253` n `20`; unknown avg `-0.3079` n `1194`
- 4h: commodity avg `-0.0026` n `13`; crypto_alt avg `0.7029` n `237`; crypto_major avg `0.6329` n `8`; equity avg `-0.0526` n `151`; fx avg `0.0185` n `6`; index avg `-0.0368` n `26`; metal avg `0.1781` n `20`; unknown avg `1.9355` n `1188`
- 24h: commodity avg `0.2721` n `13`; crypto_alt avg `0.4452` n `237`; crypto_major avg `-0.259` n `8`; equity avg `-1.406` n `151`; fx avg `-0.0144` n `6`; index avg `-0.2615` n `26`; metal avg `-0.2356` n `20`; unknown avg `5.5956` n `1010`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1988`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
