# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T17:52:26.507030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0198` n `12`; crypto_alt avg `0.0045` n `230`; crypto_major avg `0.0181` n `8`; equity avg `0.0004` n `102`; fx avg `0.0111` n `6`; index avg `-0.0084` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.0039` n `782`
- 1h: commodity avg `-0.0092` n `12`; crypto_alt avg `0.0444` n `230`; crypto_major avg `0.1396` n `8`; equity avg `0.0924` n `102`; fx avg `0.0077` n `6`; index avg `0.0059` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.0438` n `782`
- 4h: commodity avg `-0.1731` n `12`; crypto_alt avg `0.1919` n `230`; crypto_major avg `0.5664` n `8`; equity avg `0.3404` n `102`; fx avg `-0.0076` n `6`; index avg `0.043` n `25`; metal avg `0.0581` n `20`; unknown avg `1.3275` n `782`
- 24h: commodity avg `-1.3063` n `12`; crypto_alt avg `0.9254` n `230`; crypto_major avg `1.2469` n `8`; equity avg `1.3473` n `102`; fx avg `-0.1348` n `6`; index avg `0.2959` n `25`; metal avg `0.3173` n `20`; unknown avg `1.5707` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
