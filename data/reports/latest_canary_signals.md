# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T23:07:28.823563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.0289` n `232`; crypto_major avg `0.0254` n `8`; equity avg `-0.0185` n `132`; fx avg `0.0001` n `6`; index avg `0.0026` n `26`; metal avg `0.0028` n `20`; unknown avg `-0.0027` n `790`
- 1h: commodity avg `0.0118` n `12`; crypto_alt avg `-0.0609` n `232`; crypto_major avg `-0.0038` n `8`; equity avg `-0.0518` n `132`; fx avg `0.0042` n `6`; index avg `-0.0017` n `26`; metal avg `0.0031` n `20`; unknown avg `0.2074` n `790`
- 4h: commodity avg `0.11` n `12`; crypto_alt avg `0.0119` n `232`; crypto_major avg `0.0312` n `8`; equity avg `-0.1155` n `132`; fx avg `0.0272` n `6`; index avg `0.009` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.469` n `772`
- 24h: commodity avg `0.8621` n `12`; crypto_alt avg `-0.4946` n `232`; crypto_major avg `-1.737` n `8`; equity avg `-2.0972` n `130`; fx avg `0.0525` n `6`; index avg `-0.3303` n `26`; metal avg `-0.8769` n `20`; unknown avg `-0.1164` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.044`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0423`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0391`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0334`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0308`, n `668`, weak_sample_signal
