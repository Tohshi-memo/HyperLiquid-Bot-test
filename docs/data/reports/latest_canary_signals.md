# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T21:42:42.859500+00:00`
- Correlation status: `ready`
- Asset price records: `586`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1698` n `12`; crypto_alt avg `0.252` n `228`; crypto_major avg `0.0702` n `8`; equity avg `-0.3114` n `65`; fx avg `0.0014` n `5`; index avg `-0.1372` n `23`; metal avg `-0.0099` n `18`; unknown avg `-0.2056` n `365`
- 1h: commodity avg `0.4851` n `12`; crypto_alt avg `-0.0872` n `228`; crypto_major avg `-0.0045` n `8`; equity avg `-0.5086` n `65`; fx avg `-0.0219` n `5`; index avg `-0.2084` n `23`; metal avg `-0.499` n `18`; unknown avg `-0.3089` n `365`
- 4h: commodity avg `0.6691` n `12`; crypto_alt avg `0.6474` n `228`; crypto_major avg `0.0487` n `8`; equity avg `-0.4665` n `65`; fx avg `-0.0282` n `5`; index avg `-0.2089` n `23`; metal avg `-0.657` n `18`; unknown avg `-0.6485` n `365`
- 24h: commodity avg `1.0472` n `12`; crypto_alt avg `0.7316` n `228`; crypto_major avg `-2.0599` n `8`; equity avg `-1.3539` n `65`; fx avg `0.1729` n `5`; index avg `-0.9546` n `23`; metal avg `-0.4177` n `18`; unknown avg `-0.6107` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1397`, n `582`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `582`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.112`, n `582`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1034`, n `582`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.095`, n `578`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0945`, n `578`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0856`, n `578`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0852`, n `578`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0852`, n `578`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0812`, n `578`, weak_sample_signal
