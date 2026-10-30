# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T04:52:26.992873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.1412` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0051` n `13`; crypto_alt avg `0.2488` n `238`; crypto_major avg `0.0662` n `8`; equity avg `0.0815` n `156`; fx avg `0.0063` n `6`; index avg `0.004` n `27`; metal avg `0.0022` n `20`; unknown avg `0.0637` n `1260`
- 1h: commodity avg `0.0109` n `13`; crypto_alt avg `0.6565` n `238`; crypto_major avg `0.1651` n `8`; equity avg `0.4233` n `156`; fx avg `-0.0081` n `6`; index avg `0.0835` n `27`; metal avg `0.0167` n `20`; unknown avg `0.4577` n `1246`
- 4h: commodity avg `0.1432` n `13`; crypto_alt avg `1.8764` n `238`; crypto_major avg `1.8427` n `8`; equity avg `0.8823` n `156`; fx avg `-0.0625` n `6`; index avg `0.0371` n `27`; metal avg `-0.2985` n `20`; unknown avg `6.4996` n `1234`
- 24h: commodity avg `-0.086` n `13`; crypto_alt avg `-3.7779` n `238`; crypto_major avg `-0.2409` n `8`; equity avg `-2.4496` n `155`; fx avg `0.117` n `6`; index avg `-0.2831` n `27`; metal avg `-0.6431` n `20`; unknown avg `28.6468` n `982`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
