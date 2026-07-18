# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T02:52:29.202581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0418` n `12`; crypto_alt avg `-0.0767` n `230`; crypto_major avg `-0.1122` n `8`; equity avg `0.0657` n `96`; fx avg `-0.0024` n `6`; index avg `0.003` n `25`; metal avg `0.0037` n `20`; unknown avg `0.1064` n `769`
- 1h: commodity avg `0.0319` n `12`; crypto_alt avg `0.0582` n `230`; crypto_major avg `0.0107` n `8`; equity avg `0.0422` n `96`; fx avg `-0.0081` n `6`; index avg `0.0044` n `25`; metal avg `-0.0174` n `20`; unknown avg `-0.0467` n `769`
- 4h: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.0222` n `230`; crypto_major avg `0.0517` n `8`; equity avg `0.1731` n `96`; fx avg `-0.0073` n `6`; index avg `0.0392` n `25`; metal avg `0.0314` n `20`; unknown avg `-0.3318` n `769`
- 24h: commodity avg `0.809` n `12`; crypto_alt avg `0.181` n `230`; crypto_major avg `0.1086` n `8`; equity avg `0.9149` n `94`; fx avg `0.0403` n `6`; index avg `0.0155` n `25`; metal avg `0.2651` n `20`; unknown avg `0.2776` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
