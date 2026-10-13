# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T13:07:41.016970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1879` n `13`; crypto_alt avg `-0.2618` n `235`; crypto_major avg `-0.1556` n `8`; equity avg `-0.081` n `151`; fx avg `-0.0022` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0523` n `20`; unknown avg `0.2393` n `1133`
- 1h: commodity avg `0.2067` n `13`; crypto_alt avg `0.4086` n `235`; crypto_major avg `0.0567` n `8`; equity avg `-0.295` n `151`; fx avg `0.0133` n `6`; index avg `-0.0346` n `26`; metal avg `-0.1513` n `20`; unknown avg `12.7702` n `1133`
- 4h: commodity avg `0.3169` n `13`; crypto_alt avg `-1.1742` n `235`; crypto_major avg `-0.6172` n `8`; equity avg `-1.0039` n `151`; fx avg `0.0547` n `6`; index avg `-0.1051` n `26`; metal avg `-0.2182` n `20`; unknown avg `0.1234` n `1127`
- 24h: commodity avg `0.0973` n `13`; crypto_alt avg `-3.8727` n `235`; crypto_major avg `-1.867` n `8`; equity avg `-3.4986` n `151`; fx avg `0.0765` n `6`; index avg `-0.4067` n `26`; metal avg `-0.1721` n `20`; unknown avg `0.3947` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1702`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1689`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1501`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1459`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.09`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
