# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T14:37:31.062654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0327` n `13`; crypto_alt avg `-0.2587` n `237`; crypto_major avg `-0.1307` n `8`; equity avg `-0.227` n `151`; fx avg `0.0045` n `6`; index avg `-0.0708` n `26`; metal avg `-0.016` n `20`; unknown avg `-0.0576` n `1193`
- 1h: commodity avg `-0.0137` n `13`; crypto_alt avg `-0.7051` n `237`; crypto_major avg `-0.6765` n `8`; equity avg `-0.4176` n `151`; fx avg `-0.0136` n `6`; index avg `-0.0288` n `26`; metal avg `-0.1252` n `20`; unknown avg `0.5584` n `1139`
- 4h: commodity avg `-0.2494` n `13`; crypto_alt avg `-0.197` n `237`; crypto_major avg `-0.3272` n `8`; equity avg `0.024` n `151`; fx avg `0.0118` n `6`; index avg `0.0115` n `26`; metal avg `-0.1771` n `20`; unknown avg `0.9884` n `1103`
- 24h: commodity avg `-0.371` n `13`; crypto_alt avg `0.5985` n `237`; crypto_major avg `1.142` n `8`; equity avg `2.8695` n `151`; fx avg `-0.0211` n `6`; index avg `0.5357` n `26`; metal avg `0.0789` n `20`; unknown avg `3.2183` n `915`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2023`, n `667`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1484`, n `667`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1378`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1304`, n `667`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0762`, n `667`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.066`, n `667`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
