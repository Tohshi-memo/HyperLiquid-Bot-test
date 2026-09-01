# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T02:22:22.315208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0202` n `12`; crypto_alt avg `-0.0992` n `232`; crypto_major avg `-0.0165` n `8`; equity avg `-0.0212` n `130`; fx avg `-0.0144` n `6`; index avg `0.0053` n `26`; metal avg `0.0071` n `20`; unknown avg `0.0523` n `792`
- 1h: commodity avg `-0.025` n `12`; crypto_alt avg `-0.2376` n `232`; crypto_major avg `-0.215` n `8`; equity avg `-0.1111` n `130`; fx avg `-0.0338` n `6`; index avg `-0.0279` n `26`; metal avg `-0.0303` n `20`; unknown avg `0.2321` n `790`
- 4h: commodity avg `0.0554` n `12`; crypto_alt avg `0.3317` n `232`; crypto_major avg `-0.363` n `8`; equity avg `0.0179` n `130`; fx avg `0.0052` n `6`; index avg `0.0535` n `26`; metal avg `0.0503` n `20`; unknown avg `1.2673` n `790`
- 24h: commodity avg `0.3389` n `12`; crypto_alt avg `1.6483` n `231`; crypto_major avg `1.4045` n `8`; equity avg `1.353` n `130`; fx avg `-0.0429` n `6`; index avg `0.1899` n `26`; metal avg `0.0947` n `20`; unknown avg `0.0657` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
