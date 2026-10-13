# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T09:07:29.611442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `13`; crypto_alt avg `-0.248` n `235`; crypto_major avg `-0.259` n `8`; equity avg `-0.0286` n `151`; fx avg `0.0023` n `6`; index avg `0.0111` n `26`; metal avg `0.0192` n `20`; unknown avg `-0.1356` n `1133`
- 1h: commodity avg `-0.0172` n `13`; crypto_alt avg `-0.5354` n `235`; crypto_major avg `-0.6955` n `8`; equity avg `0.2019` n `151`; fx avg `-0.0522` n `6`; index avg `0.0361` n `26`; metal avg `0.0062` n `20`; unknown avg `0.8146` n `1133`
- 4h: commodity avg `-0.0902` n `13`; crypto_alt avg `-0.4998` n `235`; crypto_major avg `-0.2711` n `8`; equity avg `0.4081` n `151`; fx avg `-0.0223` n `6`; index avg `0.1072` n `26`; metal avg `0.0031` n `20`; unknown avg `1.0592` n `1101`
- 24h: commodity avg `0.0673` n `13`; crypto_alt avg `-3.9444` n `235`; crypto_major avg `-2.2828` n `8`; equity avg `-2.7118` n `151`; fx avg `0.0321` n `6`; index avg `-0.3324` n `26`; metal avg `0.071` n `20`; unknown avg `0.0679` n `923`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1847`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1659`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1586`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1384`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0806`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0749`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0734`, n `666`, weak_sample_signal
