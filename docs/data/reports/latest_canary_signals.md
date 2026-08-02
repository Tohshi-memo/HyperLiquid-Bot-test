# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T18:22:32.333071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `12`; crypto_alt avg `0.0407` n `230`; crypto_major avg `0.1233` n `8`; equity avg `0.024` n `102`; fx avg `-0.0019` n `6`; index avg `-0.0012` n `25`; metal avg `0.0159` n `20`; unknown avg `0.0129` n `782`
- 1h: commodity avg `-0.0578` n `12`; crypto_alt avg `0.1173` n `230`; crypto_major avg `0.2545` n `8`; equity avg `-0.0134` n `102`; fx avg `0.0103` n `6`; index avg `-0.0063` n `25`; metal avg `0.0368` n `20`; unknown avg `-0.0261` n `782`
- 4h: commodity avg `-0.1393` n `12`; crypto_alt avg `0.2391` n `230`; crypto_major avg `0.643` n `8`; equity avg `0.3809` n `102`; fx avg `0.0322` n `6`; index avg `0.0678` n `25`; metal avg `0.0938` n `20`; unknown avg `1.3488` n `782`
- 24h: commodity avg `-1.2519` n `12`; crypto_alt avg `1.0422` n `230`; crypto_major avg `1.4379` n `8`; equity avg `1.475` n `102`; fx avg `-0.116` n `6`; index avg `0.2936` n `25`; metal avg `0.3529` n `20`; unknown avg `1.5696` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
