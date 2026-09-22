# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T10:37:40.459516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0455` n `12`; crypto_alt avg `-0.0936` n `234`; crypto_major avg `-0.1388` n `8`; equity avg `0.0216` n `140`; fx avg `0.005` n `6`; index avg `-0.0044` n `26`; metal avg `0.0478` n `20`; unknown avg `0.5608` n `944`
- 1h: commodity avg `-0.2587` n `12`; crypto_alt avg `-0.6144` n `234`; crypto_major avg `-0.2852` n `8`; equity avg `0.351` n `140`; fx avg `-0.0027` n `6`; index avg `0.0476` n `26`; metal avg `0.1134` n `20`; unknown avg `4.7745` n `940`
- 4h: commodity avg `-0.7134` n `12`; crypto_alt avg `-0.4513` n `234`; crypto_major avg `-0.0659` n `8`; equity avg `0.4001` n `140`; fx avg `-0.1113` n `6`; index avg `0.0414` n `26`; metal avg `0.1303` n `20`; unknown avg `3.5891` n `934`
- 24h: commodity avg `-0.5396` n `12`; crypto_alt avg `0.4864` n `234`; crypto_major avg `1.6023` n `8`; equity avg `0.9854` n `140`; fx avg `-0.2518` n `6`; index avg `0.2546` n `26`; metal avg `-0.0494` n `20`; unknown avg `1130.1044` n `790`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
