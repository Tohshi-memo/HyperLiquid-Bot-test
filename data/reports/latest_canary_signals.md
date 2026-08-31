# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T15:07:29.592045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `-0.1279` n `232`; crypto_major avg `-0.04` n `8`; equity avg `0.0279` n `128`; fx avg `-0.0018` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0219` n `20`; unknown avg `0.0373` n `792`
- 1h: commodity avg `0.0454` n `12`; crypto_alt avg `0.5042` n `232`; crypto_major avg `0.6597` n `8`; equity avg `0.0271` n `128`; fx avg `0.0302` n `6`; index avg `-0.016` n `26`; metal avg `-0.0219` n `20`; unknown avg `0.5789` n `790`
- 4h: commodity avg `-0.0871` n `12`; crypto_alt avg `-0.249` n `232`; crypto_major avg `-0.1711` n `8`; equity avg `-0.1016` n `128`; fx avg `0.0526` n `6`; index avg `-0.0811` n `26`; metal avg `-0.3161` n `20`; unknown avg `0.2108` n `790`
- 24h: commodity avg `0.5445` n `12`; crypto_alt avg `-1.1459` n `231`; crypto_major avg `-1.5702` n `8`; equity avg `-0.562` n `128`; fx avg `-0.0822` n `6`; index avg `-0.1843` n `26`; metal avg `-0.5145` n `20`; unknown avg `0.8305` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
