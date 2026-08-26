# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T21:07:25.144164+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0319` n `12`; crypto_alt avg `0.385` n `231`; crypto_major avg `0.3937` n `8`; equity avg `0.488` n `122`; fx avg `-0.0101` n `6`; index avg `0.0868` n `25`; metal avg `0.0214` n `20`; unknown avg `0.1995` n `797`
- 1h: commodity avg `0.0241` n `12`; crypto_alt avg `0.3149` n `231`; crypto_major avg `0.1252` n `8`; equity avg `0.7947` n `122`; fx avg `-0.0152` n `6`; index avg `0.1208` n `25`; metal avg `-0.0111` n `20`; unknown avg `0.1288` n `797`
- 4h: commodity avg `-0.2026` n `12`; crypto_alt avg `0.8896` n `231`; crypto_major avg `0.8643` n `8`; equity avg `1.4291` n `122`; fx avg `-0.0281` n `6`; index avg `0.185` n `25`; metal avg `-0.011` n `20`; unknown avg `0.3093` n `797`
- 24h: commodity avg `0.3385` n `12`; crypto_alt avg `0.8875` n `231`; crypto_major avg `0.6312` n `8`; equity avg `1.0385` n `122`; fx avg `-0.0536` n `6`; index avg `0.1469` n `25`; metal avg `-0.3581` n `20`; unknown avg `1.0124` n `779`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
