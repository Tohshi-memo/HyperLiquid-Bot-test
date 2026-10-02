# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T06:52:26.321193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0107` n `13`; crypto_alt avg `-0.002` n `234`; crypto_major avg `-0.0167` n `8`; equity avg `-0.0724` n `142`; fx avg `0.0312` n `6`; index avg `-0.0185` n `26`; metal avg `-0.0487` n `20`; unknown avg `0.0077` n `985`
- 1h: commodity avg `-0.1281` n `13`; crypto_alt avg `0.1035` n `234`; crypto_major avg `0.1316` n `8`; equity avg `-0.0347` n `142`; fx avg `-0.0116` n `6`; index avg `0.0064` n `26`; metal avg `-0.0532` n `20`; unknown avg `6.6138` n `953`
- 4h: commodity avg `-0.1363` n `13`; crypto_alt avg `0.8594` n `234`; crypto_major avg `1.0731` n `8`; equity avg `0.0368` n `142`; fx avg `-0.0665` n `6`; index avg `0.012` n `26`; metal avg `0.1141` n `20`; unknown avg `7.4515` n `947`
- 24h: commodity avg `0.0265` n `13`; crypto_alt avg `-0.0157` n `234`; crypto_major avg `0.891` n `8`; equity avg `0.0009` n `142`; fx avg `-0.2692` n `6`; index avg `-0.0235` n `26`; metal avg `-0.103` n `20`; unknown avg `1142.4747` n `841`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
