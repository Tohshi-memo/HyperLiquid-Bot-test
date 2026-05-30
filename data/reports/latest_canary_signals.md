# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T05:52:21.303672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `12`; crypto_alt avg `0.1107` n `228`; crypto_major avg `0.0925` n `8`; equity avg `0.007` n `69`; fx avg `0.0062` n `6`; index avg `0.0293` n `23`; metal avg `-0.0002` n `18`; unknown avg `-0.3056` n `419`
- 1h: commodity avg `0.0166` n `12`; crypto_alt avg `0.6132` n `228`; crypto_major avg `0.6296` n `8`; equity avg `0.1569` n `69`; fx avg `0.0077` n `6`; index avg `0.0362` n `23`; metal avg `0.0084` n `18`; unknown avg `0.1683` n `419`
- 4h: commodity avg `-0.2589` n `12`; crypto_alt avg `0.1293` n `228`; crypto_major avg `0.2483` n `8`; equity avg `0.1945` n `69`; fx avg `0.0009` n `6`; index avg `0.0531` n `23`; metal avg `-0.0116` n `18`; unknown avg `-0.2783` n `419`
- 24h: commodity avg `-0.316` n `12`; crypto_alt avg `1.9002` n `228`; crypto_major avg `2.0395` n `8`; equity avg `0.9866` n `69`; fx avg `0.0872` n `6`; index avg `0.0752` n `23`; metal avg `0.0639` n `18`; unknown avg `0.7918` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
