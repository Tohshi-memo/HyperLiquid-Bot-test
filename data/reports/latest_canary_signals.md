# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T21:52:26.132188+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `13`; crypto_alt avg `0.1005` n `235`; crypto_major avg `0.0636` n `8`; equity avg `0.0051` n `150`; fx avg `-0.0009` n `6`; index avg `0.0047` n `26`; metal avg `0.0309` n `20`; unknown avg `0.4526` n `1124`
- 1h: commodity avg `-0.0172` n `13`; crypto_alt avg `-0.4073` n `235`; crypto_major avg `-0.3488` n `8`; equity avg `-0.0539` n `150`; fx avg `-0.0206` n `6`; index avg `-0.0083` n `26`; metal avg `0.0108` n `20`; unknown avg `0.2762` n `1112`
- 4h: commodity avg `0.1054` n `13`; crypto_alt avg `-0.5978` n `235`; crypto_major avg `-0.8004` n `8`; equity avg `-0.0784` n `150`; fx avg `-0.0149` n `6`; index avg `-0.0118` n `26`; metal avg `0.0106` n `20`; unknown avg `0.4406` n `1088`
- 24h: commodity avg `0.2022` n `13`; crypto_alt avg `1.2824` n `235`; crypto_major avg `0.3313` n `8`; equity avg `0.2156` n `150`; fx avg `0.0069` n `6`; index avg `0.0286` n `26`; metal avg `0.0917` n `20`; unknown avg `0.5962` n `965`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
