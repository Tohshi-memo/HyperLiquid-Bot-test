# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T21:52:27.196053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `13`; crypto_alt avg `-0.1447` n `236`; crypto_major avg `-0.1725` n `8`; equity avg `-0.0516` n `151`; fx avg `-0.0021` n `6`; index avg `-0.0118` n `26`; metal avg `0.0069` n `20`; unknown avg `0.1792` n `1112`
- 1h: commodity avg `0.0258` n `13`; crypto_alt avg `0.2759` n `236`; crypto_major avg `0.1651` n `8`; equity avg `-0.2231` n `151`; fx avg `-0.0167` n `6`; index avg `0.0006` n `26`; metal avg `0.0305` n `20`; unknown avg `0.1568` n `1102`
- 4h: commodity avg `-0.0487` n `13`; crypto_alt avg `0.3769` n `236`; crypto_major avg `0.2087` n `8`; equity avg `-0.4958` n `151`; fx avg `0.0068` n `6`; index avg `-0.0389` n `26`; metal avg `0.0437` n `20`; unknown avg `1.013` n `1054`
- 24h: commodity avg `-0.0526` n `13`; crypto_alt avg `-2.4942` n `236`; crypto_major avg `-2.1183` n `8`; equity avg `-4.6373` n `151`; fx avg `-0.133` n `6`; index avg `-0.605` n `26`; metal avg `-0.8546` n `20`; unknown avg `1309.5871` n `946`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0925`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0852`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0704`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0689`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0519`, n `666`, weak_sample_signal
