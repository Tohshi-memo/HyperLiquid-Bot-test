# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T00:37:30.781692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.2174` n `231`; crypto_major avg `0.1595` n `8`; equity avg `0.0592` n `127`; fx avg `-0.0314` n `6`; index avg `0.0299` n `26`; metal avg `-0.0428` n `20`; unknown avg `-0.0924` n `792`
- 1h: commodity avg `-0.0003` n `12`; crypto_alt avg `0.3514` n `231`; crypto_major avg `-0.0288` n `8`; equity avg `0.1678` n `127`; fx avg `-0.0408` n `6`; index avg `0.0585` n `26`; metal avg `-0.0834` n `20`; unknown avg `0.1436` n `792`
- 4h: commodity avg `0.0016` n `12`; crypto_alt avg `0.5781` n `231`; crypto_major avg `0.2661` n `8`; equity avg `-0.1978` n `127`; fx avg `-0.038` n `6`; index avg `0.0365` n `26`; metal avg `-0.0819` n `20`; unknown avg `-0.0566` n `792`
- 24h: commodity avg `0.3734` n `12`; crypto_alt avg `1.6383` n `231`; crypto_major avg `2.7782` n `8`; equity avg `0.2303` n `127`; fx avg `0.002` n `6`; index avg `0.0457` n `26`; metal avg `-0.0044` n `20`; unknown avg `1.1023` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
