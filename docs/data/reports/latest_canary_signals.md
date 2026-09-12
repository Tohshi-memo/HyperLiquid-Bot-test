# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T19:28:42.590845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `12`; crypto_alt avg `-0.0902` n `233`; crypto_major avg `-0.0839` n `8`; equity avg `-0.0079` n `136`; fx avg `-0.0093` n `6`; index avg `-0.0039` n `26`; metal avg `-0.005` n `20`; unknown avg `1.0343` n `838`
- 1h: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.1556` n `233`; crypto_major avg `-0.1466` n `8`; equity avg `-0.0174` n `136`; fx avg `0.0001` n `6`; index avg `-0.0054` n `26`; metal avg `-0.0068` n `20`; unknown avg `2.5757` n `796`
- 4h: commodity avg `0.0808` n `12`; crypto_alt avg `-0.3157` n `233`; crypto_major avg `-0.527` n `8`; equity avg `-0.0311` n `136`; fx avg `-0.0084` n `6`; index avg `-0.0073` n `26`; metal avg `0.0069` n `20`; unknown avg `0.1339` n `782`
- 24h: commodity avg `-0.2216` n `12`; crypto_alt avg `1.3175` n `233`; crypto_major avg `0.0892` n `8`; equity avg `-0.0219` n `136`; fx avg `-0.0387` n `6`; index avg `0.0275` n `26`; metal avg `0.0045` n `20`; unknown avg `0.9807` n `710`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
