# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T21:07:47.098461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0328` n `12`; crypto_alt avg `-0.3366` n `230`; crypto_major avg `-0.4006` n `8`; equity avg `-0.3875` n `102`; fx avg `0.0051` n `6`; index avg `-0.0386` n `25`; metal avg `0.007` n `20`; unknown avg `-0.2068` n `778`
- 1h: commodity avg `0.0382` n `12`; crypto_alt avg `-0.6917` n `230`; crypto_major avg `-0.4051` n `8`; equity avg `-0.8414` n `102`; fx avg `0.0025` n `6`; index avg `-0.0005` n `25`; metal avg `0.0864` n `20`; unknown avg `-0.2871` n `778`
- 4h: commodity avg `0.0722` n `12`; crypto_alt avg `-1.2308` n `230`; crypto_major avg `-1.0293` n `8`; equity avg `-2.1734` n `102`; fx avg `0.0759` n `6`; index avg `-0.3985` n `25`; metal avg `0.1247` n `20`; unknown avg `-0.6449` n `778`
- 24h: commodity avg `1.3025` n `12`; crypto_alt avg `-3.5614` n `230`; crypto_major avg `-1.5505` n `8`; equity avg `-4.5295` n `102`; fx avg `0.0265` n `6`; index avg `-0.7575` n `25`; metal avg `0.1544` n `20`; unknown avg `-0.8115` n `760`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
