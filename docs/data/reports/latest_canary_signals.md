# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T01:14:50.072289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.48` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0073` n `13`; crypto_alt avg `0.1166` n `235`; crypto_major avg `0.0401` n `8`; equity avg `0.0748` n `144`; fx avg `-0.0945` n `6`; index avg `0.0059` n `26`; metal avg `0.0306` n `20`; unknown avg `0.0761` n `1072`
- 1h: commodity avg `0.0319` n `13`; crypto_alt avg `0.3912` n `235`; crypto_major avg `0.2415` n `8`; equity avg `0.1866` n `144`; fx avg `-0.0784` n `6`; index avg `0.0274` n `26`; metal avg `0.1366` n `20`; unknown avg `0.7513` n `1068`
- 4h: commodity avg `-0.2314` n `13`; crypto_alt avg `0.8071` n `235`; crypto_major avg `0.4699` n `8`; equity avg `0.4294` n `144`; fx avg `-0.0826` n `6`; index avg `0.0352` n `26`; metal avg `0.2122` n `20`; unknown avg `1.0666` n `996`
- 24h: commodity avg `-0.26` n `13`; crypto_alt avg `1.4891` n `235`; crypto_major avg `1.6978` n `8`; equity avg `0.626` n `144`; fx avg `-0.0746` n `6`; index avg `0.0343` n `26`; metal avg `0.2241` n `20`; unknown avg `0.7576` n `950`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.196`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.181`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
