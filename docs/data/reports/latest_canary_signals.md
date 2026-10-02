# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T10:07:28.914068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `13`; crypto_alt avg `-0.0191` n `234`; crypto_major avg `0.0016` n `8`; equity avg `-0.115` n `142`; fx avg `0.016` n `6`; index avg `-0.024` n `26`; metal avg `-0.0565` n `20`; unknown avg `0.17` n `983`
- 1h: commodity avg `-0.0457` n `13`; crypto_alt avg `0.0711` n `234`; crypto_major avg `0.0916` n `8`; equity avg `-0.0219` n `142`; fx avg `0.0169` n `6`; index avg `0.0007` n `26`; metal avg `-0.0316` n `20`; unknown avg `0.1697` n `983`
- 4h: commodity avg `-0.6338` n `13`; crypto_alt avg `0.4732` n `234`; crypto_major avg `0.4445` n `8`; equity avg `0.3784` n `142`; fx avg `-0.0378` n `6`; index avg `0.0876` n `26`; metal avg `-0.1446` n `20`; unknown avg `-0.3185` n `907`
- 24h: commodity avg `-0.7228` n `13`; crypto_alt avg `2.3719` n `234`; crypto_major avg `2.4657` n `8`; equity avg `1.3127` n `142`; fx avg `-0.302` n `6`; index avg `0.2558` n `26`; metal avg `0.2157` n `20`; unknown avg `0.105` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1711`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
