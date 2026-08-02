# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T09:52:26.943427+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0765` n `12`; crypto_alt avg `0.0354` n `230`; crypto_major avg `-0.0313` n `8`; equity avg `0.0489` n `102`; fx avg `-0.0098` n `6`; index avg `-0.0029` n `25`; metal avg `0.0047` n `20`; unknown avg `-0.014` n `782`
- 1h: commodity avg `0.0229` n `12`; crypto_alt avg `0.0932` n `230`; crypto_major avg `0.046` n `8`; equity avg `0.0157` n `102`; fx avg `0.0767` n `6`; index avg `-0.0323` n `25`; metal avg `0.0033` n `20`; unknown avg `0.0867` n `782`
- 4h: commodity avg `-0.071` n `12`; crypto_alt avg `-0.0304` n `230`; crypto_major avg `-0.3481` n `8`; equity avg `0.188` n `102`; fx avg `-0.0314` n `6`; index avg `0.0195` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.066` n `766`
- 24h: commodity avg `-1.1176` n `12`; crypto_alt avg `0.5517` n `230`; crypto_major avg `0.3702` n `8`; equity avg `1.0142` n `102`; fx avg `-0.1626` n `6`; index avg `0.213` n `25`; metal avg `0.2429` n `20`; unknown avg `0.2959` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
