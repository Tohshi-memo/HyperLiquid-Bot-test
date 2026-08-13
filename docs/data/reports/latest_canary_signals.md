# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T16:14:04.278874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `-0.3295` n `230`; crypto_major avg `-0.2107` n `8`; equity avg `0.1026` n `113`; fx avg `-0.0053` n `6`; index avg `0.022` n `25`; metal avg `-0.0814` n `20`; unknown avg `-0.1437` n `787`
- 1h: commodity avg `0.124` n `12`; crypto_alt avg `-0.6941` n `230`; crypto_major avg `-0.5337` n `8`; equity avg `-0.4269` n `113`; fx avg `-0.0086` n `6`; index avg `-0.0556` n `25`; metal avg `-0.0736` n `20`; unknown avg `-0.1774` n `787`
- 4h: commodity avg `0.1748` n `12`; crypto_alt avg `-0.2704` n `230`; crypto_major avg `-0.0015` n `8`; equity avg `1.3881` n `113`; fx avg `-0.0221` n `6`; index avg `0.2606` n `25`; metal avg `-0.2476` n `20`; unknown avg `-0.1706` n `787`
- 24h: commodity avg `-0.2248` n `12`; crypto_alt avg `-0.5852` n `230`; crypto_major avg `-0.1461` n `8`; equity avg `1.3267` n `113`; fx avg `-0.0005` n `6`; index avg `0.3091` n `25`; metal avg `-0.5879` n `20`; unknown avg `0.1287` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.229`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1958`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1907`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
