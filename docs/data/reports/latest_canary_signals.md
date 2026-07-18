# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T01:22:29.969825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `0.0733` n `230`; crypto_major avg `0.0463` n `8`; equity avg `0.0539` n `96`; fx avg `0.0035` n `6`; index avg `-0.0027` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.081` n `769`
- 1h: commodity avg `-0.0354` n `12`; crypto_alt avg `-0.0983` n `230`; crypto_major avg `-0.1641` n `8`; equity avg `0.1137` n `96`; fx avg `0.0237` n `6`; index avg `-0.0048` n `25`; metal avg `0.0104` n `20`; unknown avg `0.0057` n `769`
- 4h: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.034` n `230`; crypto_major avg `-0.2666` n `8`; equity avg `0.1501` n `96`; fx avg `0.0258` n `6`; index avg `0.0045` n `25`; metal avg `0.0862` n `20`; unknown avg `-0.0476` n `769`
- 24h: commodity avg `0.532` n `12`; crypto_alt avg `-0.5474` n `230`; crypto_major avg `-0.6852` n `8`; equity avg `-0.2773` n `94`; fx avg `0.0793` n `6`; index avg `-0.1534` n `25`; metal avg `0.0418` n `20`; unknown avg `0.1461` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
