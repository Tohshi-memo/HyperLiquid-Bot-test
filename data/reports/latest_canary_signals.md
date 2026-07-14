# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T10:07:26.437086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0555` n `12`; crypto_alt avg `0.1449` n `230`; crypto_major avg `0.1985` n `8`; equity avg `0.0544` n `92`; fx avg `0.0028` n `6`; index avg `0.0039` n `25`; metal avg `-0.0395` n `20`; unknown avg `0.0187` n `766`
- 1h: commodity avg `0.0` n `12`; crypto_alt avg `-0.0175` n `230`; crypto_major avg `-0.0019` n `8`; equity avg `0.132` n `92`; fx avg `-0.0008` n `6`; index avg `0.0044` n `25`; metal avg `-0.0134` n `20`; unknown avg `-0.0378` n `766`
- 4h: commodity avg `0.3357` n `12`; crypto_alt avg `-0.0852` n `230`; crypto_major avg `0.0482` n `8`; equity avg `0.2699` n `92`; fx avg `0.0765` n `6`; index avg `-0.0069` n `25`; metal avg `-0.0713` n `20`; unknown avg `0.0206` n `766`
- 24h: commodity avg `1.592` n `12`; crypto_alt avg `-0.8599` n `230`; crypto_major avg `-0.5595` n `8`; equity avg `-0.46` n `92`; fx avg `-0.005` n `6`; index avg `-0.1225` n `25`; metal avg `-0.1603` n `20`; unknown avg `-0.2979` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
