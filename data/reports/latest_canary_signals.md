# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T18:37:28.959610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0235` n `12`; crypto_alt avg `-0.0064` n `233`; crypto_major avg `-0.0436` n `8`; equity avg `-0.0007` n `136`; fx avg `0.0001` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.1224` n `806`
- 1h: commodity avg `0.0133` n `12`; crypto_alt avg `-0.1569` n `233`; crypto_major avg `-0.2324` n `8`; equity avg `-0.0165` n `136`; fx avg `-0.0039` n `6`; index avg `-0.0018` n `26`; metal avg `0.0027` n `20`; unknown avg `0.175` n `804`
- 4h: commodity avg `0.0625` n `12`; crypto_alt avg `-0.0148` n `233`; crypto_major avg `-0.4559` n `8`; equity avg `-0.0078` n `136`; fx avg `-0.0078` n `6`; index avg `0.0002` n `26`; metal avg `0.0086` n `20`; unknown avg `1.886` n `790`
- 24h: commodity avg `-0.1557` n `12`; crypto_alt avg `1.2766` n `233`; crypto_major avg `0.0193` n `8`; equity avg `-0.1681` n `136`; fx avg `-0.0224` n `6`; index avg `0.0056` n `26`; metal avg `0.0359` n `20`; unknown avg `1.3393` n `692`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
