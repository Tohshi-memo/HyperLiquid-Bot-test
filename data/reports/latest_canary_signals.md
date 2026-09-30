# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T08:22:30.648178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0822` n `12`; crypto_alt avg `0.3695` n `234`; crypto_major avg `0.0928` n `8`; equity avg `-0.0583` n `142`; fx avg `0.0064` n `6`; index avg `-0.022` n `26`; metal avg `0.0311` n `20`; unknown avg `0.6577` n `963`
- 1h: commodity avg `0.1883` n `12`; crypto_alt avg `0.3961` n `234`; crypto_major avg `0.0218` n `8`; equity avg `0.004` n `142`; fx avg `-0.0006` n `6`; index avg `-0.0105` n `26`; metal avg `-0.0068` n `20`; unknown avg `0.9375` n `945`
- 4h: commodity avg `0.0346` n `12`; crypto_alt avg `0.0678` n `234`; crypto_major avg `-0.2417` n `8`; equity avg `0.0811` n `142`; fx avg `0.0235` n `6`; index avg `0.0307` n `26`; metal avg `0.1953` n `20`; unknown avg `1.8129` n `915`
- 24h: commodity avg `-0.6311` n `12`; crypto_alt avg `-0.4451` n `234`; crypto_major avg `-1.4716` n `8`; equity avg `0.1625` n `142`; fx avg `-0.0832` n `6`; index avg `0.0776` n `26`; metal avg `0.3519` n `20`; unknown avg `2909.7291` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
