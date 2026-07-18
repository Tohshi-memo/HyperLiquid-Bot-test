# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T00:22:23.174292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0351` n `12`; crypto_alt avg `0.0554` n `230`; crypto_major avg `0.1799` n `8`; equity avg `0.0477` n `96`; fx avg `0.0036` n `6`; index avg `0.0517` n `25`; metal avg `-0.0102` n `20`; unknown avg `-0.0593` n `769`
- 1h: commodity avg `-0.0377` n `12`; crypto_alt avg `0.1279` n `230`; crypto_major avg `0.1912` n `8`; equity avg `0.0637` n `96`; fx avg `-0.0031` n `6`; index avg `0.0249` n `25`; metal avg `0.0444` n `20`; unknown avg `-0.1425` n `769`
- 4h: commodity avg `0.0598` n `12`; crypto_alt avg `0.0976` n `230`; crypto_major avg `0.0913` n `8`; equity avg `0.0585` n `96`; fx avg `-0.0323` n `6`; index avg `0.0084` n `25`; metal avg `0.0782` n `20`; unknown avg `-0.1545` n `769`
- 24h: commodity avg `0.703` n `12`; crypto_alt avg `-0.3325` n `230`; crypto_major avg `-0.3872` n `8`; equity avg `-0.457` n `94`; fx avg `0.0273` n `6`; index avg `-0.1471` n `25`; metal avg `0.0662` n `20`; unknown avg `0.1459` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
