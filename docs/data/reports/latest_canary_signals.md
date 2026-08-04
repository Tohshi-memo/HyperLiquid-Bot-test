# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T09:07:27.911129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `-0.0362` n `230`; crypto_major avg `-0.135` n `8`; equity avg `-0.2225` n `107`; fx avg `0.0065` n `6`; index avg `-0.064` n `25`; metal avg `-0.0476` n `20`; unknown avg `-0.0021` n `781`
- 1h: commodity avg `0.254` n `12`; crypto_alt avg `-0.1254` n `230`; crypto_major avg `-0.2983` n `8`; equity avg `-0.5118` n `107`; fx avg `0.0186` n `6`; index avg `-0.1119` n `25`; metal avg `-0.1778` n `20`; unknown avg `-0.0541` n `781`
- 4h: commodity avg `0.1558` n `12`; crypto_alt avg `-0.2124` n `230`; crypto_major avg `-0.3468` n `8`; equity avg `0.689` n `107`; fx avg `0.0905` n `6`; index avg `0.0715` n `25`; metal avg `0.0085` n `20`; unknown avg `0.841` n `765`
- 24h: commodity avg `0.3558` n `12`; crypto_alt avg `1.1858` n `230`; crypto_major avg `1.2726` n `8`; equity avg `2.9641` n `107`; fx avg `0.0868` n `6`; index avg `0.2536` n `25`; metal avg `0.0499` n `20`; unknown avg `1.1021` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
