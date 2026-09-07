# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T10:52:25.879648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0467` n `12`; crypto_alt avg `0.2584` n `232`; crypto_major avg `0.0991` n `8`; equity avg `0.0304` n `134`; fx avg `-0.0074` n `6`; index avg `-0.0078` n `26`; metal avg `0.029` n `20`; unknown avg `-0.209` n `796`
- 1h: commodity avg `0.0919` n `12`; crypto_alt avg `0.3374` n `232`; crypto_major avg `0.1932` n `8`; equity avg `0.044` n `134`; fx avg `0.0317` n `6`; index avg `-0.0089` n `26`; metal avg `-0.0536` n `20`; unknown avg `-0.0241` n `794`
- 4h: commodity avg `-0.0486` n `12`; crypto_alt avg `0.4415` n `232`; crypto_major avg `-0.0517` n `8`; equity avg `-0.0221` n `134`; fx avg `-0.0531` n `6`; index avg `-0.0252` n `26`; metal avg `0.0026` n `20`; unknown avg `0.7005` n `784`
- 24h: commodity avg `0.0134` n `12`; crypto_alt avg `0.1712` n `232`; crypto_major avg `-0.7336` n `8`; equity avg `0.2996` n `134`; fx avg `-0.1132` n `6`; index avg `0.0232` n `26`; metal avg `-0.1161` n `20`; unknown avg `229.2179` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
