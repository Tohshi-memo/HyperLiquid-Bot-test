# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T02:37:29.501663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `13`; crypto_alt avg `-0.1885` n `239`; crypto_major avg `-0.2721` n `8`; equity avg `-0.0836` n `166`; fx avg `0.0092` n `6`; index avg `-0.025` n `27`; metal avg `-0.0218` n `20`; unknown avg `316.8952` n `1263`
- 1h: commodity avg `-0.0201` n `13`; crypto_alt avg `-0.4916` n `239`; crypto_major avg `-0.6465` n `8`; equity avg `-0.2709` n `166`; fx avg `0.0093` n `6`; index avg `-0.056` n `27`; metal avg `-0.049` n `20`; unknown avg `0.7793` n `1263`
- 4h: commodity avg `-0.0312` n `13`; crypto_alt avg `-0.4674` n `239`; crypto_major avg `-0.588` n `8`; equity avg `-0.1877` n `166`; fx avg `-0.0018` n `6`; index avg `-0.0172` n `27`; metal avg `-0.0257` n `20`; unknown avg `164.9636` n `1238`
- 24h: commodity avg `0.0016` n `13`; crypto_alt avg `0.0558` n `239`; crypto_major avg `1.6037` n `8`; equity avg `0.5661` n `166`; fx avg `-0.0406` n `6`; index avg `0.1388` n `27`; metal avg `0.0765` n `20`; unknown avg `418.5156` n `1080`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
