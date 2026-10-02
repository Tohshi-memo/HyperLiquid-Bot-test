# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T11:07:28.326940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1114` n `13`; crypto_alt avg `-0.0011` n `234`; crypto_major avg `0.184` n `8`; equity avg `0.0021` n `142`; fx avg `-0.0192` n `6`; index avg `0.0187` n `26`; metal avg `0.0047` n `20`; unknown avg `-0.085` n `983`
- 1h: commodity avg `0.0147` n `13`; crypto_alt avg `-0.094` n `234`; crypto_major avg `0.188` n `8`; equity avg `-0.0528` n `142`; fx avg `-0.0261` n `6`; index avg `0.0271` n `26`; metal avg `0.0675` n `20`; unknown avg `0.4912` n `981`
- 4h: commodity avg `-0.4884` n `13`; crypto_alt avg `0.4618` n `234`; crypto_major avg `0.6264` n `8`; equity avg `0.3209` n `142`; fx avg `-0.0817` n `6`; index avg `0.1026` n `26`; metal avg `0.0418` n `20`; unknown avg `-0.6842` n `907`
- 24h: commodity avg `-0.625` n `13`; crypto_alt avg `2.0342` n `234`; crypto_major avg `2.1722` n `8`; equity avg `0.9369` n `142`; fx avg `-0.3483` n `6`; index avg `0.1964` n `26`; metal avg `0.097` n `20`; unknown avg `-0.1871` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
