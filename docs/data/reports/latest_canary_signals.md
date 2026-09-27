# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T23:22:28.965190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0322` n `12`; crypto_alt avg `0.1939` n `234`; crypto_major avg `0.2543` n `8`; equity avg `-0.0001` n `141`; fx avg `0.0051` n `6`; index avg `0.0264` n `26`; metal avg `0.0146` n `20`; unknown avg `1.5898` n `962`
- 1h: commodity avg `0.0201` n `12`; crypto_alt avg `0.182` n `234`; crypto_major avg `0.0178` n `8`; equity avg `-0.1015` n `141`; fx avg `-0.0022` n `6`; index avg `0.0176` n `26`; metal avg `-0.0309` n `20`; unknown avg `2.3608` n `936`
- 4h: commodity avg `-0.2693` n `12`; crypto_alt avg `-0.5762` n `234`; crypto_major avg `-0.6276` n `8`; equity avg `-0.3709` n `141`; fx avg `-0.0145` n `6`; index avg `-0.0696` n `26`; metal avg `-0.1693` n `20`; unknown avg `2.396` n `886`
- 24h: commodity avg `-0.4694` n `12`; crypto_alt avg `0.4328` n `234`; crypto_major avg `-0.2137` n `8`; equity avg `-0.0383` n `141`; fx avg `-0.0165` n `6`; index avg `-0.0307` n `26`; metal avg `-0.1774` n `20`; unknown avg `4.9206` n `827`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
