# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T10:37:31.223263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0403` n `12`; crypto_alt avg `0.284` n `230`; crypto_major avg `0.3588` n `8`; equity avg `0.0988` n `114`; fx avg `0.0058` n `6`; index avg `0.0101` n `25`; metal avg `0.0266` n `20`; unknown avg `0.1485` n `792`
- 1h: commodity avg `0.0143` n `12`; crypto_alt avg `0.2095` n `230`; crypto_major avg `0.3077` n `8`; equity avg `0.1217` n `114`; fx avg `0.0172` n `6`; index avg `0.0214` n `25`; metal avg `0.0464` n `20`; unknown avg `0.1548` n `792`
- 4h: commodity avg `0.1599` n `12`; crypto_alt avg `-0.1617` n `230`; crypto_major avg `0.1037` n `8`; equity avg `0.1991` n `114`; fx avg `0.0248` n `6`; index avg `-0.0054` n `25`; metal avg `-0.0044` n `20`; unknown avg `-0.023` n `792`
- 24h: commodity avg `-0.071` n `12`; crypto_alt avg `-0.0421` n `230`; crypto_major avg `0.9292` n `8`; equity avg `1.2801` n `114`; fx avg `-0.0113` n `6`; index avg `0.1533` n `25`; metal avg `0.1945` n `20`; unknown avg `-0.0397` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
