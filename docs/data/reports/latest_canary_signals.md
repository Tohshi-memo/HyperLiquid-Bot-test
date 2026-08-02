# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T07:07:32.277632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0315` n `12`; crypto_alt avg `0.0097` n `230`; crypto_major avg `-0.0249` n `8`; equity avg `-0.0328` n `102`; fx avg `-0.0074` n `6`; index avg `0.0057` n `25`; metal avg `-0.0041` n `20`; unknown avg `-0.0107` n `782`
- 1h: commodity avg `-0.0519` n `12`; crypto_alt avg `-0.1045` n `230`; crypto_major avg `-0.0768` n `8`; equity avg `-0.0773` n `102`; fx avg `-0.0164` n `6`; index avg `0.004` n `25`; metal avg `0.0116` n `20`; unknown avg `0.0547` n `782`
- 4h: commodity avg `0.1008` n `12`; crypto_alt avg `0.1483` n `230`; crypto_major avg `0.0374` n `8`; equity avg `-0.054` n `102`; fx avg `-0.0585` n `6`; index avg `0.0513` n `25`; metal avg `0.0552` n `20`; unknown avg `0.3848` n `766`
- 24h: commodity avg `-1.098` n `12`; crypto_alt avg `0.1994` n `230`; crypto_major avg `0.3619` n `8`; equity avg `0.7985` n `102`; fx avg `-0.1314` n `6`; index avg `0.264` n `25`; metal avg `0.2612` n `20`; unknown avg `0.3483` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
