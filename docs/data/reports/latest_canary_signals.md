# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T19:52:17.858934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0716` n `12`; crypto_alt avg `-0.1393` n `228`; crypto_major avg `-0.0098` n `8`; equity avg `0.067` n `67`; fx avg `0.0056` n `6`; index avg `0.0973` n `23`; metal avg `0.0004` n `18`; unknown avg `0.0722` n `396`
- 1h: commodity avg `-0.2291` n `12`; crypto_alt avg `-0.0792` n `228`; crypto_major avg `0.0044` n `8`; equity avg `0.0956` n `67`; fx avg `-0.0025` n `6`; index avg `0.1098` n `23`; metal avg `0.0159` n `18`; unknown avg `-0.1146` n `396`
- 4h: commodity avg `-0.9271` n `12`; crypto_alt avg `1.3675` n `228`; crypto_major avg `0.9694` n `8`; equity avg `0.6424` n `67`; fx avg `-0.0058` n `6`; index avg `0.342` n `23`; metal avg `0.1456` n `18`; unknown avg `1.0358` n `396`
- 24h: commodity avg `-0.6665` n `12`; crypto_alt avg `0.752` n `228`; crypto_major avg `0.4248` n `8`; equity avg `0.5994` n `67`; fx avg `-0.0296` n `6`; index avg `0.3981` n `23`; metal avg `0.133` n `18`; unknown avg `-0.6905` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
