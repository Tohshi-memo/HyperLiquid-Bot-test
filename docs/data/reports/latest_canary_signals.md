# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T23:52:28.458887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `13`; crypto_alt avg `-0.0223` n `239`; crypto_major avg `-0.0223` n `8`; equity avg `0.1461` n `162`; fx avg `0.0024` n `6`; index avg `0.0268` n `27`; metal avg `0.0713` n `20`; unknown avg `0.0552` n `1265`
- 1h: commodity avg `-0.2296` n `13`; crypto_alt avg `0.2365` n `239`; crypto_major avg `0.3336` n `8`; equity avg `0.9883` n `162`; fx avg `-0.0066` n `6`; index avg `0.1985` n `27`; metal avg `0.3528` n `20`; unknown avg `0.438` n `1259`
- 4h: commodity avg `-0.2991` n `13`; crypto_alt avg `0.6046` n `239`; crypto_major avg `0.8407` n `8`; equity avg `1.2423` n `162`; fx avg `0.0017` n `6`; index avg `0.2109` n `27`; metal avg `0.4114` n `20`; unknown avg `0.5918` n `1185`
- 24h: commodity avg `-0.308` n `13`; crypto_alt avg `2.4281` n `239`; crypto_major avg `3.6095` n `8`; equity avg `2.1892` n `162`; fx avg `0.0167` n `6`; index avg `0.294` n `27`; metal avg `0.5906` n `20`; unknown avg `3.1424` n `1138`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
