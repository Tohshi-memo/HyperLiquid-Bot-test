# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T20:07:21.127112+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0547` n `12`; crypto_alt avg `0.162` n `228`; crypto_major avg `0.1186` n `8`; equity avg `-0.0004` n `69`; fx avg `-0.0016` n `6`; index avg `-0.202` n `23`; metal avg `0.009` n `18`; unknown avg `-0.304` n `421`
- 1h: commodity avg `-0.0245` n `12`; crypto_alt avg `0.0774` n `228`; crypto_major avg `0.0517` n `8`; equity avg `0.0875` n `69`; fx avg `-0.0009` n `6`; index avg `-0.164` n `23`; metal avg `-0.0055` n `18`; unknown avg `-0.4507` n `421`
- 4h: commodity avg `0.4569` n `12`; crypto_alt avg `0.3787` n `228`; crypto_major avg `0.7158` n `8`; equity avg `0.0848` n `69`; fx avg `-0.0014` n `6`; index avg `-0.1105` n `23`; metal avg `-0.009` n `18`; unknown avg `-0.1401` n `421`
- 24h: commodity avg `-0.12` n `12`; crypto_alt avg `1.6465` n `228`; crypto_major avg `2.6475` n `8`; equity avg `0.8186` n `69`; fx avg `-0.0206` n `6`; index avg `-0.1346` n `23`; metal avg `-0.0347` n `18`; unknown avg `0.0907` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1876`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
