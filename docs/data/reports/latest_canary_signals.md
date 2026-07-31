# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T14:52:29.182276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0438` n `12`; crypto_alt avg `-0.0121` n `230`; crypto_major avg `-0.0615` n `8`; equity avg `0.2171` n `102`; fx avg `0.0324` n `6`; index avg `0.0872` n `25`; metal avg `0.1001` n `20`; unknown avg `0.0071` n `780`
- 1h: commodity avg `0.0094` n `12`; crypto_alt avg `0.2442` n `230`; crypto_major avg `-0.1061` n `8`; equity avg `-0.1879` n `102`; fx avg `0.0615` n `6`; index avg `0.0261` n `25`; metal avg `0.2376` n `20`; unknown avg `0.4719` n `780`
- 4h: commodity avg `0.1687` n `12`; crypto_alt avg `-0.1397` n `230`; crypto_major avg `-0.6795` n `8`; equity avg `-1.9398` n `102`; fx avg `-0.0655` n `6`; index avg `-0.2651` n `25`; metal avg `-0.095` n `20`; unknown avg `0.7448` n `780`
- 24h: commodity avg `0.2319` n `12`; crypto_alt avg `-0.8548` n `230`; crypto_major avg `-1.3819` n `8`; equity avg `1.0478` n `102`; fx avg `0.0832` n `6`; index avg `0.329` n `25`; metal avg `-0.1404` n `20`; unknown avg `1.7162` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
