# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T19:37:29.311173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.53` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0538` n `12`; crypto_alt avg `-0.3805` n `230`; crypto_major avg `-0.3216` n `8`; equity avg `-0.5719` n `102`; fx avg `0.0046` n `6`; index avg `-0.1018` n `25`; metal avg `-0.104` n `20`; unknown avg `-0.2734` n `778`
- 1h: commodity avg `0.0121` n `12`; crypto_alt avg `-0.2699` n `230`; crypto_major avg `-0.4627` n `8`; equity avg `-0.6739` n `102`; fx avg `0.0323` n `6`; index avg `-0.1676` n `25`; metal avg `0.0866` n `20`; unknown avg `-0.2805` n `778`
- 4h: commodity avg `0.1013` n `12`; crypto_alt avg `-0.0392` n `230`; crypto_major avg `-0.1723` n `8`; equity avg `0.1561` n `102`; fx avg `0.0558` n `6`; index avg `0.0588` n `25`; metal avg `0.5229` n `20`; unknown avg `-0.3675` n `778`
- 24h: commodity avg `1.4034` n `12`; crypto_alt avg `-2.1989` n `230`; crypto_major avg `-0.4743` n `8`; equity avg `-1.9715` n `102`; fx avg `-0.0062` n `6`; index avg `-0.3649` n `25`; metal avg `0.3094` n `20`; unknown avg `-0.7591` n `760`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
