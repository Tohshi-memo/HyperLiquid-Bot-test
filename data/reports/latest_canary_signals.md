# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T21:37:37.219258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0526` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.2024` n `232`; crypto_major avg `-0.1712` n `8`; equity avg `-0.0513` n `131`; fx avg `-0.0111` n `6`; index avg `0.0011` n `26`; metal avg `0.0112` n `20`; unknown avg `-0.1235` n `793`
- 1h: commodity avg `-0.1146` n `12`; crypto_alt avg `-0.4762` n `232`; crypto_major avg `-0.5734` n `8`; equity avg `-0.1546` n `131`; fx avg `-0.0043` n `6`; index avg `-0.0022` n `26`; metal avg `0.0588` n `20`; unknown avg `-0.1999` n `785`
- 4h: commodity avg `0.1495` n `12`; crypto_alt avg `-0.8672` n `232`; crypto_major avg `-1.085` n `8`; equity avg `-0.2544` n `131`; fx avg `0.0048` n `6`; index avg `-0.0324` n `26`; metal avg `-0.1704` n `20`; unknown avg `1.6678` n `773`
- 24h: commodity avg `0.775` n `12`; crypto_alt avg `-0.8583` n `232`; crypto_major avg `-2.5685` n `8`; equity avg `-2.0267` n `130`; fx avg `0.0349` n `6`; index avg `-0.3312` n `26`; metal avg `-0.8634` n `20`; unknown avg `-0.5742` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0441`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0386`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0309`, n `668`, weak_sample_signal
