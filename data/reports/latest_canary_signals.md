# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T13:52:27.702918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `-0.0432` n `230`; crypto_major avg `-0.0189` n `8`; equity avg `0.1922` n `114`; fx avg `-0.0123` n `6`; index avg `0.0391` n `25`; metal avg `0.0808` n `20`; unknown avg `0.0078` n `792`
- 1h: commodity avg `-0.0162` n `12`; crypto_alt avg `0.1368` n `230`; crypto_major avg `0.2925` n `8`; equity avg `0.2897` n `114`; fx avg `0.0158` n `6`; index avg `0.0624` n `25`; metal avg `0.0626` n `20`; unknown avg `0.0846` n `792`
- 4h: commodity avg `0.0303` n `12`; crypto_alt avg `0.3294` n `230`; crypto_major avg `0.3116` n `8`; equity avg `-0.0662` n `114`; fx avg `0.0033` n `6`; index avg `0.0263` n `25`; metal avg `0.0162` n `20`; unknown avg `2.0123` n `792`
- 24h: commodity avg `0.0163` n `12`; crypto_alt avg `-0.0902` n `230`; crypto_major avg `0.8343` n `8`; equity avg `1.1879` n `114`; fx avg `0.0111` n `6`; index avg `0.1502` n `25`; metal avg `0.1596` n `20`; unknown avg `0.0076` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
