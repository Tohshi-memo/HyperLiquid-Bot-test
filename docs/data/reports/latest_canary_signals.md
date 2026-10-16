# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T03:07:31.086719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `13`; crypto_alt avg `0.0272` n `236`; crypto_major avg `0.1077` n `8`; equity avg `0.0711` n `151`; fx avg `0.0148` n `6`; index avg `0.0122` n `26`; metal avg `0.0513` n `20`; unknown avg `0.8319` n `1134`
- 1h: commodity avg `-0.076` n `13`; crypto_alt avg `0.0583` n `236`; crypto_major avg `0.1758` n `8`; equity avg `0.2523` n `151`; fx avg `0.0045` n `6`; index avg `0.058` n `26`; metal avg `0.2211` n `20`; unknown avg `0.2271` n `1134`
- 4h: commodity avg `-0.084` n `13`; crypto_alt avg `-0.1438` n `236`; crypto_major avg `-0.0847` n `8`; equity avg `0.1821` n `151`; fx avg `0.0571` n `6`; index avg `0.0166` n `26`; metal avg `0.1848` n `20`; unknown avg `0.2252` n `1128`
- 24h: commodity avg `-0.0663` n `13`; crypto_alt avg `3.0349` n `236`; crypto_major avg `1.8151` n `8`; equity avg `2.055` n `151`; fx avg `-0.0318` n `6`; index avg `0.3838` n `26`; metal avg `0.4226` n `20`; unknown avg `25.8686` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.0939`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0894`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0868`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.076`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0715`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.068`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0644`, n `666`, weak_sample_signal
