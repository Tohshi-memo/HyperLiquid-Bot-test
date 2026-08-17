# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T14:07:32.311078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0391` n `12`; crypto_alt avg `-0.0924` n `230`; crypto_major avg `-0.1234` n `8`; equity avg `-0.1146` n `114`; fx avg `0.0093` n `6`; index avg `-0.0206` n `25`; metal avg `-0.0379` n `20`; unknown avg `0.0095` n `792`
- 1h: commodity avg `0.0239` n `12`; crypto_alt avg `-0.041` n `230`; crypto_major avg `0.0579` n `8`; equity avg `0.0844` n `114`; fx avg `0.0018` n `6`; index avg `0.0297` n `25`; metal avg `0.051` n `20`; unknown avg `0.0237` n `792`
- 4h: commodity avg `-0.0388` n `12`; crypto_alt avg `0.1274` n `230`; crypto_major avg `0.1326` n `8`; equity avg `-0.1869` n `114`; fx avg `0.0139` n `6`; index avg `0.0147` n `25`; metal avg `0.0249` n `20`; unknown avg `2.0539` n `792`
- 24h: commodity avg `-0.0448` n `12`; crypto_alt avg `-0.1917` n `230`; crypto_major avg `0.6676` n `8`; equity avg `1.078` n `114`; fx avg `0.0159` n `6`; index avg `0.1363` n `25`; metal avg `0.1647` n `20`; unknown avg `0.0176` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
