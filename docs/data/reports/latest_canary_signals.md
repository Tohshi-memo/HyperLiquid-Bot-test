# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T18:37:31.037337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `-0.3393` n `234`; crypto_major avg `-0.169` n `8`; equity avg `-0.072` n `141`; fx avg `0.0006` n `6`; index avg `-0.0121` n `26`; metal avg `-0.0271` n `20`; unknown avg `0.2675` n `963`
- 1h: commodity avg `-0.0195` n `12`; crypto_alt avg `0.1101` n `234`; crypto_major avg `-0.0092` n `8`; equity avg `0.0395` n `141`; fx avg `-0.002` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0437` n `20`; unknown avg `0.3795` n `961`
- 4h: commodity avg `-0.4164` n `12`; crypto_alt avg `0.8422` n `234`; crypto_major avg `0.744` n `8`; equity avg `0.4173` n `141`; fx avg `0.015` n `6`; index avg `0.0555` n `26`; metal avg `0.0329` n `20`; unknown avg `16.2179` n `954`
- 24h: commodity avg `-0.4906` n `12`; crypto_alt avg `-3.2503` n `234`; crypto_major avg `-1.6794` n `8`; equity avg `-3.0545` n `141`; fx avg `0.0417` n `6`; index avg `-0.2738` n `26`; metal avg `-0.9854` n `20`; unknown avg `22.5682` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1797`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
