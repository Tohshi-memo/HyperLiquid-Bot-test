# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T21:37:27.191276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `13`; crypto_alt avg `-0.2349` n `239`; crypto_major avg `-0.1655` n `8`; equity avg `-0.0496` n `166`; fx avg `0.0026` n `6`; index avg `-0.0017` n `27`; metal avg `-0.0136` n `20`; unknown avg `0.509` n `1260`
- 1h: commodity avg `-0.0016` n `13`; crypto_alt avg `-0.2714` n `239`; crypto_major avg `-0.15` n `8`; equity avg `-0.034` n `166`; fx avg `-0.0166` n `6`; index avg `0.009` n `27`; metal avg `-0.0145` n `20`; unknown avg `41.4138` n `1242`
- 4h: commodity avg `0.0594` n `13`; crypto_alt avg `-0.286` n `239`; crypto_major avg `0.1848` n `8`; equity avg `0.2505` n `166`; fx avg `0.0059` n `6`; index avg `0.0594` n `27`; metal avg `0.011` n `20`; unknown avg `-0.2682` n `1176`
- 24h: commodity avg `0.0315` n `13`; crypto_alt avg `0.6584` n `239`; crypto_major avg `2.2752` n `8`; equity avg `1.2368` n `166`; fx avg `-0.0866` n `6`; index avg `0.2296` n `27`; metal avg `0.2372` n `20`; unknown avg `184.5286` n `1084`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
