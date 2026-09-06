# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T23:37:28.050438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `0.1173` n `232`; crypto_major avg `0.1345` n `8`; equity avg `-0.0336` n `134`; fx avg `0.0209` n `6`; index avg `0.004` n `26`; metal avg `-0.0022` n `20`; unknown avg `141.7451` n `794`
- 1h: commodity avg `-0.0111` n `12`; crypto_alt avg `0.4497` n `232`; crypto_major avg `0.4537` n `8`; equity avg `-0.028` n `134`; fx avg `0.0137` n `6`; index avg `-0.0336` n `26`; metal avg `-0.0057` n `20`; unknown avg `-0.0035` n `791`
- 4h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.9121` n `232`; crypto_major avg `0.8454` n `8`; equity avg `-0.0767` n `134`; fx avg `0.0404` n `6`; index avg `-0.0204` n `26`; metal avg `-0.0692` n `20`; unknown avg `-0.0521` n `771`
- 24h: commodity avg `-0.0019` n `12`; crypto_alt avg `1.6557` n `232`; crypto_major avg `1.1632` n `8`; equity avg `0.2074` n `134`; fx avg `0.0486` n `6`; index avg `-0.0148` n `26`; metal avg `-0.0869` n `20`; unknown avg `151.7764` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
