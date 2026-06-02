# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T19:37:27.728184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.97` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.1074` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0281` n `12`; crypto_alt avg `-0.9441` n `228`; crypto_major avg `-0.6457` n `8`; equity avg `-0.0831` n `69`; fx avg `0.0023` n `6`; index avg `-0.0646` n `23`; metal avg `-0.0338` n `18`; unknown avg `-0.3155` n `422`
- 1h: commodity avg `-0.0736` n `12`; crypto_alt avg `-1.5307` n `228`; crypto_major avg `-1.0654` n `8`; equity avg `0.0073` n `69`; fx avg `0.0315` n `6`; index avg `0.042` n `23`; metal avg `-0.0579` n `18`; unknown avg `-0.8933` n `422`
- 4h: commodity avg `0.5554` n `12`; crypto_alt avg `-0.0701` n `228`; crypto_major avg `-0.6685` n `8`; equity avg `-0.0061` n `69`; fx avg `-0.0095` n `6`; index avg `-0.0727` n `23`; metal avg `-0.6503` n `18`; unknown avg `0.3019` n `422`
- 24h: commodity avg `0.0173` n `12`; crypto_alt avg `-5.298` n `228`; crypto_major avg `-5.444` n `8`; equity avg `0.3744` n `69`; fx avg `0.0859` n `6`; index avg `0.2225` n `23`; metal avg `0.214` n `18`; unknown avg `-0.5754` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
