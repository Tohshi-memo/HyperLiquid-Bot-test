# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T15:37:27.868874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `0.3154` n `232`; crypto_major avg `0.2479` n `8`; equity avg `0.1235` n `133`; fx avg `0.0088` n `6`; index avg `0.0164` n `26`; metal avg `-0.0079` n `20`; unknown avg `0.1438` n `792`
- 1h: commodity avg `0.1753` n `12`; crypto_alt avg `-0.0768` n `232`; crypto_major avg `-0.0363` n `8`; equity avg `-0.2165` n `133`; fx avg `-0.0126` n `6`; index avg `-0.0081` n `26`; metal avg `-0.0621` n `20`; unknown avg `0.2359` n `789`
- 4h: commodity avg `0.3693` n `12`; crypto_alt avg `0.2449` n `232`; crypto_major avg `0.6452` n `8`; equity avg `0.7053` n `133`; fx avg `-0.1074` n `6`; index avg `0.1628` n `26`; metal avg `0.311` n `20`; unknown avg `0.2875` n `789`
- 24h: commodity avg `0.7311` n `12`; crypto_alt avg `-1.3533` n `232`; crypto_major avg `-1.5427` n `8`; equity avg `-0.5784` n `132`; fx avg `-0.3478` n `6`; index avg `-0.0755` n `26`; metal avg `0.0558` n `20`; unknown avg `-0.0546` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
