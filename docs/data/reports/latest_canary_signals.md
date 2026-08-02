# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T17:37:30.671841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0268` n `12`; crypto_alt avg `0.0569` n `230`; crypto_major avg `0.104` n `8`; equity avg `-0.0524` n `102`; fx avg `0.0018` n `6`; index avg `-0.0099` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.0311` n `782`
- 1h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.0614` n `230`; crypto_major avg `0.2169` n `8`; equity avg `0.2155` n `102`; fx avg `0.0037` n `6`; index avg `0.0234` n `25`; metal avg `0.008` n `20`; unknown avg `0.1058` n `782`
- 4h: commodity avg `-0.2186` n `12`; crypto_alt avg `0.2479` n `230`; crypto_major avg `0.6139` n `8`; equity avg `0.3189` n `102`; fx avg `-0.0228` n `6`; index avg `0.0528` n `25`; metal avg `0.0455` n `20`; unknown avg `1.2361` n `782`
- 24h: commodity avg `-1.3314` n `12`; crypto_alt avg `0.8304` n `230`; crypto_major avg `1.1745` n `8`; equity avg `1.2983` n `102`; fx avg `-0.1399` n `6`; index avg `0.2734` n `25`; metal avg `0.299` n `20`; unknown avg `1.5716` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
