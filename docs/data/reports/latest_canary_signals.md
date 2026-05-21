# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T17:33:42.067297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.02` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.7865` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.2578` n `12`; crypto_alt avg `0.1975` n `228`; crypto_major avg `0.1127` n `8`; equity avg `-0.1178` n `67`; fx avg `0.0016` n `6`; index avg `0.0131` n `23`; metal avg `-0.0769` n `18`; unknown avg `0.6721` n `386`
- 1h: commodity avg `-0.7989` n `12`; crypto_alt avg `1.1394` n `228`; crypto_major avg `1.02` n `8`; equity avg `0.7223` n `67`; fx avg `-0.0122` n `6`; index avg `0.4286` n `23`; metal avg `0.5504` n `18`; unknown avg `1.358` n `385`
- 4h: commodity avg `-1.4952` n `12`; crypto_alt avg `1.775` n `228`; crypto_major avg `1.2913` n `8`; equity avg `0.9699` n `67`; fx avg `-0.0185` n `6`; index avg `0.4583` n `23`; metal avg `1.5612` n `18`; unknown avg `2.1969` n `385`
- 24h: commodity avg `0.169` n `12`; crypto_alt avg `1.7061` n `228`; crypto_major avg `2.3502` n `8`; equity avg `1.5658` n `66`; fx avg `-0.0048` n `6`; index avg `0.5635` n `23`; metal avg `0.3782` n `18`; unknown avg `7.3859` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0487`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.047`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
