# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T07:52:27.754219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1075` n `12`; crypto_alt avg `-0.0815` n `230`; crypto_major avg `-0.0198` n `8`; equity avg `-0.0069` n `92`; fx avg `0.0163` n `6`; index avg `-0.0206` n `25`; metal avg `-0.0286` n `20`; unknown avg `-0.0625` n `766`
- 1h: commodity avg `0.0148` n `12`; crypto_alt avg `-0.1676` n `230`; crypto_major avg `-0.1665` n `8`; equity avg `0.094` n `92`; fx avg `0.0097` n `6`; index avg `0.0108` n `25`; metal avg `-0.0589` n `20`; unknown avg `-0.0733` n `766`
- 4h: commodity avg `0.119` n `12`; crypto_alt avg `0.3682` n `230`; crypto_major avg `0.1535` n `8`; equity avg `1.1341` n `92`; fx avg `0.0862` n `6`; index avg `0.2353` n `25`; metal avg `0.1365` n `20`; unknown avg `0.0234` n `750`
- 24h: commodity avg `1.2333` n `12`; crypto_alt avg `-0.7668` n `230`; crypto_major avg `-0.8224` n `8`; equity avg `-0.2588` n `92`; fx avg `-0.1044` n `6`; index avg `-0.0486` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.2644` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
