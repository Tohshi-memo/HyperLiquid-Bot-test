# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T18:07:35.266670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0418` n `12`; crypto_alt avg `0.0843` n `234`; crypto_major avg `0.1162` n `8`; equity avg `0.0202` n `140`; fx avg `-0.0012` n `6`; index avg `0.0165` n `26`; metal avg `0.0073` n `20`; unknown avg `0.0041` n `938`
- 1h: commodity avg `-0.032` n `12`; crypto_alt avg `0.3663` n `234`; crypto_major avg `0.4037` n `8`; equity avg `0.1837` n `140`; fx avg `0.012` n `6`; index avg `0.0301` n `26`; metal avg `0.0375` n `20`; unknown avg `0.0004` n `920`
- 4h: commodity avg `-0.2802` n `12`; crypto_alt avg `1.0199` n `234`; crypto_major avg `1.1573` n `8`; equity avg `0.6689` n `140`; fx avg `-0.0525` n `6`; index avg `0.0371` n `26`; metal avg `0.2543` n `20`; unknown avg `-0.2255` n `906`
- 24h: commodity avg `-0.1711` n `12`; crypto_alt avg `5.8677` n `234`; crypto_major avg `6.5055` n `8`; equity avg `0.7749` n `140`; fx avg `0.1888` n `6`; index avg `-0.1015` n `26`; metal avg `0.331` n `20`; unknown avg `1.6354` n `717`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
