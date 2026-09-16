# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T04:52:28.543391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0279` n `12`; crypto_alt avg `-0.1717` n `234`; crypto_major avg `-0.2031` n `8`; equity avg `-0.0185` n `137`; fx avg `0.0004` n `6`; index avg `0.0043` n `27`; metal avg `-0.0246` n `20`; unknown avg `3.4895` n `919`
- 1h: commodity avg `-0.0249` n `12`; crypto_alt avg `0.3008` n `234`; crypto_major avg `0.1194` n `8`; equity avg `-0.0579` n `137`; fx avg `-0.0172` n `6`; index avg `-0.0172` n `27`; metal avg `-0.0074` n `20`; unknown avg `5.0093` n `911`
- 4h: commodity avg `-0.0945` n `12`; crypto_alt avg `0.0739` n `234`; crypto_major avg `0.2069` n `8`; equity avg `0.5513` n `137`; fx avg `-0.0451` n `6`; index avg `0.0529` n `27`; metal avg `0.2569` n `20`; unknown avg `4.4263` n `907`
- 24h: commodity avg `0.1464` n `12`; crypto_alt avg `-3.2734` n `234`; crypto_major avg `-3.1342` n `8`; equity avg `-0.3779` n `137`; fx avg `0.2153` n `6`; index avg `0.0338` n `27`; metal avg `0.3454` n `20`; unknown avg `18796.1884` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
