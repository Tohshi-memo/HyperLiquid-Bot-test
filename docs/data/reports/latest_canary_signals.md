# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T09:37:29.547906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0234` n `12`; crypto_alt avg `0.0676` n `230`; crypto_major avg `0.1084` n `8`; equity avg `0.2543` n `96`; fx avg `0.0112` n `6`; index avg `0.0245` n `25`; metal avg `-0.0184` n `20`; unknown avg `0.0314` n `769`
- 1h: commodity avg `0.2345` n `12`; crypto_alt avg `0.6096` n `230`; crypto_major avg `0.5566` n `8`; equity avg `0.6503` n `96`; fx avg `0.015` n `6`; index avg `0.0629` n `25`; metal avg `0.162` n `20`; unknown avg `0.0109` n `768`
- 4h: commodity avg `0.1644` n `12`; crypto_alt avg `-0.0929` n `230`; crypto_major avg `0.0587` n `8`; equity avg `0.0575` n `96`; fx avg `0.0684` n `6`; index avg `-0.0083` n `25`; metal avg `0.1174` n `20`; unknown avg `-0.0006` n `736`
- 24h: commodity avg `0.1076` n `12`; crypto_alt avg `-1.4414` n `230`; crypto_major avg `-2.6281` n `8`; equity avg `-5.3943` n `94`; fx avg `0.0001` n `6`; index avg `-0.7822` n `25`; metal avg `-0.7229` n `20`; unknown avg `-0.4634` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
