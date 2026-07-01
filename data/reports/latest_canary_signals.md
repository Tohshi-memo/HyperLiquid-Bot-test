# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T20:52:31.486027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `0.2144` n `228`; crypto_major avg `0.2098` n `8`; equity avg `0.1505` n `88`; fx avg `0.0005` n `6`; index avg `0.0178` n `25`; metal avg `-0.0044` n `20`; unknown avg `0.417` n `763`
- 1h: commodity avg `0.0106` n `12`; crypto_alt avg `0.2221` n `228`; crypto_major avg `-0.1028` n `8`; equity avg `-0.2099` n `88`; fx avg `0.0066` n `6`; index avg `-0.0437` n `25`; metal avg `-0.0582` n `20`; unknown avg `1.1956` n `763`
- 4h: commodity avg `-0.1227` n `12`; crypto_alt avg `-0.5281` n `228`; crypto_major avg `-0.381` n `8`; equity avg `-0.8646` n `88`; fx avg `0.0061` n `6`; index avg `-0.1408` n `25`; metal avg `-0.3444` n `20`; unknown avg `0.6118` n `761`
- 24h: commodity avg `-0.5988` n `12`; crypto_alt avg `1.7203` n `228`; crypto_major avg `1.2432` n `8`; equity avg `-1.6299` n `88`; fx avg `0.0026` n `6`; index avg `-0.5217` n `25`; metal avg `0.1761` n `20`; unknown avg `0.691` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
