# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T20:37:33.055790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0148` n `12`; crypto_alt avg `-0.1888` n `230`; crypto_major avg `-0.0185` n `8`; equity avg `-0.1871` n `102`; fx avg `0.002` n `6`; index avg `0.0084` n `25`; metal avg `0.0901` n `20`; unknown avg `-0.0238` n `778`
- 1h: commodity avg `-0.0128` n `12`; crypto_alt avg `-0.8737` n `230`; crypto_major avg `-0.4565` n `8`; equity avg `-1.6659` n `102`; fx avg `0.0089` n `6`; index avg `-0.3874` n `25`; metal avg `-0.187` n `20`; unknown avg `-0.1403` n `778`
- 4h: commodity avg `0.1182` n `12`; crypto_alt avg `-0.7051` n `230`; crypto_major avg `-0.3402` n `8`; equity avg `-1.108` n `102`; fx avg `0.0949` n `6`; index avg `-0.2536` n `25`; metal avg `0.3054` n `20`; unknown avg `-0.5488` n `778`
- 24h: commodity avg `1.3664` n `12`; crypto_alt avg `-2.9414` n `230`; crypto_major avg `-0.9487` n `8`; equity avg `-4.0056` n `102`; fx avg `0.0166` n `6`; index avg `-0.7293` n `25`; metal avg `0.1355` n `20`; unknown avg `-0.7458` n `760`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
