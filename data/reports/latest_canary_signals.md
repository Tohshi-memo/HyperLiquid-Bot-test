# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T19:22:30.475752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1799` n `12`; crypto_alt avg `-0.3441` n `230`; crypto_major avg `-0.4102` n `8`; equity avg `-0.8496` n `112`; fx avg `-0.0018` n `6`; index avg `-0.0853` n `25`; metal avg `-0.0595` n `20`; unknown avg `-0.2037` n `781`
- 1h: commodity avg `0.1799` n `12`; crypto_alt avg `-0.3441` n `230`; crypto_major avg `-0.4102` n `8`; equity avg `-0.8496` n `112`; fx avg `-0.0018` n `6`; index avg `-0.0853` n `25`; metal avg `-0.0595` n `20`; unknown avg `-0.2037` n `781`
- 4h: commodity avg `0.1799` n `12`; crypto_alt avg `-0.3441` n `230`; crypto_major avg `-0.4102` n `8`; equity avg `-0.8496` n `112`; fx avg `-0.0018` n `6`; index avg `-0.0853` n `25`; metal avg `-0.0595` n `20`; unknown avg `-0.2037` n `781`
- 24h: commodity avg `0.5052` n `12`; crypto_alt avg `0.0051` n `230`; crypto_major avg `-1.5689` n `8`; equity avg `-0.7206` n `109`; fx avg `0.039` n `6`; index avg `-0.2778` n `25`; metal avg `-0.105` n `20`; unknown avg `113.1959` n `749`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.117`, n `671`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `671`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1059`, n `671`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0958`, n `671`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0928`, n `671`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.086`, n `671`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0776`, n `671`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `671`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `671`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0656`, n `671`, weak_sample_signal
