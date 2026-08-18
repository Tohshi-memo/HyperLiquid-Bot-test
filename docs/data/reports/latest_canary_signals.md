# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T10:52:32.601385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `-0.0295` n `230`; crypto_major avg `-0.0065` n `8`; equity avg `0.1431` n `114`; fx avg `-0.0001` n `6`; index avg `0.0242` n `25`; metal avg `0.0032` n `20`; unknown avg `-0.0001` n `795`
- 1h: commodity avg `-0.0467` n `12`; crypto_alt avg `0.0044` n `230`; crypto_major avg `0.1116` n `8`; equity avg `0.1636` n `114`; fx avg `0.0053` n `6`; index avg `0.035` n `25`; metal avg `0.0558` n `20`; unknown avg `0.361` n `795`
- 4h: commodity avg `-0.1558` n `12`; crypto_alt avg `0.1107` n `230`; crypto_major avg `-0.1764` n `8`; equity avg `-1.0155` n `114`; fx avg `-0.0204` n `6`; index avg `-0.1063` n `25`; metal avg `-0.0859` n `20`; unknown avg `-0.0249` n `793`
- 24h: commodity avg `0.5098` n `12`; crypto_alt avg `-0.8878` n `230`; crypto_major avg `-0.1511` n `8`; equity avg `-2.7215` n `114`; fx avg `-0.0168` n `6`; index avg `-0.5323` n `25`; metal avg `-0.2116` n `20`; unknown avg `-0.0109` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
