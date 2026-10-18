# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T05:52:25.791501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `13`; crypto_alt avg `0.0464` n `237`; crypto_major avg `0.0098` n `8`; equity avg `0.0191` n `151`; fx avg `-0.009` n `6`; index avg `0.0067` n `26`; metal avg `0.002` n `20`; unknown avg `0.2194` n `1193`
- 1h: commodity avg `-0.0279` n `13`; crypto_alt avg `-0.6736` n `237`; crypto_major avg `-0.3311` n `8`; equity avg `-0.0789` n `151`; fx avg `0.0046` n `6`; index avg `-0.0122` n `26`; metal avg `-0.0036` n `20`; unknown avg `-0.0609` n `1191`
- 4h: commodity avg `-0.0258` n `13`; crypto_alt avg `-0.9897` n `237`; crypto_major avg `-0.2754` n `8`; equity avg `-0.0471` n `151`; fx avg `-0.013` n `6`; index avg `-0.0028` n `26`; metal avg `0.0078` n `20`; unknown avg `-0.1792` n `1185`
- 24h: commodity avg `-0.1392` n `13`; crypto_alt avg `-3.0611` n `236`; crypto_major avg `-0.8992` n `8`; equity avg `-0.9231` n `151`; fx avg `-0.042` n `6`; index avg `-0.123` n `26`; metal avg `-0.0503` n `20`; unknown avg `4.0753` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1686`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1322`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.107`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.079`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
