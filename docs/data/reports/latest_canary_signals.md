# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T04:37:24.841491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `-0.1229` n `230`; crypto_major avg `-0.0352` n `8`; equity avg `-0.0434` n `96`; fx avg `-0.0041` n `6`; index avg `0.0013` n `25`; metal avg `-0.0046` n `20`; unknown avg `-0.0352` n `769`
- 1h: commodity avg `-0.0376` n `12`; crypto_alt avg `-0.2761` n `230`; crypto_major avg `-0.1067` n `8`; equity avg `-0.059` n `96`; fx avg `0.0028` n `6`; index avg `0.0237` n `25`; metal avg `-0.0022` n `20`; unknown avg `0.7337` n `769`
- 4h: commodity avg `0.0075` n `12`; crypto_alt avg `-0.4297` n `230`; crypto_major avg `-0.1218` n `8`; equity avg `0.0566` n `96`; fx avg `-0.0059` n `6`; index avg `0.0677` n `25`; metal avg `-0.0071` n `20`; unknown avg `-0.228` n `769`
- 24h: commodity avg `0.6614` n `12`; crypto_alt avg `-0.4989` n `230`; crypto_major avg `-0.0039` n `8`; equity avg `1.0091` n `96`; fx avg `0.0501` n `6`; index avg `0.1957` n `25`; metal avg `0.2343` n `20`; unknown avg `0.2171` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
