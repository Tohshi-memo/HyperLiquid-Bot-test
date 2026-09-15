# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T02:22:26.096227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `12`; crypto_alt avg `0.0763` n `233`; crypto_major avg `0.0514` n `8`; equity avg `0.0239` n `136`; fx avg `0.0379` n `6`; index avg `0.0017` n `27`; metal avg `0.0104` n `20`; unknown avg `2.5973` n `908`
- 1h: commodity avg `0.0544` n `12`; crypto_alt avg `-0.1535` n `233`; crypto_major avg `-0.0633` n `8`; equity avg `-0.0867` n `136`; fx avg `0.0776` n `6`; index avg `-0.025` n `27`; metal avg `0.02` n `20`; unknown avg `4.0118` n `906`
- 4h: commodity avg `0.0774` n `12`; crypto_alt avg `-0.3855` n `233`; crypto_major avg `-0.6424` n `8`; equity avg `0.2707` n `136`; fx avg `0.116` n `6`; index avg `0.0975` n `27`; metal avg `0.0442` n `20`; unknown avg `4.5881` n `900`
- 24h: commodity avg `-0.0147` n `12`; crypto_alt avg `-0.1935` n `233`; crypto_major avg `1.2363` n `8`; equity avg `-0.0554` n `136`; fx avg `0.1195` n `6`; index avg `-0.0357` n `27`; metal avg `-0.366` n `20`; unknown avg `7.9159` n `794`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
