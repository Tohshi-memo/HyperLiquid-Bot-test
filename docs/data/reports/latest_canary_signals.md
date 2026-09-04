# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T04:22:35.477376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `0.2601` n `232`; crypto_major avg `0.2769` n `8`; equity avg `0.1138` n `133`; fx avg `0.0028` n `6`; index avg `0.022` n `26`; metal avg `0.0176` n `20`; unknown avg `11.9525` n `793`
- 1h: commodity avg `0.007` n `12`; crypto_alt avg `0.0644` n `232`; crypto_major avg `0.1339` n `8`; equity avg `0.0904` n `133`; fx avg `0.0219` n `6`; index avg `0.0289` n `26`; metal avg `-0.0308` n `20`; unknown avg `8.5941` n `791`
- 4h: commodity avg `0.0598` n `12`; crypto_alt avg `-0.3072` n `232`; crypto_major avg `-0.0088` n `8`; equity avg `0.2384` n `133`; fx avg `0.0433` n `6`; index avg `0.0609` n `26`; metal avg `-0.1222` n `20`; unknown avg `36.5721` n `784`
- 24h: commodity avg `-0.0855` n `12`; crypto_alt avg `2.9143` n `232`; crypto_major avg `4.5105` n `8`; equity avg `1.3593` n `133`; fx avg `-0.0819` n `6`; index avg `0.2079` n `26`; metal avg `0.4179` n `20`; unknown avg `2.1126` n `736`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
