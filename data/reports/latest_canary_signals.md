# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T14:22:24.646393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `-0.0491` n `234`; crypto_major avg `-0.235` n `8`; equity avg `-0.0588` n `141`; fx avg `-0.0042` n `6`; index avg `-0.005` n `26`; metal avg `-0.0028` n `20`; unknown avg `0.3305` n `962`
- 1h: commodity avg `-0.0407` n `12`; crypto_alt avg `0.1595` n `234`; crypto_major avg `-0.068` n `8`; equity avg `-0.0328` n `141`; fx avg `-0.0099` n `6`; index avg `-0.019` n `26`; metal avg `0.0027` n `20`; unknown avg `1.182` n `960`
- 4h: commodity avg `-0.0411` n `12`; crypto_alt avg `-0.763` n `234`; crypto_major avg `-0.5973` n `8`; equity avg `-0.0726` n `141`; fx avg `-0.0042` n `6`; index avg `-0.0387` n `26`; metal avg `-0.0197` n `20`; unknown avg `2.7057` n `954`
- 24h: commodity avg `-0.0194` n `12`; crypto_alt avg `0.2024` n `234`; crypto_major avg `0.3479` n `8`; equity avg `0.2755` n `141`; fx avg `-0.0397` n `6`; index avg `0.0004` n `26`; metal avg `-0.0178` n `20`; unknown avg `66.5468` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
