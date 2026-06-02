# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T17:07:26.959959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.22` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.7891` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.5854` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `2.484` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `0.0581` n `228`; crypto_major avg `-0.0053` n `8`; equity avg `-0.1293` n `69`; fx avg `-0.0157` n `6`; index avg `-0.0115` n `23`; metal avg `-0.076` n `18`; unknown avg `-0.1647` n `422`
- 1h: commodity avg `0.271` n `12`; crypto_alt avg `0.821` n `228`; crypto_major avg `0.0968` n `8`; equity avg `0.0723` n `69`; fx avg `-0.0367` n `6`; index avg `-0.105` n `23`; metal avg `-0.3174` n `18`; unknown avg `0.1706` n `422`
- 4h: commodity avg `0.7149` n `12`; crypto_alt avg `-2.1477` n `228`; crypto_major avg `-2.0742` n `8`; equity avg `0.5112` n `69`; fx avg `-0.0351` n `6`; index avg `0.4098` n `23`; metal avg `-0.6285` n `18`; unknown avg `-0.1872` n `422`
- 24h: commodity avg `-0.4156` n `12`; crypto_alt avg `-2.7864` n `228`; crypto_major avg `-3.3747` n `8`; equity avg `0.3493` n `69`; fx avg `0.0969` n `6`; index avg `0.5566` n `23`; metal avg `0.5938` n `18`; unknown avg `-0.3408` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
