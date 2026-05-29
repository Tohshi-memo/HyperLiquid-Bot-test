# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T14:22:22.383767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0557` n `12`; crypto_alt avg `-0.2021` n `228`; crypto_major avg `0.1441` n `8`; equity avg `-0.6206` n `69`; fx avg `-0.0088` n `6`; index avg `-0.1688` n `23`; metal avg `-0.3127` n `18`; unknown avg `0.3105` n `417`
- 1h: commodity avg `0.0505` n `12`; crypto_alt avg `0.038` n `228`; crypto_major avg `0.0458` n `8`; equity avg `-0.3434` n `69`; fx avg `-0.032` n `6`; index avg `-0.2404` n `23`; metal avg `-0.2982` n `18`; unknown avg `-0.0193` n `417`
- 4h: commodity avg `0.1992` n `12`; crypto_alt avg `-1.2766` n `228`; crypto_major avg `-0.8307` n `8`; equity avg `-0.5777` n `69`; fx avg `0.015` n `6`; index avg `-0.0598` n `23`; metal avg `-0.072` n `18`; unknown avg `0.8788` n `417`
- 24h: commodity avg `0.5657` n `12`; crypto_alt avg `0.6429` n `228`; crypto_major avg `1.0905` n `8`; equity avg `2.0491` n `69`; fx avg `0.0945` n `6`; index avg `0.7825` n `23`; metal avg `1.013` n `18`; unknown avg `1.115` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1754`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
