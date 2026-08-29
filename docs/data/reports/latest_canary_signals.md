# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T06:07:26.513878+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.61` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0053` n `12`; crypto_alt avg `-0.3533` n `231`; crypto_major avg `-0.2693` n `8`; equity avg `-0.0031` n `127`; fx avg `-0.0016` n `6`; index avg `0.0004` n `26`; metal avg `-0.0061` n `20`; unknown avg `-0.0881` n `761`
- 1h: commodity avg `-0.0183` n `12`; crypto_alt avg `-0.2909` n `231`; crypto_major avg `-0.3058` n `8`; equity avg `-0.0035` n `127`; fx avg `-0.0041` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0135` n `20`; unknown avg `-0.0342` n `761`
- 4h: commodity avg `-0.025` n `12`; crypto_alt avg `-0.181` n `231`; crypto_major avg `-0.1233` n `8`; equity avg `0.0954` n `127`; fx avg `0.0083` n `6`; index avg `0.0359` n `26`; metal avg `0.0059` n `20`; unknown avg `-0.1269` n `761`
- 24h: commodity avg `-0.1402` n `12`; crypto_alt avg `-1.9269` n `231`; crypto_major avg `-2.6171` n `8`; equity avg `-1.4618` n `127`; fx avg `-0.0317` n `6`; index avg `-0.1166` n `26`; metal avg `-0.2412` n `20`; unknown avg `-0.4276` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
