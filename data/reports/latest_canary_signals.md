# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T02:07:29.753509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0251` n `12`; crypto_alt avg `-0.0195` n `230`; crypto_major avg `-0.06` n `8`; equity avg `-0.15` n `94`; fx avg `-0.0078` n `6`; index avg `-0.0655` n `25`; metal avg `-0.0437` n `20`; unknown avg `-0.0301` n `768`
- 1h: commodity avg `-0.065` n `12`; crypto_alt avg `0.18` n `230`; crypto_major avg `0.0799` n `8`; equity avg `-0.1328` n `94`; fx avg `-0.0157` n `6`; index avg `-0.0522` n `25`; metal avg `-0.0992` n `20`; unknown avg `-0.2171` n `768`
- 4h: commodity avg `-0.0781` n `12`; crypto_alt avg `0.0363` n `230`; crypto_major avg `-0.2061` n `8`; equity avg `-0.6392` n `94`; fx avg `-0.0067` n `6`; index avg `-0.2317` n `25`; metal avg `-0.2679` n `20`; unknown avg `-0.1192` n `766`
- 24h: commodity avg `-0.0712` n `12`; crypto_alt avg `0.336` n `230`; crypto_major avg `0.7028` n `8`; equity avg `-2.044` n `93`; fx avg `0.1632` n `6`; index avg `-0.4968` n `25`; metal avg `-0.0968` n `20`; unknown avg `0.1004` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
