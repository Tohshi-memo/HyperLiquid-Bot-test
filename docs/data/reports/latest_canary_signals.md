# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T14:37:26.280328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.41` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.302` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.0245` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1792` n `12`; crypto_alt avg `-0.5411` n `228`; crypto_major avg `-0.1374` n `8`; equity avg `-0.01` n `69`; fx avg `0.0352` n `6`; index avg `-0.1286` n `23`; metal avg `0.2931` n `18`; unknown avg `-0.4945` n `422`
- 1h: commodity avg `-0.0144` n `12`; crypto_alt avg `-1.86` n `228`; crypto_major avg `-1.1284` n `8`; equity avg `0.3326` n `69`; fx avg `0.0035` n `6`; index avg `0.1736` n `23`; metal avg `-0.1332` n `18`; unknown avg `-0.6321` n `422`
- 4h: commodity avg `0.0877` n `12`; crypto_alt avg `-1.1792` n `228`; crypto_major avg `-0.9138` n `8`; equity avg `0.0491` n `69`; fx avg `0.0221` n `6`; index avg `0.1107` n `23`; metal avg `-0.4023` n `18`; unknown avg `0.1069` n `422`
- 24h: commodity avg `-1.4486` n `12`; crypto_alt avg `-0.4608` n `228`; crypto_major avg `-1.5331` n `8`; equity avg `1.0321` n `69`; fx avg `0.2143` n `6`; index avg `0.5813` n `23`; metal avg `1.193` n `18`; unknown avg `-0.1939` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
