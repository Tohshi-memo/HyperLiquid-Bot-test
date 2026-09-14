# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T19:37:30.444861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0171` n `12`; crypto_alt avg `-0.2529` n `233`; crypto_major avg `-0.2855` n `8`; equity avg `-0.0788` n `136`; fx avg `0.0088` n `6`; index avg `-0.0275` n `27`; metal avg `-0.0317` n `20`; unknown avg `8.7669` n `908`
- 1h: commodity avg `0.1112` n `12`; crypto_alt avg `-0.4043` n `233`; crypto_major avg `-0.3444` n `8`; equity avg `-0.3296` n `136`; fx avg `0.0019` n `6`; index avg `-0.0741` n `27`; metal avg `-0.1246` n `20`; unknown avg `3.5021` n `906`
- 4h: commodity avg `-0.1821` n `12`; crypto_alt avg `0.8963` n `233`; crypto_major avg `1.2632` n `8`; equity avg `-0.0119` n `136`; fx avg `0.0324` n `6`; index avg `0.0099` n `27`; metal avg `-0.0594` n `20`; unknown avg `0.7084` n `878`
- 24h: commodity avg `0.1107` n `12`; crypto_alt avg `0.4318` n `233`; crypto_major avg `2.3543` n `8`; equity avg `-0.468` n `136`; fx avg `0.0552` n `6`; index avg `-0.161` n `27`; metal avg `-0.3942` n `20`; unknown avg `3.7457` n `696`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
