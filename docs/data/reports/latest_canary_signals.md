# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T14:07:35.474644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `0.6305` n `232`; crypto_major avg `0.5095` n `8`; equity avg `0.0672` n `134`; fx avg `0.0027` n `6`; index avg `-0.0334` n `26`; metal avg `0.0441` n `20`; unknown avg `1.118` n `781`
- 1h: commodity avg `-0.0652` n `12`; crypto_alt avg `-0.5911` n `232`; crypto_major avg `-0.3982` n `8`; equity avg `-0.0873` n `134`; fx avg `0.0107` n `6`; index avg `-0.1049` n `26`; metal avg `-0.0987` n `20`; unknown avg `0.8918` n `781`
- 4h: commodity avg `-0.2592` n `12`; crypto_alt avg `-1.3303` n `232`; crypto_major avg `-0.9252` n `8`; equity avg `0.2498` n `134`; fx avg `0.016` n `6`; index avg `-0.0346` n `26`; metal avg `-0.0364` n `20`; unknown avg `0.4424` n `775`
- 24h: commodity avg `-0.1015` n `12`; crypto_alt avg `-0.9843` n `232`; crypto_major avg `-1.2872` n `8`; equity avg `0.1476` n `134`; fx avg `-0.1363` n `6`; index avg `-0.0948` n `26`; metal avg `0.0504` n `20`; unknown avg `7061.4076` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
