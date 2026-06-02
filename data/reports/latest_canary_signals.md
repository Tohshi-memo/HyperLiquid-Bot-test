# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T21:07:25.884481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.9` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.1354` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.053` n `12`; crypto_alt avg `0.0317` n `228`; crypto_major avg `-0.0523` n `8`; equity avg `0.141` n `69`; fx avg `-0.0131` n `6`; index avg `0.0233` n `23`; metal avg `-0.0007` n `18`; unknown avg `0.2439` n `422`
- 1h: commodity avg `-0.0941` n `12`; crypto_alt avg `0.1324` n `228`; crypto_major avg `-0.3002` n `8`; equity avg `0.3647` n `69`; fx avg `-0.0277` n `6`; index avg `-0.0399` n `23`; metal avg `0.0145` n `18`; unknown avg `0.3719` n `422`
- 4h: commodity avg `0.046` n `12`; crypto_alt avg `-0.4535` n `228`; crypto_major avg `-0.9357` n `8`; equity avg `0.3314` n `69`; fx avg `-0.0145` n `6`; index avg `0.1997` n `23`; metal avg `-0.077` n `18`; unknown avg `-0.2647` n `422`
- 24h: commodity avg `-0.0729` n `12`; crypto_alt avg `-3.2325` n `228`; crypto_major avg `-4.4999` n `8`; equity avg `1.1592` n `69`; fx avg `0.0631` n `6`; index avg `0.683` n `23`; metal avg `0.4785` n `18`; unknown avg `-0.3033` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
