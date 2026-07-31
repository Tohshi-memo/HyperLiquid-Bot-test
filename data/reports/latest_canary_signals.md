# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T17:22:30.068739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.043` n `12`; crypto_alt avg `0.1418` n `230`; crypto_major avg `0.0888` n `8`; equity avg `0.0989` n `102`; fx avg `0.0039` n `6`; index avg `0.0149` n `25`; metal avg `0.0478` n `20`; unknown avg `-0.0047` n `780`
- 1h: commodity avg `0.0875` n `12`; crypto_alt avg `0.2001` n `230`; crypto_major avg `-0.054` n `8`; equity avg `0.5267` n `102`; fx avg `0.0552` n `6`; index avg `0.0807` n `25`; metal avg `0.0208` n `20`; unknown avg `-0.2196` n `780`
- 4h: commodity avg `-0.1728` n `12`; crypto_alt avg `-0.0419` n `230`; crypto_major avg `-1.1272` n `8`; equity avg `-1.9528` n `102`; fx avg `0.0118` n `6`; index avg `-0.1773` n `25`; metal avg `0.0734` n `20`; unknown avg `-0.2231` n `780`
- 24h: commodity avg `0.0956` n `12`; crypto_alt avg `-0.2239` n `230`; crypto_major avg `-1.8932` n `8`; equity avg `0.4022` n `102`; fx avg `0.1269` n `6`; index avg `0.2991` n `25`; metal avg `-0.3445` n `20`; unknown avg `0.4497` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
