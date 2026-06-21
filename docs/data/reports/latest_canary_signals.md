# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T15:37:28.079749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0254` n `12`; crypto_alt avg `0.0897` n `228`; crypto_major avg `0.0262` n `8`; equity avg `0.04` n `78`; fx avg `-0.0095` n `6`; index avg `-0.0089` n `23`; metal avg `-0.0032` n `18`; unknown avg `0.0112` n `702`
- 1h: commodity avg `0.0164` n `12`; crypto_alt avg `0.1627` n `228`; crypto_major avg `0.2617` n `8`; equity avg `0.1137` n `78`; fx avg `-0.014` n `6`; index avg `-0.01` n `23`; metal avg `0.0184` n `18`; unknown avg `0.1483` n `702`
- 4h: commodity avg `0.1753` n `12`; crypto_alt avg `0.4933` n `228`; crypto_major avg `0.416` n `8`; equity avg `0.0329` n `78`; fx avg `0.0225` n `6`; index avg `-0.0126` n `23`; metal avg `-0.0061` n `18`; unknown avg `0.3549` n `702`
- 24h: commodity avg `0.0382` n `12`; crypto_alt avg `1.2977` n `228`; crypto_major avg `-0.0479` n `8`; equity avg `0.3454` n `78`; fx avg `0.0355` n `6`; index avg `0.0098` n `23`; metal avg `-0.1143` n `18`; unknown avg `0.7001` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
