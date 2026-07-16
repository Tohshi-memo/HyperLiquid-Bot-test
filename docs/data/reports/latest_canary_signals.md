# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T03:37:32.104655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0594` n `12`; crypto_alt avg `-0.0187` n `230`; crypto_major avg `-0.0105` n `8`; equity avg `-0.0572` n `94`; fx avg `-0.0068` n `6`; index avg `0.0037` n `25`; metal avg `0.0562` n `20`; unknown avg `-0.1538` n `768`
- 1h: commodity avg `-0.1132` n `12`; crypto_alt avg `-0.1005` n `230`; crypto_major avg `-0.015` n `8`; equity avg `0.0991` n `94`; fx avg `-0.0148` n `6`; index avg `0.0048` n `25`; metal avg `0.0645` n `20`; unknown avg `-0.3809` n `768`
- 4h: commodity avg `-0.1605` n `12`; crypto_alt avg `-0.0568` n `230`; crypto_major avg `-0.2257` n `8`; equity avg `-0.2409` n `94`; fx avg `-0.02` n `6`; index avg `-0.1213` n `25`; metal avg `-0.1404` n `20`; unknown avg `-0.561` n `766`
- 24h: commodity avg `-0.1875` n `12`; crypto_alt avg `0.2457` n `230`; crypto_major avg `0.1974` n `8`; equity avg `-2.2083` n `93`; fx avg `0.1091` n `6`; index avg `-0.4518` n `25`; metal avg `0.0192` n `20`; unknown avg `-0.1403` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
