# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T18:07:15.486092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.79` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `0.0273` n `228`; crypto_major avg `0.0488` n `8`; equity avg `-0.0336` n `65`; fx avg `0.0` n `5`; index avg `-0.0046` n `23`; metal avg `0.0054` n `18`; unknown avg `-0.0027` n `376`
- 1h: commodity avg `-0.0448` n `12`; crypto_alt avg `0.1433` n `228`; crypto_major avg `0.0372` n `8`; equity avg `-0.0028` n `65`; fx avg `0.0` n `5`; index avg `-0.0043` n `23`; metal avg `0.0197` n `18`; unknown avg `0.1833` n `376`
- 4h: commodity avg `0.2402` n `12`; crypto_alt avg `0.423` n `228`; crypto_major avg `0.1192` n `8`; equity avg `0.1194` n `65`; fx avg `-0.0191` n `5`; index avg `0.0106` n `23`; metal avg `-0.0047` n `18`; unknown avg `0.0928` n `376`
- 24h: commodity avg `0.1779` n `12`; crypto_alt avg `0.8426` n `228`; crypto_major avg `0.66` n `8`; equity avg `1.346` n `65`; fx avg `-0.0068` n `5`; index avg `0.2607` n `23`; metal avg `-0.3032` n `18`; unknown avg `0.0171` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
