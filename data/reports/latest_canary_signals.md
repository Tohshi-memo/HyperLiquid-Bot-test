# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T18:22:18.099560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0201` n `12`; crypto_alt avg `0.1319` n `228`; crypto_major avg `0.1969` n `8`; equity avg `0.2484` n `69`; fx avg `0.0119` n `6`; index avg `0.0224` n `23`; metal avg `-0.0598` n `18`; unknown avg `0.1123` n `417`
- 1h: commodity avg `-0.0456` n `12`; crypto_alt avg `0.9535` n `228`; crypto_major avg `0.7073` n `8`; equity avg `0.6839` n `69`; fx avg `0.0024` n `6`; index avg `0.0894` n `23`; metal avg `0.1142` n `18`; unknown avg `0.2381` n `417`
- 4h: commodity avg `0.397` n `12`; crypto_alt avg `2.2618` n `228`; crypto_major avg `1.8886` n `8`; equity avg `1.8991` n `69`; fx avg `-0.0068` n `6`; index avg `1.007` n `23`; metal avg `1.1494` n `18`; unknown avg `0.3977` n `417`
- 24h: commodity avg `0.8603` n `12`; crypto_alt avg `-2.4621` n `228`; crypto_major avg `-0.4289` n `8`; equity avg `1.5291` n `68`; fx avg `-0.0066` n `6`; index avg `1.0729` n `23`; metal avg `0.6497` n `18`; unknown avg `-0.3602` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1913`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
