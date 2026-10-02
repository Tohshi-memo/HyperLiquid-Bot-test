# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T14:07:37.344548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.63` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.2806` n `13`; crypto_alt avg `-0.3406` n `235`; crypto_major avg `-0.3692` n `8`; equity avg `0.314` n `143`; fx avg `0.0169` n `6`; index avg `0.0431` n `26`; metal avg `0.0186` n `20`; unknown avg `0.5439` n `956`
- 1h: commodity avg `-0.0412` n `13`; crypto_alt avg `-0.2547` n `235`; crypto_major avg `-0.5867` n `8`; equity avg `0.2736` n `143`; fx avg `0.1054` n `6`; index avg `0.0398` n `26`; metal avg `-0.0883` n `20`; unknown avg `0.4396` n `952`
- 4h: commodity avg `0.0315` n `13`; crypto_alt avg `0.3708` n `235`; crypto_major avg `-0.2073` n `8`; equity avg `0.7634` n `142`; fx avg `0.0333` n `6`; index avg `0.2355` n `26`; metal avg `0.1005` n `20`; unknown avg `0.7344` n `944`
- 24h: commodity avg `-0.6688` n `13`; crypto_alt avg `3.1551` n `235`; crypto_major avg `2.0571` n `8`; equity avg `2.8769` n `142`; fx avg `-0.2562` n `6`; index avg `0.6352` n `26`; metal avg `0.2168` n `20`; unknown avg `109.0534` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
