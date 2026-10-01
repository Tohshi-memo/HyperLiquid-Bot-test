# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T14:37:34.690829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `13`; crypto_alt avg `0.4138` n `234`; crypto_major avg `0.3069` n `8`; equity avg `0.5295` n `142`; fx avg `-0.0504` n `6`; index avg `0.0792` n `26`; metal avg `0.1575` n `20`; unknown avg `0.6264` n `933`
- 1h: commodity avg `0.049` n `13`; crypto_alt avg `-0.1515` n `234`; crypto_major avg `0.1026` n `8`; equity avg `-0.1889` n `142`; fx avg `-0.0564` n `6`; index avg `-0.1286` n `26`; metal avg `0.056` n `20`; unknown avg `2.1878` n `931`
- 4h: commodity avg `0.0458` n `13`; crypto_alt avg `-0.3219` n `234`; crypto_major avg `0.1258` n `8`; equity avg `-0.5157` n `142`; fx avg `-0.0902` n `6`; index avg `-0.1683` n `26`; metal avg `0.0235` n `20`; unknown avg `2.1359` n `925`
- 24h: commodity avg `-0.1557` n `13`; crypto_alt avg `-0.8045` n `234`; crypto_major avg `0.5941` n `8`; equity avg `0.0294` n `142`; fx avg `-0.0373` n `6`; index avg `-0.0851` n `26`; metal avg `-0.0076` n `20`; unknown avg `3.1136` n `782`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
