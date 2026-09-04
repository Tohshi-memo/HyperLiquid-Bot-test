# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T05:22:26.693701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `0.036` n `232`; crypto_major avg `-0.006` n `8`; equity avg `0.114` n `133`; fx avg `-0.0335` n `6`; index avg `0.0382` n `26`; metal avg `-0.0082` n `20`; unknown avg `0.0098` n `793`
- 1h: commodity avg `-0.0933` n `12`; crypto_alt avg `-0.3166` n `232`; crypto_major avg `-0.1754` n `8`; equity avg `0.269` n `133`; fx avg `-0.0479` n `6`; index avg `0.0607` n `26`; metal avg `0.0251` n `20`; unknown avg `19.4227` n `791`
- 4h: commodity avg `-0.0808` n `12`; crypto_alt avg `-0.1886` n `232`; crypto_major avg `0.1399` n `8`; equity avg `0.4464` n `133`; fx avg `-0.042` n `6`; index avg `0.1148` n `26`; metal avg `-0.0767` n `20`; unknown avg `8.5879` n `791`
- 24h: commodity avg `-0.079` n `12`; crypto_alt avg `2.8001` n `232`; crypto_major avg `4.7723` n `8`; equity avg `2.5127` n `133`; fx avg `-0.1542` n `6`; index avg `0.479` n `26`; metal avg `0.5606` n `20`; unknown avg `25.2046` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
