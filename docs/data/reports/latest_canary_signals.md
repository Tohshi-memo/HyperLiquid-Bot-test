# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T20:07:19.165844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1326` n `12`; crypto_alt avg `-0.0678` n `228`; crypto_major avg `-0.0632` n `8`; equity avg `-0.023` n `67`; fx avg `0.0235` n `6`; index avg `0.0424` n `23`; metal avg `-0.0078` n `18`; unknown avg `-0.0359` n `396`
- 1h: commodity avg `-0.0994` n `12`; crypto_alt avg `0.1159` n `228`; crypto_major avg `0.0933` n `8`; equity avg `0.0923` n `67`; fx avg `-0.009` n `6`; index avg `0.1434` n `23`; metal avg `0.0353` n `18`; unknown avg `0.2383` n `396`
- 4h: commodity avg `-0.8029` n `12`; crypto_alt avg `1.2138` n `228`; crypto_major avg `0.7465` n `8`; equity avg `0.5644` n `67`; fx avg `-0.0086` n `6`; index avg `0.4354` n `23`; metal avg `0.1389` n `18`; unknown avg `0.7956` n `396`
- 24h: commodity avg `-0.6525` n `12`; crypto_alt avg `0.646` n `228`; crypto_major avg `0.3869` n `8`; equity avg `0.554` n `67`; fx avg `-0.0338` n `6`; index avg `0.4053` n `23`; metal avg `0.2382` n `18`; unknown avg `-0.5958` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
