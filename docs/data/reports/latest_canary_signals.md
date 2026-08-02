# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T03:07:29.042858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4221` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.3399` n `12`; crypto_alt avg `-0.0052` n `230`; crypto_major avg `0.0716` n `8`; equity avg `-0.0315` n `102`; fx avg `-0.0154` n `6`; index avg `-0.0013` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.0859` n `782`
- 1h: commodity avg `-0.5855` n `12`; crypto_alt avg `0.0284` n `230`; crypto_major avg `0.1195` n `8`; equity avg `0.5217` n `102`; fx avg `-0.0114` n `6`; index avg `0.1322` n `25`; metal avg `0.0972` n `20`; unknown avg `-0.0159` n `782`
- 4h: commodity avg `-1.2119` n `12`; crypto_alt avg `1.0668` n `230`; crypto_major avg `1.2102` n `8`; equity avg `1.0408` n `102`; fx avg `-0.0255` n `6`; index avg `0.226` n `25`; metal avg `0.1326` n `20`; unknown avg `1.9449` n `782`
- 24h: commodity avg `-1.2851` n `12`; crypto_alt avg `0.0512` n `230`; crypto_major avg `0.244` n `8`; equity avg `0.8369` n `102`; fx avg `-0.0995` n `6`; index avg `0.1773` n `25`; metal avg `0.2033` n `20`; unknown avg `-0.0659` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
