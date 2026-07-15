# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T19:37:25.824833+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.3` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1135` n `12`; crypto_alt avg `0.0264` n `230`; crypto_major avg `0.0481` n `8`; equity avg `0.2854` n `94`; fx avg `-0.0083` n `6`; index avg `0.0263` n `25`; metal avg `-0.0547` n `20`; unknown avg `0.0234` n `768`
- 1h: commodity avg `0.102` n `12`; crypto_alt avg `-0.355` n `230`; crypto_major avg `-0.5772` n `8`; equity avg `-0.2254` n `94`; fx avg `-0.0062` n `6`; index avg `-0.0406` n `25`; metal avg `-0.1079` n `20`; unknown avg `0.1053` n `768`
- 4h: commodity avg `0.4528` n `12`; crypto_alt avg `-0.5768` n `230`; crypto_major avg `-0.8215` n `8`; equity avg `0.0756` n `94`; fx avg `0.071` n `6`; index avg `0.051` n `25`; metal avg `0.2137` n `20`; unknown avg `-0.0003` n `768`
- 24h: commodity avg `0.1452` n `12`; crypto_alt avg `0.4214` n `230`; crypto_major avg `0.6431` n `8`; equity avg `-0.4731` n `93`; fx avg `0.2089` n `6`; index avg `-0.1672` n `25`; metal avg `0.1205` n `20`; unknown avg `0.2293` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
