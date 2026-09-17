# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T10:07:29.513555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.133` n `12`; crypto_alt avg `-0.1617` n `234`; crypto_major avg `-0.1599` n `8`; equity avg `0.0268` n `137`; fx avg `0.0071` n `6`; index avg `0.0129` n `27`; metal avg `-0.0044` n `20`; unknown avg `0.1442` n `919`
- 1h: commodity avg `-0.1495` n `12`; crypto_alt avg `-0.4393` n `234`; crypto_major avg `-0.4998` n `8`; equity avg `-0.074` n `137`; fx avg `0.013` n `6`; index avg `0.0021` n `27`; metal avg `-0.005` n `20`; unknown avg `0.2431` n `919`
- 4h: commodity avg `-0.1682` n `12`; crypto_alt avg `0.3567` n `234`; crypto_major avg `0.1915` n `8`; equity avg `0.8088` n `137`; fx avg `0.049` n `6`; index avg `0.1407` n `27`; metal avg `-0.0118` n `20`; unknown avg `0.0004` n `911`
- 24h: commodity avg `-0.8123` n `10`; crypto_alt avg `3.0347` n `232`; crypto_major avg `1.6044` n `7`; equity avg `1.6034` n `132`; fx avg `0.102` n `6`; index avg `0.1091` n `23`; metal avg `-0.2164` n `13`; unknown avg `0.6866` n `702`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
