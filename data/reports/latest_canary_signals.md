# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T01:52:30.089078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1196` n `13`; crypto_alt avg `-0.1741` n `234`; crypto_major avg `-0.03` n `8`; equity avg `-0.0208` n `142`; fx avg `-0.0039` n `6`; index avg `-0.0058` n `26`; metal avg `0.0121` n `20`; unknown avg `0.0013` n `974`
- 1h: commodity avg `-0.32` n `13`; crypto_alt avg `-0.2039` n `234`; crypto_major avg `-0.0113` n `8`; equity avg `0.1409` n `142`; fx avg `0.0132` n `6`; index avg `0.0411` n `26`; metal avg `0.1803` n `20`; unknown avg `0.0041` n `972`
- 4h: commodity avg `-0.2958` n `13`; crypto_alt avg `0.4712` n `234`; crypto_major avg `-0.0397` n `8`; equity avg `0.3325` n `142`; fx avg `0.1218` n `6`; index avg `0.125` n `26`; metal avg `0.0326` n `20`; unknown avg `0.6529` n `942`
- 24h: commodity avg `-0.1491` n `13`; crypto_alt avg `-0.0332` n `234`; crypto_major avg `0.5368` n `8`; equity avg `-0.0907` n `142`; fx avg `0.2148` n `6`; index avg `0.0593` n `26`; metal avg `-0.0757` n `20`; unknown avg `778.9627` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
