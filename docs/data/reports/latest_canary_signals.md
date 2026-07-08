# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T07:07:26.896627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0605` n `12`; crypto_alt avg `-0.2786` n `229`; crypto_major avg `-0.33` n `8`; equity avg `-0.2167` n `91`; fx avg `0.0244` n `6`; index avg `-0.0373` n `25`; metal avg `-0.1118` n `20`; unknown avg `-0.0504` n `763`
- 1h: commodity avg `0.0285` n `12`; crypto_alt avg `-0.3653` n `229`; crypto_major avg `-0.4029` n `8`; equity avg `-0.3472` n `91`; fx avg `-0.044` n `6`; index avg `-0.0713` n `25`; metal avg `-0.0627` n `20`; unknown avg `-0.2332` n `763`
- 4h: commodity avg `0.1447` n `12`; crypto_alt avg `-0.6132` n `229`; crypto_major avg `-0.9296` n `8`; equity avg `-0.7889` n `91`; fx avg `-0.0561` n `6`; index avg `-0.2945` n `25`; metal avg `-0.0424` n `20`; unknown avg `-0.2851` n `743`
- 24h: commodity avg `0.8509` n `12`; crypto_alt avg `-3.2332` n `229`; crypto_major avg `-2.9504` n `8`; equity avg `-2.145` n `91`; fx avg `-0.2898` n `6`; index avg `-0.4188` n `25`; metal avg `-0.0446` n `20`; unknown avg `-0.6966` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
