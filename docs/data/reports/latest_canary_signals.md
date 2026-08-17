# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T11:37:27.148938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0948` n `12`; crypto_alt avg `0.0329` n `230`; crypto_major avg `-0.0076` n `8`; equity avg `-0.0898` n `114`; fx avg `-0.0059` n `6`; index avg `-0.0051` n `25`; metal avg `0.0082` n `20`; unknown avg `0.0024` n `792`
- 1h: commodity avg `-0.0935` n `12`; crypto_alt avg `0.1621` n `230`; crypto_major avg `0.0625` n `8`; equity avg `-0.1858` n `114`; fx avg `-0.015` n `6`; index avg `-0.0113` n `25`; metal avg `0.02` n `20`; unknown avg `1.137` n `792`
- 4h: commodity avg `0.1056` n `12`; crypto_alt avg `0.0102` n `230`; crypto_major avg `0.0252` n `8`; equity avg `-0.0989` n `114`; fx avg `-0.0101` n `6`; index avg `-0.0126` n `25`; metal avg `-0.1033` n `20`; unknown avg `0.0089` n `792`
- 24h: commodity avg `-0.1566` n `12`; crypto_alt avg `0.055` n `230`; crypto_major avg `0.9654` n `8`; equity avg `1.1304` n `114`; fx avg `-0.0187` n `6`; index avg `0.1394` n `25`; metal avg `0.2109` n `20`; unknown avg `0.118` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
