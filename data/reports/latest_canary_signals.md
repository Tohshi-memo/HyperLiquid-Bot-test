# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T20:01:50.962471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `0.0106` n `230`; crypto_major avg `-0.0155` n `8`; equity avg `-0.0106` n `102`; fx avg `0.0041` n `6`; index avg `-0.0097` n `25`; metal avg `-0.0111` n `20`; unknown avg `-0.0117` n `783`
- 1h: commodity avg `0.0021` n `12`; crypto_alt avg `0.0076` n `230`; crypto_major avg `0.1221` n `8`; equity avg `0.0497` n `102`; fx avg `0.0564` n `6`; index avg `0.0001` n `25`; metal avg `0.0128` n `20`; unknown avg `-0.0431` n `782`
- 4h: commodity avg `-0.1384` n `12`; crypto_alt avg `0.3021` n `230`; crypto_major avg `0.8857` n `8`; equity avg `0.4244` n `102`; fx avg `0.0842` n `6`; index avg `0.0417` n `25`; metal avg `0.083` n `20`; unknown avg `0.5751` n `782`
- 24h: commodity avg `-1.3627` n `12`; crypto_alt avg `1.4509` n `230`; crypto_major avg `2.0895` n `8`; equity avg `1.7161` n `102`; fx avg `-0.0697` n `6`; index avg `0.3216` n `25`; metal avg `0.3365` n `20`; unknown avg `1.6238` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
