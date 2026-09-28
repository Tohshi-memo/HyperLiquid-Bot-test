# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T17:22:36.226011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1936` n `12`; crypto_alt avg `0.7943` n `234`; crypto_major avg `0.7542` n `8`; equity avg `0.3386` n `141`; fx avg `-0.013` n `6`; index avg `0.0453` n `26`; metal avg `0.0902` n `20`; unknown avg `2.6224` n `962`
- 1h: commodity avg `-0.1572` n `12`; crypto_alt avg `0.197` n `234`; crypto_major avg `0.2493` n `8`; equity avg `0.146` n `141`; fx avg `0.0058` n `6`; index avg `0.0046` n `26`; metal avg `0.0639` n `20`; unknown avg `3.5984` n `960`
- 4h: commodity avg `-0.3658` n `12`; crypto_alt avg `-0.2671` n `234`; crypto_major avg `0.3491` n `8`; equity avg `-0.3719` n `141`; fx avg `0.0341` n `6`; index avg `-0.0605` n `26`; metal avg `0.0557` n `20`; unknown avg `121.8217` n `904`
- 24h: commodity avg `-0.5164` n `12`; crypto_alt avg `-2.7549` n `234`; crypto_major avg `-0.9634` n `8`; equity avg `-2.8833` n `141`; fx avg `0.0346` n `6`; index avg `-0.2455` n `26`; metal avg `-0.9414` n `20`; unknown avg `23.1782` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
