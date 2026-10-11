# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T12:07:26.866172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `13`; crypto_alt avg `0.2094` n `235`; crypto_major avg `0.0523` n `8`; equity avg `0.0433` n `150`; fx avg `0.0114` n `6`; index avg `0.0108` n `26`; metal avg `0.0051` n `20`; unknown avg `0.1943` n `1109`
- 1h: commodity avg `-0.0477` n `13`; crypto_alt avg `0.4085` n `235`; crypto_major avg `0.2444` n `8`; equity avg `0.0911` n `150`; fx avg `0.0187` n `6`; index avg `0.0072` n `26`; metal avg `0.0049` n `20`; unknown avg `0.1995` n `1109`
- 4h: commodity avg `-0.0345` n `13`; crypto_alt avg `0.1562` n `235`; crypto_major avg `0.2825` n `8`; equity avg `0.1321` n `150`; fx avg `0.0311` n `6`; index avg `0.009` n `26`; metal avg `-0.0029` n `20`; unknown avg `0.1386` n `1109`
- 24h: commodity avg `0.4066` n `13`; crypto_alt avg `1.1946` n `235`; crypto_major avg `0.1865` n `8`; equity avg `0.1641` n `150`; fx avg `0.0302` n `6`; index avg `0.0053` n `26`; metal avg `0.005` n `20`; unknown avg `0.7905` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
