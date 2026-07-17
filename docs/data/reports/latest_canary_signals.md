# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T02:37:27.157041+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0797` n `12`; crypto_alt avg `-0.1337` n `230`; crypto_major avg `-0.1469` n `8`; equity avg `-0.3334` n `94`; fx avg `0.0109` n `6`; index avg `-0.0133` n `25`; metal avg `-0.0791` n `20`; unknown avg `-0.1483` n `768`
- 1h: commodity avg `-0.1353` n `12`; crypto_alt avg `-0.7023` n `230`; crypto_major avg `-0.6403` n `8`; equity avg `-0.8157` n `94`; fx avg `-0.0035` n `6`; index avg `-0.0792` n `25`; metal avg `-0.1909` n `20`; unknown avg `0.2764` n `768`
- 4h: commodity avg `-0.0948` n `12`; crypto_alt avg `-0.993` n `230`; crypto_major avg `-0.9309` n `8`; equity avg `-1.937` n `94`; fx avg `-0.0015` n `6`; index avg `-0.2441` n `25`; metal avg `-0.1567` n `20`; unknown avg `-0.1874` n `768`
- 24h: commodity avg `-0.1773` n `12`; crypto_alt avg `-2.4382` n `230`; crypto_major avg `-3.079` n `8`; equity avg `-5.4145` n `94`; fx avg `-0.1522` n `6`; index avg `-0.6697` n `25`; metal avg `-0.8155` n `20`; unknown avg `-0.7157` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
