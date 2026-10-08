# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T14:52:35.547761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1182` n `13`; crypto_alt avg `0.004` n `235`; crypto_major avg `0.0126` n `8`; equity avg `-0.2544` n `150`; fx avg `-0.009` n `6`; index avg `-0.046` n `26`; metal avg `-0.0599` n `20`; unknown avg `0.2877` n `1077`
- 1h: commodity avg `0.0431` n `13`; crypto_alt avg `0.6078` n `235`; crypto_major avg `0.398` n `8`; equity avg `0.112` n `150`; fx avg `0.0357` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0501` n `20`; unknown avg `0.4674` n `1027`
- 4h: commodity avg `-0.1099` n `13`; crypto_alt avg `-0.0432` n `235`; crypto_major avg `-0.5347` n `8`; equity avg `-0.0477` n `150`; fx avg `0.0315` n `6`; index avg `0.0688` n `26`; metal avg `-0.0762` n `20`; unknown avg `0.3072` n `1021`
- 24h: commodity avg `0.613` n `13`; crypto_alt avg `1.3251` n `235`; crypto_major avg `-1.4177` n `8`; equity avg `-1.2724` n `150`; fx avg `0.0933` n `6`; index avg `-0.0892` n `26`; metal avg `-0.0272` n `20`; unknown avg `22.3337` n `990`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
