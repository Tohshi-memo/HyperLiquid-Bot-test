# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T22:22:20.106177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.48` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.8487` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5878` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0602` n `12`; crypto_alt avg `0.0742` n `228`; crypto_major avg `0.0214` n `8`; equity avg `-0.0406` n `69`; fx avg `0.0018` n `6`; index avg `0.0257` n `23`; metal avg `-0.002` n `18`; unknown avg `0.1227` n `422`
- 1h: commodity avg `-1.4557` n `12`; crypto_alt avg `-0.7573` n `228`; crypto_major avg `-0.584` n `8`; equity avg `0.024` n `69`; fx avg `-0.0067` n `6`; index avg `-0.0137` n `23`; metal avg `0.0307` n `18`; unknown avg `0.6244` n `422`
- 4h: commodity avg `0.1514` n `12`; crypto_alt avg `-0.7509` n `228`; crypto_major avg `-1.3293` n `8`; equity avg `0.5194` n `69`; fx avg `0.0053` n `6`; index avg `0.2585` n `23`; metal avg `0.0809` n `18`; unknown avg `0.891` n `422`
- 24h: commodity avg `0.1265` n `12`; crypto_alt avg `-3.559` n `228`; crypto_major avg `-5.084` n `8`; equity avg `1.3224` n `69`; fx avg `0.0829` n `6`; index avg `0.7636` n `23`; metal avg `0.5092` n `18`; unknown avg `-0.318` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
