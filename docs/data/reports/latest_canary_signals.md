# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T13:07:17.452996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `12`; crypto_alt avg `0.2574` n `228`; crypto_major avg `0.1326` n `8`; equity avg `0.0215` n `69`; fx avg `0.0014` n `6`; index avg `0.044` n `23`; metal avg `-0.0143` n `18`; unknown avg `0.7545` n `421`
- 1h: commodity avg `0.0354` n `12`; crypto_alt avg `0.1973` n `228`; crypto_major avg `0.1464` n `8`; equity avg `0.1099` n `69`; fx avg `0.0178` n `6`; index avg `0.0689` n `23`; metal avg `-0.0073` n `18`; unknown avg `-0.0481` n `421`
- 4h: commodity avg `0.2417` n `12`; crypto_alt avg `0.3539` n `228`; crypto_major avg `0.4878` n `8`; equity avg `0.2272` n `69`; fx avg `0.0183` n `6`; index avg `0.0754` n `23`; metal avg `0.0062` n `18`; unknown avg `0.749` n `421`
- 24h: commodity avg `-0.0489` n `12`; crypto_alt avg `2.9275` n `228`; crypto_major avg `3.0108` n `8`; equity avg `1.5233` n `69`; fx avg `0.1094` n `6`; index avg `0.0382` n `23`; metal avg `-0.0841` n `18`; unknown avg `1.4692` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
