# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T13:22:33.424125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `12`; crypto_alt avg `0.5276` n `234`; crypto_major avg `0.3009` n `8`; equity avg `0.0376` n `141`; fx avg `0.0185` n `6`; index avg `0.0121` n `26`; metal avg `0.0225` n `20`; unknown avg `405.2934` n `943`
- 1h: commodity avg `0.0319` n `12`; crypto_alt avg `0.9113` n `234`; crypto_major avg `0.5299` n `8`; equity avg `-0.0849` n `141`; fx avg `-0.0205` n `6`; index avg `0.0125` n `26`; metal avg `-0.0273` n `20`; unknown avg `4.7189` n `941`
- 4h: commodity avg `-0.1268` n `12`; crypto_alt avg `1.5569` n `234`; crypto_major avg `0.8455` n `8`; equity avg `0.3155` n `141`; fx avg `-0.0458` n `6`; index avg `0.0589` n `26`; metal avg `0.0505` n `20`; unknown avg `3.8155` n `935`
- 24h: commodity avg `0.5238` n `12`; crypto_alt avg `-2.7051` n `234`; crypto_major avg `-2.4756` n `8`; equity avg `-2.1786` n `141`; fx avg `-0.0152` n `6`; index avg `-0.3705` n `26`; metal avg `-0.2322` n `20`; unknown avg `588.1785` n `819`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
