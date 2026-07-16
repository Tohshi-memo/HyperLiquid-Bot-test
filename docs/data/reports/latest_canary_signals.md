# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T06:07:26.155963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0267` n `12`; crypto_alt avg `-0.0817` n `230`; crypto_major avg `-0.0304` n `8`; equity avg `-0.1892` n `94`; fx avg `0.0034` n `6`; index avg `-0.0356` n `25`; metal avg `0.062` n `20`; unknown avg `0.0189` n `752`
- 1h: commodity avg `0.0199` n `12`; crypto_alt avg `-0.0823` n `230`; crypto_major avg `0.3175` n `8`; equity avg `-0.2026` n `94`; fx avg `0.0163` n `6`; index avg `-0.0484` n `25`; metal avg `0.0483` n `20`; unknown avg `0.0153` n `752`
- 4h: commodity avg `-0.0886` n `12`; crypto_alt avg `-0.0994` n `230`; crypto_major avg `0.2782` n `8`; equity avg `-0.0222` n `94`; fx avg `-0.0326` n `6`; index avg `0.0226` n `25`; metal avg `0.122` n `20`; unknown avg `-0.1954` n `752`
- 24h: commodity avg `-0.0743` n `12`; crypto_alt avg `-0.0654` n `230`; crypto_major avg `0.0419` n `8`; equity avg `-2.6145` n `93`; fx avg `0.1339` n `6`; index avg `-0.5391` n `25`; metal avg `0.0747` n `20`; unknown avg `-0.2204` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
