# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T03:07:39.879573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `-0.0858` n `230`; crypto_major avg `-0.0566` n `8`; equity avg `-0.1089` n `108`; fx avg `-0.0266` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0246` n `20`; unknown avg `0.0419` n `782`
- 1h: commodity avg `-0.0244` n `12`; crypto_alt avg `-0.1168` n `230`; crypto_major avg `-0.2621` n `8`; equity avg `0.3257` n `108`; fx avg `0.0385` n `6`; index avg `0.0559` n `25`; metal avg `-0.1737` n `20`; unknown avg `-0.0191` n `782`
- 4h: commodity avg `0.0933` n `12`; crypto_alt avg `-0.2705` n `230`; crypto_major avg `-0.5206` n `8`; equity avg `-0.2128` n `108`; fx avg `-0.0441` n `6`; index avg `-0.1437` n `25`; metal avg `0.1741` n `20`; unknown avg `-0.0417` n `782`
- 24h: commodity avg `0.1462` n `12`; crypto_alt avg `-0.2478` n `230`; crypto_major avg `-0.5494` n `8`; equity avg `-1.642` n `108`; fx avg `0.0202` n `6`; index avg `-0.3232` n `25`; metal avg `0.5777` n `20`; unknown avg `0.864` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
