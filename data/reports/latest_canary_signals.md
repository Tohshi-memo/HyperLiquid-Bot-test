# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T12:37:29.452492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0179` n `13`; crypto_alt avg `-0.3629` n `239`; crypto_major avg `-0.1465` n `8`; equity avg `0.0819` n `164`; fx avg `0.0013` n `6`; index avg `-0.007` n `27`; metal avg `0.0069` n `20`; unknown avg `12.6336` n `1266`
- 1h: commodity avg `0.2362` n `13`; crypto_alt avg `-0.6672` n `239`; crypto_major avg `-0.4874` n `8`; equity avg `-0.2828` n `164`; fx avg `-0.0241` n `6`; index avg `-0.0325` n `27`; metal avg `-0.1065` n `20`; unknown avg `10.1948` n `1258`
- 4h: commodity avg `0.1412` n `13`; crypto_alt avg `-0.2509` n `239`; crypto_major avg `0.0092` n `8`; equity avg `0.312` n `164`; fx avg `-0.0052` n `6`; index avg `0.0689` n `27`; metal avg `-0.1553` n `20`; unknown avg `199.3905` n `1256`
- 24h: commodity avg `-0.0165` n `13`; crypto_alt avg `-0.0407` n `239`; crypto_major avg `-0.0203` n `8`; equity avg `1.1537` n `164`; fx avg `0.0212` n `6`; index avg `0.322` n `27`; metal avg `-0.1828` n `20`; unknown avg `3.0899` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
