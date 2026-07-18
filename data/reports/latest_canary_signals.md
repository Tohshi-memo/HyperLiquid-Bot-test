# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T03:22:29.485473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `12`; crypto_alt avg `-0.029` n `230`; crypto_major avg `0.0069` n `8`; equity avg `0.0144` n `96`; fx avg `0.0035` n `6`; index avg `0.0033` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.0661` n `769`
- 1h: commodity avg `-0.0165` n `12`; crypto_alt avg `-0.0428` n `230`; crypto_major avg `-0.0676` n `8`; equity avg `0.0139` n `96`; fx avg `-0.0` n `6`; index avg `0.0116` n `25`; metal avg `0.0145` n `20`; unknown avg `-0.0917` n `769`
- 4h: commodity avg `-0.0251` n `12`; crypto_alt avg `-0.0371` n `230`; crypto_major avg `0.1162` n `8`; equity avg `0.2228` n `96`; fx avg `-0.0109` n `6`; index avg `0.0596` n `25`; metal avg `0.0408` n `20`; unknown avg `-0.3957` n `769`
- 24h: commodity avg `0.7671` n `12`; crypto_alt avg `-0.6539` n `230`; crypto_major avg `-0.3573` n `8`; equity avg `0.3026` n `95`; fx avg `0.0392` n `6`; index avg `-0.0373` n `25`; metal avg `0.0683` n `20`; unknown avg `0.1949` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
