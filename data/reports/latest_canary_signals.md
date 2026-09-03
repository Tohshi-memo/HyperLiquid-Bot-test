# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T23:07:31.271445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `0.1161` n `232`; crypto_major avg `0.1485` n `8`; equity avg `0.0285` n `133`; fx avg `0.0038` n `6`; index avg `0.008` n `26`; metal avg `-0.0107` n `20`; unknown avg `2.9291` n `790`
- 1h: commodity avg `0.0269` n `12`; crypto_alt avg `-0.3415` n `232`; crypto_major avg `-0.2221` n `8`; equity avg `0.0008` n `133`; fx avg `0.0145` n `6`; index avg `0.0116` n `26`; metal avg `-0.0247` n `20`; unknown avg `3.2836` n `784`
- 4h: commodity avg `0.039` n `12`; crypto_alt avg `-0.7289` n `232`; crypto_major avg `-0.2739` n `8`; equity avg `-0.0483` n `133`; fx avg `0.0197` n `6`; index avg `-0.0166` n `26`; metal avg `-0.0228` n `20`; unknown avg `0.7508` n `766`
- 24h: commodity avg `-0.0852` n `12`; crypto_alt avg `3.9049` n `232`; crypto_major avg `5.1353` n `8`; equity avg `1.2556` n `133`; fx avg `-0.2217` n `6`; index avg `0.1642` n `26`; metal avg `0.7902` n `20`; unknown avg `1.1391` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
