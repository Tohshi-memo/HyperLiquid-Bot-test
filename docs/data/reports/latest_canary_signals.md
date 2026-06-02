# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T09:52:24.095031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.81` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.3522` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0255` n `12`; crypto_alt avg `-0.0938` n `228`; crypto_major avg `-0.2239` n `8`; equity avg `0.0804` n `69`; fx avg `0.0084` n `6`; index avg `0.057` n `23`; metal avg `0.0655` n `18`; unknown avg `-0.2889` n `422`
- 1h: commodity avg `0.1903` n `12`; crypto_alt avg `-0.4402` n `228`; crypto_major avg `-0.5073` n `8`; equity avg `-0.0404` n `69`; fx avg `-0.0041` n `6`; index avg `-0.0206` n `23`; metal avg `-0.1013` n `18`; unknown avg `-0.1794` n `422`
- 4h: commodity avg `0.0067` n `12`; crypto_alt avg `-0.7308` n `228`; crypto_major avg `-1.1199` n `8`; equity avg `0.2869` n `69`; fx avg `0.0462` n `6`; index avg `0.2323` n `23`; metal avg `0.0837` n `18`; unknown avg `-1.0274` n `412`
- 24h: commodity avg `-1.0979` n `12`; crypto_alt avg `-0.6445` n `228`; crypto_major avg `-2.5645` n `8`; equity avg `0.727` n `69`; fx avg `0.1199` n `6`; index avg `0.1033` n `23`; metal avg `1.0079` n `18`; unknown avg `1.0494` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
