# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T11:07:29.650642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0458` n `12`; crypto_alt avg `-0.016` n `230`; crypto_major avg `0.081` n `8`; equity avg `0.0113` n `93`; fx avg `0.0125` n `6`; index avg `0.0132` n `25`; metal avg `-0.0174` n `20`; unknown avg `-0.0165` n `767`
- 1h: commodity avg `-0.0941` n `12`; crypto_alt avg `-0.1169` n `230`; crypto_major avg `-0.0789` n `8`; equity avg `-0.0693` n `93`; fx avg `-0.0104` n `6`; index avg `-0.0034` n `25`; metal avg `-0.0971` n `20`; unknown avg `-0.0745` n `767`
- 4h: commodity avg `-0.0652` n `12`; crypto_alt avg `-0.0378` n `230`; crypto_major avg `0.0521` n `8`; equity avg `-0.3162` n `93`; fx avg `-0.0045` n `6`; index avg `-0.07` n `25`; metal avg `-0.1813` n `20`; unknown avg `-0.1262` n `765`
- 24h: commodity avg `-0.1784` n `12`; crypto_alt avg `1.6597` n `230`; crypto_major avg `3.0518` n `8`; equity avg `1.441` n `92`; fx avg `0.0164` n `6`; index avg `0.4059` n `25`; metal avg `0.2413` n `20`; unknown avg `0.24` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
