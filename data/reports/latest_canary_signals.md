# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T15:52:26.484338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `-0.0365` n `230`; crypto_major avg `-0.0438` n `8`; equity avg `0.0009` n `102`; fx avg `-0.0063` n `6`; index avg `0.0098` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.0446` n `782`
- 1h: commodity avg `-0.0061` n `12`; crypto_alt avg `0.0106` n `230`; crypto_major avg `0.0051` n `8`; equity avg `0.0446` n `102`; fx avg `-0.0028` n `6`; index avg `-0.0029` n `25`; metal avg `0.0124` n `20`; unknown avg `1.1253` n `782`
- 4h: commodity avg `-0.1329` n `12`; crypto_alt avg `0.0626` n `230`; crypto_major avg `0.1345` n `8`; equity avg `0.0717` n `102`; fx avg `-0.0408` n `6`; index avg `0.0131` n `25`; metal avg `0.0327` n `20`; unknown avg `1.0839` n `782`
- 24h: commodity avg `-1.1125` n `12`; crypto_alt avg `0.3547` n `230`; crypto_major avg `0.2001` n `8`; equity avg `0.944` n `102`; fx avg `-0.1318` n `6`; index avg `0.2092` n `25`; metal avg `0.2514` n `20`; unknown avg `1.4506` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
