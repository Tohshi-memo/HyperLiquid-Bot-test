# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T22:52:33.292183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `-0.0749` n `230`; crypto_major avg `-0.0205` n `8`; equity avg `-0.0064` n `114`; fx avg `0.0037` n `6`; index avg `0.0086` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.0236` n `793`
- 1h: commodity avg `0.023` n `12`; crypto_alt avg `-0.3722` n `230`; crypto_major avg `-0.0918` n `8`; equity avg `0.0772` n `114`; fx avg `0.0178` n `6`; index avg `0.0153` n `25`; metal avg `-0.0211` n `20`; unknown avg `-0.0329` n `792`
- 4h: commodity avg `0.1571` n `12`; crypto_alt avg `-0.458` n `230`; crypto_major avg `-0.1712` n `8`; equity avg `-0.1617` n `114`; fx avg `0.0106` n `6`; index avg `-0.0094` n `25`; metal avg `0.0053` n `20`; unknown avg `-0.0097` n `792`
- 24h: commodity avg `0.5721` n `12`; crypto_alt avg `0.4536` n `230`; crypto_major avg `1.4456` n `8`; equity avg `1.2202` n `114`; fx avg `0.0319` n `6`; index avg `0.0671` n `25`; metal avg `0.1142` n `20`; unknown avg `0.2822` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
