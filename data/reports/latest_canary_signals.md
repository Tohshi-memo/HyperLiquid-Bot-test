# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T15:37:37.751918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0312` n `12`; crypto_alt avg `0.1036` n `230`; crypto_major avg `0.1806` n `8`; equity avg `0.0374` n `108`; fx avg `-0.0021` n `6`; index avg `-0.0132` n `25`; metal avg `0.0289` n `20`; unknown avg `0.0045` n `782`
- 1h: commodity avg `-0.0166` n `12`; crypto_alt avg `0.1459` n `230`; crypto_major avg `0.2403` n `8`; equity avg `0.3515` n `108`; fx avg `-0.0174` n `6`; index avg `-0.007` n `25`; metal avg `0.1024` n `20`; unknown avg `-0.1229` n `782`
- 4h: commodity avg `-0.261` n `12`; crypto_alt avg `0.1543` n `230`; crypto_major avg `0.4951` n `8`; equity avg `-0.0369` n `108`; fx avg `-0.0316` n `6`; index avg `-0.0506` n `25`; metal avg `0.1765` n `20`; unknown avg `0.0002` n `782`
- 24h: commodity avg `-0.183` n `12`; crypto_alt avg `1.1672` n `230`; crypto_major avg `1.0602` n `8`; equity avg `0.5357` n `108`; fx avg `0.0246` n `6`; index avg `0.169` n `25`; metal avg `0.8989` n `20`; unknown avg `0.7934` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
