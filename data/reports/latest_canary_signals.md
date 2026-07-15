# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T00:57:17.778565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0656` n `12`; crypto_alt avg `0.0265` n `230`; crypto_major avg `0.0674` n `8`; equity avg `0.0997` n `92`; fx avg `-0.0217` n `6`; index avg `0.0401` n `25`; metal avg `0.0526` n `20`; unknown avg `-0.034` n `768`
- 1h: commodity avg `0.1588` n `12`; crypto_alt avg `-0.0297` n `230`; crypto_major avg `-0.1755` n `8`; equity avg `0.1551` n `92`; fx avg `0.0305` n `6`; index avg `0.0165` n `25`; metal avg `0.0635` n `20`; unknown avg `-0.3116` n `768`
- 4h: commodity avg `0.1138` n `12`; crypto_alt avg `0.374` n `230`; crypto_major avg `0.2959` n `8`; equity avg `0.5442` n `92`; fx avg `0.0177` n `6`; index avg `0.1239` n `25`; metal avg `0.0995` n `20`; unknown avg `-0.5933` n `766`
- 24h: commodity avg `0.0949` n `12`; crypto_alt avg `1.8888` n `230`; crypto_major avg `3.2061` n `8`; equity avg `1.7766` n `92`; fx avg `0.0226` n `6`; index avg `0.5561` n `25`; metal avg `0.6754` n `20`; unknown avg `0.1229` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
