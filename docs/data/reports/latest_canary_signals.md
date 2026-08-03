# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T02:22:30.205781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0347` n `12`; crypto_alt avg `0.1856` n `230`; crypto_major avg `0.1684` n `8`; equity avg `0.0955` n `102`; fx avg `-0.0148` n `6`; index avg `0.0116` n `25`; metal avg `-0.0126` n `20`; unknown avg `0.1469` n `784`
- 1h: commodity avg `-0.0742` n `12`; crypto_alt avg `0.1441` n `230`; crypto_major avg `0.0987` n `8`; equity avg `0.3612` n `102`; fx avg `-0.0157` n `6`; index avg `0.1125` n `25`; metal avg `0.0507` n `20`; unknown avg `-0.1541` n `784`
- 4h: commodity avg `0.0628` n `12`; crypto_alt avg `-0.7625` n `230`; crypto_major avg `-0.8959` n `8`; equity avg `0.5115` n `102`; fx avg `-0.3214` n `6`; index avg `0.0142` n `25`; metal avg `-0.0976` n `20`; unknown avg `0.1852` n `783`
- 24h: commodity avg `-0.3699` n `12`; crypto_alt avg `-0.3914` n `230`; crypto_major avg `0.0466` n `8`; equity avg `0.9442` n `102`; fx avg `-0.2895` n `6`; index avg `0.128` n `25`; metal avg `0.048` n `20`; unknown avg `1.2799` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
