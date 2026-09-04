# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T08:07:31.425589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0534` n `12`; crypto_alt avg `0.1078` n `232`; crypto_major avg `-0.0463` n `8`; equity avg `0.0971` n `133`; fx avg `-0.002` n `6`; index avg `0.0078` n `26`; metal avg `0.0337` n `20`; unknown avg `0.1213` n `791`
- 1h: commodity avg `-0.1333` n `12`; crypto_alt avg `0.0743` n `232`; crypto_major avg `-0.313` n `8`; equity avg `0.3115` n `133`; fx avg `0.0109` n `6`; index avg `0.0429` n `26`; metal avg `0.1365` n `20`; unknown avg `0.115` n `791`
- 4h: commodity avg `-0.1747` n `12`; crypto_alt avg `-0.1243` n `232`; crypto_major avg `-0.3183` n `8`; equity avg `0.2961` n `133`; fx avg `-0.0269` n `6`; index avg `0.0538` n `26`; metal avg `0.179` n `20`; unknown avg `0.7013` n `755`
- 24h: commodity avg `0.0312` n `12`; crypto_alt avg `1.6475` n `232`; crypto_major avg `3.1938` n `8`; equity avg `1.6515` n `133`; fx avg `-0.0367` n `6`; index avg `0.3038` n `26`; metal avg `0.4536` n `20`; unknown avg `1.7606` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
