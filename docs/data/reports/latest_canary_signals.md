# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T14:07:30.975907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `13`; crypto_alt avg `-0.4398` n `234`; crypto_major avg `-0.2365` n `8`; equity avg `-0.3865` n `142`; fx avg `-0.0007` n `6`; index avg `-0.1215` n `26`; metal avg `-0.0813` n `20`; unknown avg `0.3525` n `973`
- 1h: commodity avg `0.1124` n `13`; crypto_alt avg `-0.0978` n `234`; crypto_major avg `0.1623` n `8`; equity avg `-0.6925` n `142`; fx avg `0.0071` n `6`; index avg `-0.1906` n `26`; metal avg `-0.1341` n `20`; unknown avg `16.4867` n `973`
- 4h: commodity avg `-0.0259` n `13`; crypto_alt avg `-0.3777` n `234`; crypto_major avg `0.1894` n `8`; equity avg `-0.721` n `142`; fx avg `-0.0126` n `6`; index avg `-0.1376` n `26`; metal avg `0.0993` n `20`; unknown avg `1.7232` n `967`
- 24h: commodity avg `-0.0804` n `13`; crypto_alt avg `-2.1856` n `234`; crypto_major avg `-0.5863` n `8`; equity avg `-0.7796` n `142`; fx avg `0.0548` n `6`; index avg `-0.1964` n `26`; metal avg `-0.2669` n `20`; unknown avg `3.2444` n `786`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
