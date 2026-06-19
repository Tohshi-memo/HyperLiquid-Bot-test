# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T21:59:13.290389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2273` n `12`; crypto_alt avg `-0.1502` n `228`; crypto_major avg `-0.1731` n `8`; equity avg `-0.0508` n `78`; fx avg `-0.0142` n `6`; index avg `-0.0025` n `23`; metal avg `0.0017` n `18`; unknown avg `0.4111` n `687`
- 1h: commodity avg `0.2519` n `12`; crypto_alt avg `-0.3054` n `228`; crypto_major avg `-0.343` n `8`; equity avg `-0.0611` n `78`; fx avg `-0.0727` n `6`; index avg `-0.007` n `23`; metal avg `-0.0059` n `18`; unknown avg `-0.2929` n `687`
- 4h: commodity avg `0.3242` n `12`; crypto_alt avg `-0.7167` n `228`; crypto_major avg `-0.3827` n `8`; equity avg `-0.0808` n `78`; fx avg `-0.0992` n `6`; index avg `-0.0085` n `23`; metal avg `0.1452` n `18`; unknown avg `-0.2908` n `687`
- 24h: commodity avg `0.5785` n `12`; crypto_alt avg `-3.9271` n `228`; crypto_major avg `-4.8273` n `8`; equity avg `0.6495` n `78`; fx avg `-0.1668` n `6`; index avg `0.2062` n `23`; metal avg `-4.1155` n `18`; unknown avg `-0.5602` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
