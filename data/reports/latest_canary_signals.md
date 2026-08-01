# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T22:52:28.639653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.031` n `12`; crypto_alt avg `-0.0834` n `230`; crypto_major avg `-0.0362` n `8`; equity avg `0.0305` n `102`; fx avg `-0.0233` n `6`; index avg `0.0098` n `25`; metal avg `-0.0062` n `20`; unknown avg `-0.0435` n `782`
- 1h: commodity avg `-0.0441` n `12`; crypto_alt avg `-0.0964` n `230`; crypto_major avg `0.005` n `8`; equity avg `-0.0886` n `102`; fx avg `-0.0186` n `6`; index avg `-0.0219` n `25`; metal avg `-0.0006` n `20`; unknown avg `0.2152` n `782`
- 4h: commodity avg `-0.1275` n `12`; crypto_alt avg `0.6411` n `230`; crypto_major avg `0.8076` n `8`; equity avg `0.2844` n `102`; fx avg `-0.0` n `6`; index avg `0.0193` n `25`; metal avg `0.0784` n `20`; unknown avg `0.2969` n `782`
- 24h: commodity avg `-0.1485` n `12`; crypto_alt avg `-0.3591` n `230`; crypto_major avg `-0.7625` n `8`; equity avg `-0.0837` n `102`; fx avg `-0.0665` n `6`; index avg `-0.0283` n `25`; metal avg `0.0391` n `20`; unknown avg `-0.0052` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
