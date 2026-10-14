# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T14:07:27.242836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0564` n `13`; crypto_alt avg `-0.834` n `235`; crypto_major avg `-0.7219` n `8`; equity avg `-0.3126` n `151`; fx avg `-0.038` n `6`; index avg `-0.0558` n `26`; metal avg `-0.042` n `20`; unknown avg `-0.35` n `1134`
- 1h: commodity avg `-0.0197` n `13`; crypto_alt avg `-0.6047` n `235`; crypto_major avg `-0.6657` n `8`; equity avg `-0.6058` n `151`; fx avg `-0.0288` n `6`; index avg `-0.0301` n `26`; metal avg `-0.1174` n `20`; unknown avg `41.3836` n `1132`
- 4h: commodity avg `-0.2482` n `13`; crypto_alt avg `-1.6287` n `235`; crypto_major avg `-1.1792` n `8`; equity avg `-1.883` n `151`; fx avg `-0.112` n `6`; index avg `-0.2668` n `26`; metal avg `-0.5395` n `20`; unknown avg `2.9077` n `1125`
- 24h: commodity avg `0.1254` n `13`; crypto_alt avg `-2.417` n `235`; crypto_major avg `-1.7896` n `8`; equity avg `-2.1188` n `151`; fx avg `-0.1545` n `6`; index avg `-0.272` n `26`; metal avg `-0.7634` n `20`; unknown avg `1262.5777` n `981`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1308`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1141`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0969`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0732`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0553`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0545`, n `666`, weak_sample_signal
