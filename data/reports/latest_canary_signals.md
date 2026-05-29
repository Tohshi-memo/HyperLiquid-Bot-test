# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T14:07:20.264984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1437` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2474` n `12`; crypto_alt avg `-0.041` n `228`; crypto_major avg `-0.2368` n `8`; equity avg `0.13` n `69`; fx avg `-0.0111` n `6`; index avg `0.0255` n `23`; metal avg `0.0972` n `18`; unknown avg `-0.3088` n `417`
- 1h: commodity avg `0.3595` n `12`; crypto_alt avg `0.1805` n `228`; crypto_major avg `-0.1651` n `8`; equity avg `0.1554` n `69`; fx avg `0.0076` n `6`; index avg `-0.0372` n `23`; metal avg `0.1706` n `18`; unknown avg `-0.0696` n `417`
- 4h: commodity avg `0.3615` n `12`; crypto_alt avg `-1.3088` n `228`; crypto_major avg `-1.0135` n `8`; equity avg `0.0445` n `69`; fx avg `0.0177` n `6`; index avg `0.1302` n `23`; metal avg `0.1733` n `18`; unknown avg `0.1052` n `417`
- 24h: commodity avg `-0.0868` n `12`; crypto_alt avg `1.6282` n `228`; crypto_major avg `1.838` n `8`; equity avg `3.0153` n `69`; fx avg `0.1059` n `6`; index avg `1.2409` n `23`; metal avg `2.087` n `18`; unknown avg `1.2087` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
