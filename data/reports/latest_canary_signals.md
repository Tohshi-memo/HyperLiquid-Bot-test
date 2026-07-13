# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T20:07:29.554407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `12`; crypto_alt avg `0.0001` n `230`; crypto_major avg `-0.0115` n `8`; equity avg `-0.0793` n `92`; fx avg `0.001` n `6`; index avg `-0.0081` n `25`; metal avg `0.0351` n `20`; unknown avg `-0.0063` n `766`
- 1h: commodity avg `0.0224` n `12`; crypto_alt avg `0.2164` n `230`; crypto_major avg `0.3237` n `8`; equity avg `0.059` n `92`; fx avg `0.0054` n `6`; index avg `-0.0276` n `25`; metal avg `0.0421` n `20`; unknown avg `0.0188` n `766`
- 4h: commodity avg `0.5832` n `12`; crypto_alt avg `-0.8316` n `230`; crypto_major avg `-0.3889` n `8`; equity avg `-0.7271` n `92`; fx avg `-0.0025` n `6`; index avg `-0.1132` n `25`; metal avg `-0.1189` n `20`; unknown avg `-0.277` n `766`
- 24h: commodity avg `0.6062` n `12`; crypto_alt avg `-2.2982` n `230`; crypto_major avg `-2.8905` n `8`; equity avg `-3.2718` n `92`; fx avg `-0.0724` n `6`; index avg `-0.6378` n `25`; metal avg `-0.5093` n `20`; unknown avg `-0.2789` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1762`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
