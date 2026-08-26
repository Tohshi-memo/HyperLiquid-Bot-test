# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T19:52:27.065095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `0.0859` n `231`; crypto_major avg `-0.0038` n `8`; equity avg `-0.1161` n `122`; fx avg `0.0042` n `6`; index avg `-0.0044` n `25`; metal avg `-0.0193` n `20`; unknown avg `-0.018` n `797`
- 1h: commodity avg `0.0236` n `12`; crypto_alt avg `0.0517` n `231`; crypto_major avg `0.0557` n `8`; equity avg `-0.017` n `122`; fx avg `-0.0037` n `6`; index avg `0.0005` n `25`; metal avg `-0.0303` n `20`; unknown avg `0.0249` n `797`
- 4h: commodity avg `-0.2042` n `12`; crypto_alt avg `0.4809` n `231`; crypto_major avg `0.5452` n `8`; equity avg `0.3744` n `122`; fx avg `-0.0054` n `6`; index avg `0.0258` n `25`; metal avg `-0.0172` n `20`; unknown avg `0.1784` n `797`
- 24h: commodity avg `0.2015` n `12`; crypto_alt avg `-1.2225` n `231`; crypto_major avg `-1.3568` n `8`; equity avg `-0.1954` n `122`; fx avg `-0.0414` n `6`; index avg `0.0405` n `25`; metal avg `-0.4439` n `20`; unknown avg `0.5421` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
