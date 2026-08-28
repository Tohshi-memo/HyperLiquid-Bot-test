# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T02:07:27.300892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0466` n `12`; crypto_alt avg `-0.4062` n `231`; crypto_major avg `-0.3294` n `8`; equity avg `0.0563` n `127`; fx avg `0.0086` n `6`; index avg `0.0215` n `26`; metal avg `0.0253` n `20`; unknown avg `0.0771` n `792`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.4145` n `231`; crypto_major avg `-0.3919` n `8`; equity avg `0.104` n `127`; fx avg `-0.013` n `6`; index avg `0.0203` n `26`; metal avg `-0.135` n `20`; unknown avg `0.1216` n `792`
- 4h: commodity avg `-0.0271` n `12`; crypto_alt avg `-0.1728` n `231`; crypto_major avg `-0.515` n `8`; equity avg `0.2525` n `127`; fx avg `-0.0391` n `6`; index avg `0.0678` n `26`; metal avg `-0.1406` n `20`; unknown avg `-0.0333` n `792`
- 24h: commodity avg `0.3374` n `12`; crypto_alt avg `1.2434` n `231`; crypto_major avg `1.8436` n `8`; equity avg `0.3099` n `127`; fx avg `-0.0053` n `6`; index avg `0.052` n `26`; metal avg `-0.2374` n `20`; unknown avg `0.7459` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
