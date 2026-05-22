# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T06:07:15.737586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.52` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1247` n `12`; crypto_alt avg `-0.4421` n `228`; crypto_major avg `-0.3208` n `8`; equity avg `-0.1845` n `67`; fx avg `-0.0086` n `6`; index avg `-0.1226` n `23`; metal avg `-0.3826` n `18`; unknown avg `-0.3413` n `376`
- 1h: commodity avg `0.301` n `12`; crypto_alt avg `-0.2361` n `228`; crypto_major avg `-0.3296` n `8`; equity avg `-0.1697` n `67`; fx avg `0.0111` n `6`; index avg `-0.0296` n `23`; metal avg `-0.2034` n `18`; unknown avg `0.0504` n `376`
- 4h: commodity avg `0.2034` n `12`; crypto_alt avg `0.2063` n `228`; crypto_major avg `-0.2606` n `8`; equity avg `0.2159` n `67`; fx avg `0.0574` n `6`; index avg `0.151` n `23`; metal avg `-0.0201` n `18`; unknown avg `-0.0657` n `376`
- 24h: commodity avg `-0.5135` n `12`; crypto_alt avg `1.912` n `228`; crypto_major avg `0.1876` n `8`; equity avg `1.2761` n `66`; fx avg `0.0957` n `6`; index avg `0.6432` n `23`; metal avg `0.5106` n `18`; unknown avg `2.415` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0445`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0424`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0407`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0405`, n `668`, weak_sample_signal
