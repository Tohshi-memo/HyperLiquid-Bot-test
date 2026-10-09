# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T19:22:25.620488+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0147` n `13`; crypto_alt avg `-0.0248` n `235`; crypto_major avg `-0.0161` n `8`; equity avg `0.1018` n `150`; fx avg `-0.0087` n `6`; index avg `0.0024` n `26`; metal avg `-0.0461` n `20`; unknown avg `-0.0567` n `1092`
- 1h: commodity avg `-0.2124` n `13`; crypto_alt avg `-0.2603` n `235`; crypto_major avg `-0.1174` n `8`; equity avg `0.0551` n `150`; fx avg `-0.0022` n `6`; index avg `0.0147` n `26`; metal avg `-0.0147` n `20`; unknown avg `1.2568` n `1090`
- 4h: commodity avg `-0.4185` n `13`; crypto_alt avg `0.4747` n `235`; crypto_major avg `-0.0954` n `8`; equity avg `0.273` n `150`; fx avg `0.0071` n `6`; index avg `0.0439` n `26`; metal avg `0.0063` n `20`; unknown avg `2.0933` n `1020`
- 24h: commodity avg `-0.253` n `13`; crypto_alt avg `2.2563` n `235`; crypto_major avg `0.9537` n `8`; equity avg `1.3056` n `150`; fx avg `0.0327` n `6`; index avg `0.2071` n `26`; metal avg `0.622` n `20`; unknown avg `2.0622` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1588`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1426`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1315`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1257`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1222`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1115`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1015`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `669`, weak_sample_signal
