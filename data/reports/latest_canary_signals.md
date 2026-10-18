# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T04:07:29.622323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `13`; crypto_alt avg `-0.2809` n `237`; crypto_major avg `-0.1576` n `8`; equity avg `-0.0651` n `151`; fx avg `-0.0006` n `6`; index avg `0.0021` n `26`; metal avg `-0.0004` n `20`; unknown avg `-0.0007` n `1185`
- 1h: commodity avg `-0.0025` n `13`; crypto_alt avg `0.014` n `237`; crypto_major avg `0.0454` n `8`; equity avg `0.0999` n `151`; fx avg `-0.0077` n `6`; index avg `0.0159` n `26`; metal avg `0.0073` n `20`; unknown avg `0.1` n `1185`
- 4h: commodity avg `0.0469` n `13`; crypto_alt avg `0.0808` n `236`; crypto_major avg `0.7445` n `8`; equity avg `0.1992` n `151`; fx avg `-0.0211` n `6`; index avg `0.0396` n `26`; metal avg `0.0359` n `20`; unknown avg `0.4337` n `1185`
- 24h: commodity avg `-0.1217` n `13`; crypto_alt avg `-2.2046` n `236`; crypto_major avg `-0.3257` n `8`; equity avg `-0.8309` n `151`; fx avg `-0.0485` n `6`; index avg `-0.1012` n `26`; metal avg `-0.0689` n `20`; unknown avg `3.7317` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1665`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1371`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1088`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.08`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
