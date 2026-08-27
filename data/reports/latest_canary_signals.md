# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T19:07:35.584782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `0.2264` n `231`; crypto_major avg `0.5238` n `8`; equity avg `0.0922` n `127`; fx avg `0.0018` n `6`; index avg `0.029` n `26`; metal avg `0.0552` n `20`; unknown avg `-0.0843` n `792`
- 1h: commodity avg `-0.1627` n `12`; crypto_alt avg `-0.3103` n `231`; crypto_major avg `0.1194` n `8`; equity avg `0.1368` n `127`; fx avg `0.0001` n `6`; index avg `0.0052` n `26`; metal avg `0.0642` n `20`; unknown avg `0.7267` n `792`
- 4h: commodity avg `0.2601` n `12`; crypto_alt avg `0.0643` n `231`; crypto_major avg `0.4724` n `8`; equity avg `0.1286` n `127`; fx avg `0.0184` n `6`; index avg `-0.0174` n `26`; metal avg `0.2866` n `20`; unknown avg `0.3851` n `792`
- 24h: commodity avg `0.4559` n `12`; crypto_alt avg `3.1465` n `231`; crypto_major avg `4.4547` n `8`; equity avg `1.4236` n `127`; fx avg `-0.0416` n `6`; index avg `0.1018` n `26`; metal avg `0.2735` n `20`; unknown avg `1.1438` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
