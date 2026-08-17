# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T11:12:36.300206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.031` n `12`; crypto_alt avg `0.0598` n `230`; crypto_major avg `0.039` n `8`; equity avg `-0.0359` n `114`; fx avg `0.0178` n `6`; index avg `0.0013` n `25`; metal avg `0.0128` n `20`; unknown avg `0.0462` n `792`
- 1h: commodity avg `-0.0622` n `12`; crypto_alt avg `0.3009` n `230`; crypto_major avg `0.452` n `8`; equity avg `0.0959` n `114`; fx avg `-0.0135` n `6`; index avg `0.0244` n `25`; metal avg `0.0571` n `20`; unknown avg `2.0768` n `792`
- 4h: commodity avg `0.1648` n `12`; crypto_alt avg `-0.1129` n `230`; crypto_major avg `0.0605` n `8`; equity avg `0.1103` n `114`; fx avg `0.0053` n `6`; index avg `0.0013` n `25`; metal avg `-0.028` n `20`; unknown avg `0.0032` n `792`
- 24h: commodity avg `-0.0761` n `12`; crypto_alt avg `0.0455` n `230`; crypto_major avg `1.0091` n `8`; equity avg `1.2827` n `114`; fx avg `-0.0256` n `6`; index avg `0.155` n `25`; metal avg `0.2013` n `20`; unknown avg `0.1204` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
